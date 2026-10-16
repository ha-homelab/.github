"""Reproduce the original public architecture SVG; no external assets or data."""

from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
INK = "#172b3a"
BLUE = "#175f9b"
MUTED = "#526574"


def text(x, y, value, size=18, color=INK, weight=400):
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" '
        f'font-weight="{weight}">{escape(value)}</text>'
    )


def box(x, y, title, lines, color=BLUE):
    result = (
        f'<rect x="{x}" y="{y}" width="470" height="148" rx="10" '
        f'fill="#f7f9fb" stroke="{color}" stroke-width="2"/>'
    )
    result += text(x + 20, y + 34, title, 23, color, 650)
    for offset, line in enumerate(lines):
        result += text(x + 20, y + 67 + 27 * offset, line, 18, MUTED)
    return result


def arrow(x1, y1, x2, y2):
    return (
        f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{BLUE}" '
        'stroke-width="2.5" fill="none" marker-end="url(#arrow)"/>'
    )


def build():
    body = text(38, 43, "Evidence before automation", 30, INK, 650)
    body += text(
        38,
        78,
        "Four separate tools · local files · synthetic fixtures · review handoffs",
        20,
        MUTED,
    )
    body += box(
        38,
        117,
        "1. Entity migration plan",
        [
            "Role + hardware + capabilities + fingerprints",
            "Output: ready or blocked changes",
            "Question: what should move?",
        ],
    )
    body += box(
        592,
        117,
        "2. Meter contracts",
        [
            "Physical scope + provenance + sample quality",
            "Output: findings and eligible sums",
            "Question: what does this value cover?",
        ],
    )
    body += box(
        38,
        331,
        "3. Real HA scenario engine",
        [
            "Reviewed synthetic timeline + assertions",
            "Output: ordered calls and final states",
            "Question: what does this sequence do?",
        ],
    )
    body += box(
        592,
        331,
        "4. Voice evidence",
        [
            "Recorded action + API + audible observation",
            "Output: pass, fail or incomplete evidence",
            "Question: was the requested outcome seen?",
        ],
    )
    body += arrow(273, 268, 273, 324)
    body += text(289, 303, "Reviewed handoff", 17, BLUE)
    body += text(617, 303, "Independent evidence checks", 17, BLUE)
    body += '<path d="M38 525 H1062" stroke="#a52a2a" stroke-width="2" stroke-dasharray="8 6"/>'
    body += text(
        38, 559, "Physical acceptance remains a separate step", 24, "#a52a2a", 650
    )
    body += text(
        38,
        593,
        "Radio delivery · relay/contact behavior · actual load · water flow · audible sound",
        20,
        MUTED,
    )
    body += text(
        38,
        630,
        "No automatic deployment. No whole-strip watts claimed as one outlet. No unknown = success.",
        19,
        INK,
    )
    body += text(
        38,
        684,
        "Original synthetic architecture · MIT · Reproduce with render_architecture.py",
        15,
        MUTED,
    )
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 715" '
        'role="img" aria-labelledby="title desc">\n'
        '<title id="title">Evidence before automation</title>'
        '<desc id="desc">Four tools: entity migration planning, meter contracts, a real '
        "Home Assistant synthetic scenario engine and voice evidence evaluation. "
        "Arrows describe human review handoffs, not automatic integrations. Physical "
        "acceptance and deployment remain separate.</desc>"
        '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" '
        'refY="4" orient="auto"><path d="M0 0 L8 4 L0 8" fill="#175f9b"/></marker></defs>'
        '<rect width="1100" height="715" fill="white"/>'
        '<g font-family="system-ui, sans-serif">' + body + "</g></svg>\n"
    )


if __name__ == "__main__":
    (ROOT / "architecture.svg").write_text(build())
