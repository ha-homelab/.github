"""Refresh documentation language links from languages.json; no network needed."""

import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LANGUAGES = json.loads((ROOT / "languages.json").read_text(encoding="utf-8"))
START = "<!-- language-navigation:start -->"
END = "<!-- language-navigation:end -->"


def filename(stem, code):
    return f"{stem}{'' if code == 'en' else '.' + code}.md"


def navigation(directory, stem):
    """Use absolute profile links because GitHub embeds that page at org root."""
    if directory == "profile":
        prefix = "https://github.com/ha-homelab/.github/blob/main/profile/"
    elif directory == "root":
        prefix = "community-tools/"
    else:
        prefix = ""
    links = []
    for item in LANGUAGES:
        href = prefix + filename(stem, item["code"])
        links.append(
            f'<a href="{href}" lang="{item["code"]}" '
            f'dir="{item.get("dir", "ltr")}">{escape(item["label"])}</a>'
        )
    rows = [" · ".join(links[i : i + 8]) for i in range(0, len(links), 8)]
    alignment = ' align="center"' if directory == "profile" else ""
    return (
        f'{START}\n<p dir="ltr"{alignment}>\n' + "<br>\n".join(rows) + f"\n</p>\n{END}"
    )


def pages():
    yield ROOT / "README.md", "root", "README"
    for language in LANGUAGES:
        for directory, stem in (
            ("profile", "README"),
            ("community-tools", "README"),
            ("community-tools", "process-and-results"),
        ):
            yield ROOT / directory / filename(stem, language["code"]), directory, stem


def update(body, directory, stem):
    if body.count(START) != 1 or body.count(END) != 1:
        raise ValueError("Each page must contain one language-navigation block")
    return re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        lambda _: navigation(directory, stem),
        body,
        flags=re.DOTALL,
    )


if __name__ == "__main__":
    for path, directory, stem in pages():
        path.write_text(
            update(path.read_text(encoding="utf-8"), directory, stem),
            encoding="utf-8",
        )
