"""Render localized SVGs from checked-in evidence; standard library only."""

import json
import re
import textwrap
import unicodedata
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
INK, MUTED, BG, LINE = "#15283f", "#486078", "#f5f8fc", "#cbd8e5"
COLORS = ("#116f93", "#087967", "#7052b5", "#b54537")
PALE = ("#e2f3fb", "#e0f4ec", "#eee8fa", "#fcece5")
NAMES = (
    "Entity Migrations",
    "Meter Contracts",
    "Scenario Tests",
    "Assist Scenario Lab",
)


LANGUAGES = tuple(
    entry["code"]
    for entry in json.loads(
        (ROOT.parent / "languages.json").read_text(encoding="utf-8")
    )
)
TRANSLATIONS = {
    lang: json.loads((ROOT / "locales" / f"{lang}.json").read_text(encoding="utf-8"))
    for lang in LANGUAGES
}


def tr(lang, en):
    return TRANSLATIONS[lang][en]


def text(x, y, value, size=18, color=INK, weight=400, anchor="start"):
    # Keep geometric alignment while letting the browser shape RTL text.
    rtl = any(unicodedata.bidirectional(c) in {"R", "AL"} for c in str(value))
    direction = ' direction="rtl" unicode-bidi="plaintext"' if rtl else ""
    if rtl:
        anchor = {"start": "end", "end": "start", "middle": "middle"}[anchor]
    content = escape(str(value))
    if rtl:
        # ISO dates keep year-month-day order inside a right-to-left caption.
        content = re.sub(
            r"\b\d{4}-\d{2}-\d{2}\b",
            lambda match: (
                f'<tspan direction="ltr" unicode-bidi="embed">{match[0]}</tspan>'
            ),
            content,
        )
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" '
        f'font-weight="{weight}" text-anchor="{anchor}"{direction}>{content}</text>'
    )


def wrapped(value, width):
    """Wrap CJK/Thai labels without dropping marks or assuming word spaces."""
    needs_unicode_wrap = any(
        unicodedata.east_asian_width(c) in {"W", "F"}
        or "\u0e00" <= c <= "\u0e7f"
        or unicodedata.category(c).startswith("M")
        for c in value
    )
    if not needs_unicode_wrap:
        return textwrap.wrap(value, width=width, break_long_words=False)
    clusters = []
    for char in value:
        attaches = (
            unicodedata.category(char).startswith("M")
            or char == "\u200d"
            or (
                clusters
                and (
                    clusters[-1].endswith("\u200d")
                    or "\u0e40" <= clusters[-1][-1] <= "\u0e44"
                    or unicodedata.name(clusters[-1][-1], "").endswith("VIRAMA")
                )
            )
        )
        if attaches and clusters:
            clusters[-1] += char
        else:
            clusters.append(char)

    def units(cluster):
        # Spacing vowel marks in Indic scripts occupy width even though they
        # belong to the preceding letter; counting them as zero overfills cards.
        return sum(
            0.5
            if unicodedata.category(c) == "Mc"
            else 0
            if unicodedata.category(c).startswith(("M", "C"))
            else 2
            if unicodedata.east_asian_width(c) in {"W", "F"}
            else 1
            for c in cluster
        )

    # Japanese kinsoku: do not begin a line with small kana, closing punctuation
    # or a prolonged-sound mark, or leave an opening bracket at the line end.
    nonstarters = set(
        "、。，．？！：；ー々ヽヾゝゞぁぃぅぇぉっゃゅょゎゕゖ"
        "ァィゥェォッャュョヮヵヶ）］｝〉》」』】〕〗〙〛)]}”’"
    ) | {chr(code) for code in range(0x31F0, 0x3200)}
    openers = set("（［｛〈《「『【〔〖〘〚([{“‘")

    def legal(index, remaining):
        return (
            index > 0
            and remaining[index - 1][-1] not in openers
            and remaining[index][0] not in nonstarters
        )

    result = []
    while clusters:
        used, fit = 0, 0
        for cluster in clusters:
            if fit and used + units(cluster) > width:
                break
            used += units(cluster)
            fit += 1
        if fit == len(clusters):
            result.append("".join(clusters).rstrip())
            break

        spaces = [
            i for i in range(1, fit + 1) if clusters[i].isspace() and legal(i, clusters)
        ]
        cut = spaces[-1] if spaces else fit
        while cut > 1 and not legal(cut, clusters):
            cut -= 1
        result.append("".join(clusters[:cut]).rstrip())
        clusters = clusters[cut:]
        while clusters and clusters[0].isspace():
            clusters.pop(0)
    return result


def lines(x, y, value, width=30, size=18, color=MUTED, weight=400):
    return "".join(
        text(x, y + n * (size + 7), line, size, color, weight)
        for n, line in enumerate(wrapped(value, width))
    )


def rect(x, y, w, h, fill="white", stroke="none", radius=16):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
        f'fill="{fill}" stroke="{stroke}"/>'
    )


def path(d, color=LINE, width=2, dash=""):
    attr = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{attr}/>'


def arrow(x1, y1, x2, y2):
    return path(f"M{x1} {y1} L{x2} {y2}", MUTED) + path(
        f"M{x2 - 5} {y2 - 8} L{x2} {y2} L{x2 + 5} {y2 - 8}", MUTED
    )


def header(label, title, subtitle):
    return (
        rect(0, 0, 1200, 152, INK, radius=0)
        + rect(40, 30, 6, 92, "#43d0bd", radius=3)
        + text(62, 49, label, 15, "#91e4da", 650)
        + text(62, 91, title, 32, "white", 700)
        + text(62, 125, subtitle, 17, "#d4e1ef")
    )


def svg(lang, height, title, desc, body):
    identifier = f"visual-{lang}-{height}"
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {height}" '
        f'lang="{lang}" role="img" aria-labelledby="{identifier}-title {identifier}-desc">\n'
        f'<title id="{identifier}-title">{escape(title)}</title><desc id="{identifier}-desc">{escape(desc)}</desc>'
        f'<rect width="1200" height="{height}" fill="{BG}"/>'
        '<g font-family="Arial, DejaVu Sans, sans-serif">' + body + "</g></svg>\n"
    )


def build(lang="en"):
    title = tr(lang, "From a proposed change to reviewed evidence")
    desc = tr(
        lang,
        "Choose relevant independent checks, review their outputs, then perform separate physical acceptance. Arrows are human handoffs, not a deployed pipeline.",
    )
    body = header(
        "HA HOMELAB / 01",
        title,
        tr(lang, "Four tools. Explicit inputs. Review before deployment."),
    )
    body += rect(40, 180, 1120, 59, "#e6edf5")
    body += text(
        600,
        217,
        tr(
            lang,
            "01  Prepare local inputs and select the checks relevant to the change",
        ),
        21,
        INK,
        600,
        "middle",
    )
    questions = [
        tr(lang, "What should move?"),
        tr(lang, "What is measured?"),
        tr(lang, "What will HA do?"),
        tr(lang, "What was observed?"),
    ]
    inputs = [
        tr(lang, "Manifest, snapshot and supported source files"),
        tr(lang, "Meter topology, timestamps, units and source identity"),
        tr(lang, "Synthetic timeline, initial states and assertions"),
        tr(lang, "Local records of intent, action and audible response"),
    ]
    outputs = [
        tr(lang, "Plan + conflicts"),
        tr(lang, "Findings + valid sums"),
        tr(lang, "Calls + final states"),
        tr(lang, "Outcome + evidence gaps"),
    ]
    for i in range(4):
        x = 40 + 286 * i
        body += arrow(x + 131, 239, x + 131, 270)
        body += rect(x, 279, 262, 284, "white", LINE) + rect(
            x, 279, 262, 8, COLORS[i], radius=4
        )
        body += text(x + 18, 323, NAMES[i], 21, COLORS[i], 700)
        body += text(x + 18, 359, questions[i], 19, INK, 600)
        body += lines(x + 18, 396, inputs[i], 24, 18)
        body += rect(x + 14, 497, 234, 48, PALE[i], radius=8)
        output_lines = wrapped(outputs[i], 24)
        for line_number, label in enumerate(output_lines):
            baseline = 527 if len(output_lines) == 1 else 516 + 22 * line_number
            body += text(x + 131, baseline, label, 17, COLORS[i], 650, "middle")
        body += arrow(x + 131, 563, x + 131, 597)
    body += rect(40, 606, 1120, 85, INK)
    body += text(
        62,
        641,
        tr(lang, "02  Review scope, conflicts and missing evidence"),
        24,
        "white",
        650,
    )
    body += text(
        62,
        674,
        tr(
            lang,
            "Keep reports with the change; fix invalid inputs and rerun the relevant checks.",
        ),
        18,
        "#d4e1ef",
    )
    body += path("M40 723 H1160", COLORS[3], 2, "8 7")
    body += text(
        40,
        763,
        tr(lang, "03  Deploy through review, then verify the actual device"),
        25,
        COLORS[3],
        650,
    )
    body += text(
        40,
        797,
        tr(
            lang,
            "Radio delivery · relay contacts · actual load · source timing · audible sound",
        ),
        18,
    )
    body += text(
        40,
        843,
        tr(
            lang,
            "Arrows = human review handoffs. These tools do not implement an automatic deployment pipeline.",
        ),
        16,
        MUTED,
    )
    return svg(lang, 874, title, desc, body)


def results(lang="en"):
    title = tr(lang, "Inputs, checks and results")
    desc = tr(
        lang,
        "Illustrated summaries of inputs, checks and outputs. Synthetic arithmetic: 700 W plus 0.02 kW plus 0 W equals 720 W. Not raw report screenshots.",
    )
    body = header(
        "HA HOMELAB / 02",
        title,
        tr(lang, "Illustrated summaries of the bundled synthetic examples"),
    )
    for x, label in zip(
        (62, 280, 592, 913),
        (
            tr(lang, "TOOL"),
            tr(lang, "INPUT"),
            tr(lang, "CHECK / PROCESS"),
            tr(lang, "RESULT"),
        ),
    ):
        body += text(x, 202, label, 14, MUTED, 700)
    rows = [
        (
            "Entity Migrations",
            "light.table → switch.table",
            tr(lang, "Check role policy, capabilities and supported references"),
            tr(lang, "Reviewable plan; conflicts block readiness"),
        ),
        (
            "Meter Contracts",
            "700 W + 0.02 kW + 0 W",
            tr(lang, "Normalize units; verify freshness and distinct sources"),
            tr(lang, "720 W total; review shared and duplicate sources"),
        ),
        (
            "Scenario Tests",
            "scenario_table_off",
            tr(lang, "Run real HA with synthetic callbacks and exact assertions"),
            tr(lang, "1 expected call; new OFF, retired plug stays ON"),
        ),
        (
            "Assist Scenario Lab",
            tr(lang, "API finished; audible observation missing"),
            tr(lang, "Evaluate correctness, action and audibility separately"),
            tr(lang, "Incomplete evidence; bundled example exits 3"),
        ),
    ]
    for i, (name, source, process, result) in enumerate(rows):
        y = 222 + 155 * i
        body += rect(40, y, 1120, 137, "white", LINE) + rect(40, y, 207, 137, PALE[i])
        body += lines(60, y + 48, name, 16, 21, COLORS[i], 700)
        body += lines(280, y + 37, source, 26, 18, INK)
        body += lines(592, y + 37, process, 27, 18)
        body += lines(913, y + 37, result, 22, 18, COLORS[i], 600)
    body += text(
        40,
        884,
        tr(
            lang,
            "A valid sum, a ready plan, a passed scenario and audible evidence answer different questions.",
        ),
        18,
        INK,
        600,
    )
    body += text(
        40,
        919,
        tr(lang, "Sources and exact commands: process-and-results.md."),
        16,
        MUTED,
    )
    return svg(lang, 949, title, desc, body)


def validation(lang="en"):
    evidence = json.loads(
        (ROOT / "validation-evidence.json").read_text(encoding="utf-8")
    )
    title = tr(lang, "Recorded Linux test results")
    body = header(
        "HA HOMELAB / 03",
        title,
        tr(
            lang, "{date} UTC evidence snapshot · test counts, not device performance"
        ).format(date=evidence["snapshot_date_utc"]),
    )
    left, top, scale = 338, 220, 8.7
    for tick in range(0, 81, 20):
        x = left + tick * scale
        body += path(f"M{x} {top} V612", LINE)
        body += text(x, 644, tick, 16, MUTED, anchor="middle")
    for i, item in enumerate(evidence["projects"]):
        y = top + 24 + i * 97
        body += text(40, y + 27, item["label"], 23, COLORS[i], 650)
        body += rect(left, y, item["passed"] * scale, 39, COLORS[i], radius=5)
        body += text(
            left + item["passed"] * scale + 14,
            y + 27,
            f"{item['passed']} " + tr(lang, "passed"),
            18,
            COLORS[i],
            700,
        )
        if item["skipped"]:
            body += rect(
                left + (item["passed"] + 15) * scale,
                y + 5,
                22,
                28,
                "white",
                COLORS[i],
                3,
            )
            body += text(
                left + (item["passed"] + 15) * scale + 34,
                y + 27,
                tr(lang, "1 skipped*"),
                17,
                MUTED,
            )
        if item.get("runtime_cases"):
            body += text(
                left + 12,
                y + 66,
                tr(lang, "Includes 7 tests using the actual Home Assistant engine"),
                17,
                MUTED,
            )
    body += text(
        686,
        680,
        tr(lang, "Passed test cases (count)"),
        18,
        INK,
        600,
        "middle",
    )
    body += rect(40, 714, 1120, 105, "#e6edf5")
    body += text(
        62,
        748,
        tr(
            lang,
            "* Case-insensitive filesystem test skipped on Linux; exercised on macOS.",
        ),
        18,
    )
    body += text(
        62,
        779,
        tr(
            lang,
            "Different suites cover different scopes. Bar length is not a quality or safety ranking.",
        ),
        18,
    )
    body += text(
        40,
        857,
        tr(
            lang,
            "Source: validation-evidence.json → four linked GitHub Actions runs. No live polling.",
        ),
        16,
        MUTED,
    )
    desc = tr(
        lang,
        "Passed tests: Entity Migrations 36 and one skip; Meter Contracts 75; Scenario Tests 54 including seven real-HA tests; Assist Scenario Lab 24. Counts do not rank quality.",
    )
    return svg(lang, 888, title, desc, body)


def role_transfer(lang="en"):
    title = tr(lang, "Role transfer: one event, two distinct outcomes")
    body = header(
        "HA HOMELAB / 04",
        title,
        tr(
            lang,
            "Bundled synthetic scenario · actual HA engine · in-memory device callbacks",
        ),
    )
    for x, label in [
        (340, tr(lang, "INITIAL")),
        (700, tr(lang, "EVENT / ACTION")),
        (1080, tr(lang, "FINAL")),
    ]:
        body += text(x, 207, label, 15, MUTED, 700, "middle")
    for y in (252, 425):
        body += rect(40, y - 16, 1120, 147, "white", LINE)
        for yy, label in ((y + 30, "ON"), (y + 91, "OFF")):
            body += path(f"M316 {yy} H1115", LINE, 1) + text(
                274, yy + 6, label, 17, MUTED
            )
    body += path("M700 224 V583", MUTED, 2, "5 6")
    body += lines(
        62,
        284,
        tr(lang, "Retired hardware"),
        16,
        22,
        COLORS[0],
        700,
    )
    body += text(62, 347, tr(lang, "No command sent"), 17, MUTED)
    body += lines(
        62,
        457,
        tr(lang, "Replacement role"),
        18,
        22,
        COLORS[2],
        700,
    )
    body += text(62, 520, tr(lang, "One turn_off call"), 17, MUTED)
    body += path("M340 282 H1080", COLORS[0], 6) + path(
        "M340 455 H700 V516 H1080", COLORS[2], 6
    )
    for x, y, color in (
        (340, 282, COLORS[0]),
        (1080, 282, COLORS[0]),
        (340, 455, COLORS[2]),
        (1080, 516, COLORS[2]),
    ):
        body += f'<circle cx="{x}" cy="{y}" r="8" fill="{color}"/>'
    body += text(
        600,
        612,
        tr(lang, "Logical sequence (not a measured time axis)"),
        19,
        INK,
        600,
        "middle",
    )
    body += rect(40, 647, 548, 110, PALE[2])
    body += text(60, 679, tr(lang, "EXPECTED CALL"), 14, COLORS[2], 700)
    body += text(60, 711, "switch.turn_off → switch.scenario_table", 19, COLORS[2], 600)
    body += text(60, 739, tr(lang, "Final state: off"), 18)
    body += rect(612, 647, 548, 110, PALE[0])
    body += text(632, 679, tr(lang, "FORBIDDEN CALL"), 14, COLORS[0], 700)
    body += text(
        632, 711, "turn_off → switch.scenario_retired_plug", 19, COLORS[0], 600
    )
    body += text(632, 739, tr(lang, "Final state: on"), 18)
    body += text(
        40,
        802,
        tr(
            lang,
            "Fixture requests 40 ms before the event and 100 ms to settle; these are not measured latency.",
        ),
        18,
    )
    body += text(
        40,
        838,
        tr(
            lang,
            "Source: role-transfer.scenario.json · physical relay / power delivery not tested by this chart.",
        ),
        16,
        MUTED,
    )
    desc = tr(
        lang,
        "The old device stays on. One event turns the replacement off. Exactly one expected call, the old-device off call forbidden. Logical stages are not elapsed-time measurements.",
    )
    return svg(lang, 868, title, desc, body)


BUILDERS = {
    "architecture": build,
    "results": results,
    "validation": validation,
    "role-transfer": role_transfer,
}


def render_all():
    for name, builder in BUILDERS.items():
        for language in LANGUAGES:
            suffix = "" if language == "en" else f".{language}"
            (ROOT / f"{name}{suffix}.svg").write_text(
                builder(language), encoding="utf-8"
            )


if __name__ == "__main__":
    render_all()
