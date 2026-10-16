"""Render the profile's original diagrams from the dated public catalog.

Run from any directory: python3 assets/profile/render.py
Uses only the Python standard library; no network requests or live-household data.
"""

import json
from collections import Counter
from datetime import date
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
SNAPSHOT_DATE = date.fromisoformat(DATA["snapshot_date_los_angeles"])
MONTHS = {
    "en": [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ],
    "ru": [
        "января",
        "февраля",
        "марта",
        "апреля",
        "мая",
        "июня",
        "июля",
        "августа",
        "сентября",
        "октября",
        "ноября",
        "декабря",
    ],
}
SOURCE_DATES = {
    lang: f"{SNAPSHOT_DATE.day} {months[SNAPSHOT_DATE.month - 1]} {SNAPSHOT_DATE.year}"
    for lang, months in MONTHS.items()
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

LABELS = {
    "en": {
        "map": "A home, built from understandable parts",
        "sub": "Project roles across the HA Homelab ecosystem",
        "groups": [
            "Voice & media",
            "Devices & bridges",
            "Configuration & recovery",
            "Space, sensing & access",
            "Tests & contracts",
        ],
        "details": [
            ["EchoLocal · EchoMuse · Android", "Echo Dot / Show · LG capture"],
            ["DESLOC · RF · Zigbee · Z-Wave", "ESPHome conversions · SLZB recovery"],
            ["Home Assistant configuration", "k3s deployment & recovery"],
            ["Home Studio · RuView · ONVIF", "Sensing evidence · Access sessions"],
            [
                "Entity roles · Meter provenance",
                "Automation scenarios · Voice evidence",
            ],
        ],
        "mapnote": "Lines group related work; they are not an automatic deployment or a mandatory data path.",
        "chart": f"{DATA['public_project_count']} public projects, five areas",
        "chartsub": "A dated directory snapshot, not a quality or performance ranking",
        "axis": "Public projects (count)",
        "yaxis": "Project area",
        "source": f"Source: GitHub public repository API · {SOURCE_DATES['en']} (America/Los_Angeles)",
        "note": f"One category per project. The .github profile repository is excluded ({DATA['public_repository_count']} public repositories total).",
    },
    "ru": {
        "map": "Понятные части умного дома",
        "sub": "Роли проектов в экосистеме HA Homelab",
        "groups": [
            "Голос и медиа",
            "Устройства и мосты",
            "Конфигурация и восстановление",
            "Пространство, датчики, доступ",
            "Тесты и контракты",
        ],
        "details": [
            ["EchoLocal · EchoMuse · Android", "Echo Dot / Show · захват LG"],
            ["DESLOC · RF · Zigbee · Z-Wave", "Прошивка ESPHome · восстановление SLZB"],
            ["Конфигурация Home Assistant", "Развёртывание и восстановление k3s"],
            ["Home Studio · RuView · ONVIF", "Наблюдения · сессии Access"],
            [
                "Роли сущностей · источники показаний",
                "Сценарии автоматики · проверка голоса",
            ],
        ],
        "mapnote": "Линии связывают темы: это не автоматическое развёртывание и не обязательный путь данных.",
        "chart": f"Публичные проекты: {DATA['public_project_count']}. Направления: 5",
        "chartsub": "Срез каталога, а не рейтинг качества или производительности",
        "axis": "Количество публичных проектов",
        "yaxis": "Направление проектов",
        "source": f"Источник: GitHub API публичных репозиториев · {SOURCE_DATES['ru']} (America/Los_Angeles)",
        "note": f"Каждый проект учтён один раз. Без профиля .github (всего {DATA['public_repository_count']} публичных репозитория).",
    },
}


def text(x, y, value, size=18, fill="#c1d1dd", weight=400, anchor="start"):
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
        f'font-weight="{weight}" text-anchor="{anchor}">{escape(str(value))}</text>'
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
                15 if lang == "ru" else 18,
                "#ffffff",
                700,
            )
        )
        for line, value in enumerate(labels["details"][index]):
            svg.append(
                text(x + 18, y + 101 + line * 25, value, 12 if lang == "ru" else 14)
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
        suffix = ".ru" if language == "ru" else ""
        for name, builder in (("ecosystem", ecosystem), ("portfolio", portfolio)):
            (ROOT / f"{name}{suffix}.svg").write_text(
                builder(language), encoding="utf-8"
            )
