"""Render the profile's original diagrams from the dated public catalog.

Run from any directory: python3 assets/profile/render.py
Uses only the Python standard library; no network requests or live-household data.
"""

import json
import unicodedata
from collections import Counter
from datetime import date
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
SNAPSHOT_DATE = date.fromisoformat(DATA["snapshot_date_los_angeles"])
LANGUAGES = tuple(
    entry["code"]
    for entry in json.loads(
        (ROOT.parents[1] / "languages.json").read_text(encoding="utf-8")
    )
)
LOCALES = {
    lang: json.loads((ROOT / "locales" / f"{lang}.json").read_text(encoding="utf-8"))
    for lang in LANGUAGES
}
SOURCE_DATES = {
    lang: locale.get("date_format", "{day} {month} {year}").format(
        day=SNAPSHOT_DATE.day,
        month=locale["months"][SNAPSHOT_DATE.month - 1],
        year=SNAPSHOT_DATE.year,
    )
    for lang, locale in LOCALES.items()
}
CATEGORIES = [
    "Voice and media",
    "Device integrations, bridges and recovery",
    "Configuration and reliability",
    "Spatial tools, sensing and access",
    "Testing and contracts",
]
COUNTS = Counter(project["category"] for project in DATA["projects"])
assert dict(COUNTS) == DATA["category_counts"]
assert sum(COUNTS.values()) == DATA["public_project_count"]

LABELS = {lang: dict(locale["labels"]) for lang, locale in LOCALES.items()}
for lang, labels in LABELS.items():
    for key in ("chart", "source", "note"):
        labels[key] = labels[key].format(
            count=DATA["public_project_count"],
            total=DATA["public_repository_count"],
            date=SOURCE_DATES[lang],
        )


def text(x, y, value, size=18, fill="#c1d1dd", weight=400, anchor="start"):
    rtl = any(unicodedata.bidirectional(c) in {"R", "AL"} for c in str(value))
    direction = ' direction="rtl" unicode-bidi="plaintext"' if rtl else ""
    if rtl:
        anchor = {"start": "end", "end": "start", "middle": "middle"}[anchor]
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
        f'font-weight="{weight}" text-anchor="{anchor}"{direction}>{escape(str(value))}</text>'
    )


def start(title, description, height, lang):
    return [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="{height}" '
            f'viewBox="0 0 1120 {height}" role="img" aria-labelledby="title desc" lang="{lang}">'
        ),
        f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>',
        f'<rect width="1120" height="{height}" rx="20" fill="#102634"/>',
        '<g font-family="Arial, Helvetica, sans-serif">',
        text(40, 58, title, 30, "#ffffff", 700),
    ]


def ecosystem(lang):
    labels = LABELS[lang]
    svg = start(labels["map"], labels["mapnote"], 660, lang)
    svg.append(text(40, 91, labels["sub"], 18))
    svg.append(
        '<path d="M 340 226 H 385 V 333 H 415 M 340 459 H 385 V 333 '
        'M 705 333 H 735 V 226 H 780 M 735 333 V 459 H 780" '
        'fill="none" stroke="#4a7184" stroke-width="3"/>'
    )
    positions = [
        (40, 377, 300, 165),
        (40, 144, 300, 165),
        (415, 245, 290, 176),
        (780, 144, 300, 165),
        (780, 377, 300, 165),
    ]
    for index, (x, y, width, height) in enumerate(positions):
        central = index == 2
        svg.append(
            f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="14" '
            f'fill="{"#173f4e" if central else "#173342"}" stroke="#3b6474"/>'
        )
        svg.append(
            text(x + 18, y + 30, f"{COUNTS[CATEGORIES[index]]:02d}", 17, "#38d5cc", 700)
        )
        svg.append(
            text(
                x + 18,
                y + 67,
                labels["groups"][index],
                18 if lang == "en" else 15,
                "#ffffff",
                700,
            )
        )
        for line, value in enumerate(labels["details"][index]):
            svg.append(
                text(x + 18, y + 101 + line * 25, value, 14 if lang == "en" else 12)
            )
    svg.extend(
        [
            text(40, 600, labels["mapnote"], 15),
            text(40, 628, labels["source"], 13),
            "</g></svg>\n",
        ]
    )
    return "\n".join(svg)


def portfolio(lang):
    labels = LABELS[lang]
    svg = start(labels["chart"], labels["note"], 625, lang)
    svg.append(text(40, 91, labels["chartsub"], 18))
    svg.append(text(40, 139, labels["yaxis"], 14, "#94aebb"))
    x0, scale = 420, 80
    for tick in range(9):
        x = x0 + tick * scale
        svg.append(f'<line x1="{x}" y1="160" x2="{x}" y2="477" stroke="#294653"/>')
        svg.append(text(x, 501, tick, 16, anchor="middle"))
    for row, i in enumerate((1, 3, 0, 4, 2)):
        y = 177 + row * 62
        count = COUNTS[CATEGORIES[i]]
        svg.extend(
            [
                text(
                    40,
                    y + 24,
                    labels["groups"][i],
                    19 if lang == "en" else 17,
                    "#edf5f8",
                ),
                f'<rect x="{x0}" y="{y}" width="{count * scale}" height="36" rx="5" fill="#38d5cc"/>',
                text(x0 + count * scale + 14, y + 25, count, 21, "#ffffff", 700),
            ]
        )
    svg.extend(
        [
            text(740, 537, labels["axis"], 17, anchor="middle"),
            text(40, 577, labels["source"], 14),
            text(40, 602, labels["note"], 13),
            "</g></svg>\n",
        ]
    )
    return "\n".join(svg)


if __name__ == "__main__":
    for language in LABELS:
        suffix = "" if language == "en" else f".{language}"
        for name, builder in (("ecosystem", ecosystem), ("portfolio", portfolio)):
            (ROOT / f"{name}{suffix}.svg").write_text(
                builder(language), encoding="utf-8"
            )
