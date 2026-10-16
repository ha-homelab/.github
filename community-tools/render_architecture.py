"""Render original bilingual SVGs from checked-in evidence; standard library only."""

import json
import textwrap
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


def tr(lang, en, ru):
    return ru if lang == "ru" else en


def text(x, y, value, size=18, color=INK, weight=400, anchor="start"):
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" '
        f'font-weight="{weight}" text-anchor="{anchor}">{escape(str(value))}</text>'
    )


def lines(x, y, value, width=30, size=18, color=MUTED, weight=400):
    return "".join(
        text(x, y + n * (size + 7), line, size, color, weight)
        for n, line in enumerate(
            textwrap.wrap(value, width=width, break_long_words=False)
        )
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
    title = tr(
        lang,
        "From a proposed change to reviewed evidence",
        "От изменения к проверенному результату",
    )
    desc = tr(
        lang,
        "Choose relevant independent checks, review their outputs, then perform separate physical acceptance. Arrows are human handoffs, not a deployed pipeline.",
        "Выберите независимые проверки, оцените их результаты, затем проведите отдельную физическую приёмку. Стрелки — передача на ревью, а не готовый конвейер.",
    )
    body = header(
        "HA HOMELAB / 01",
        title,
        tr(
            lang,
            "Four tools. Explicit inputs. Review before deployment.",
            "Четыре инструмента. Явные входные данные. Ревью до внедрения.",
        ),
    )
    body += rect(40, 180, 1120, 59, "#e6edf5")
    body += text(
        600,
        217,
        tr(
            lang,
            "01  Prepare local inputs and select the checks relevant to the change",
            "01  Подготовьте локальные данные и выберите проверки для изменения",
        ),
        21,
        INK,
        600,
        "middle",
    )
    questions = [
        tr(lang, "What should move?", "Что переносим?"),
        tr(lang, "What is measured?", "Что измеряем?"),
        tr(lang, "What will HA do?", "Что выполнит HA?"),
        tr(lang, "What was observed?", "Что наблюдали?"),
    ]
    inputs = [
        tr(
            lang,
            "Manifest, snapshot and supported source files",
            "Манифест, снимок и поддерживаемые файлы",
        ),
        tr(
            lang,
            "Meter topology, timestamps, units and source identity",
            "Топология измерителей, время, единицы, источник",
        ),
        tr(
            lang,
            "Synthetic timeline, initial states and assertions",
            "Учебная последовательность, состояния и ожидания",
        ),
        tr(
            lang,
            "Local records of intent, action and audible response",
            "Локальные записи команды, действия и звука",
        ),
    ]
    outputs = [
        tr(lang, "Plan + conflicts", "План + конфликты"),
        tr(lang, "Findings + valid sums", "Замечания + суммы"),
        tr(lang, "Calls + final states", "Вызовы + состояния"),
        tr(lang, "Outcome + evidence gaps", "Итог + пробелы данных"),
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
        body += text(x + 131, 527, outputs[i], 17, COLORS[i], 650, "middle")
        body += arrow(x + 131, 563, x + 131, 597)
    body += rect(40, 606, 1120, 85, INK)
    body += text(
        62,
        641,
        tr(
            lang,
            "02  Review scope, conflicts and missing evidence",
            "02  Проверьте область, конфликты и недостающие данные",
        ),
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
            "Сохраните отчёты с изменением; исправьте входные данные и повторите нужные проверки.",
        ),
        18,
        "#d4e1ef",
    )
    body += path("M40 723 H1160", COLORS[3], 2, "8 7")
    body += text(
        40,
        763,
        tr(
            lang,
            "03  Deploy through review, then verify the actual device",
            "03  Внедрите через ревью и проверьте физическое устройство",
        ),
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
            "Радиосвязь · контакты реле · реальная нагрузка · время измерения · слышимый звук",
        ),
        18,
    )
    body += text(
        40,
        843,
        tr(
            lang,
            "Arrows = human review handoffs. These tools do not implement an automatic deployment pipeline.",
            "Стрелки = передача на ревью. Инструменты не образуют автоматический конвейер внедрения.",
        ),
        16,
        MUTED,
    )
    return svg(lang, 874, title, desc, body)


def results(lang="en"):
    title = tr(lang, "Inputs, checks and results", "Что именно означает результат")
    desc = tr(
        lang,
        "Illustrated summaries of inputs, checks and outputs. Synthetic arithmetic: 700 W plus 0.02 kW plus 0 W equals 720 W. Not raw report screenshots.",
        "Примеры входов, проверок и выходов. Учебная сумма: 700 Вт + 0,02 кВт + 0 Вт = 720 Вт. Это не скриншоты сырых отчётов.",
    )
    body = header(
        "HA HOMELAB / 02",
        title,
        tr(
            lang,
            "Illustrated summaries of the bundled synthetic examples",
            "Иллюстрированные результаты комплектных учебных примеров",
        ),
    )
    for x, label in zip(
        (62, 280, 592, 913),
        (
            tr(lang, "TOOL", "ИНСТРУМЕНТ"),
            tr(lang, "INPUT", "ВХОД"),
            tr(lang, "CHECK / PROCESS", "ПРОВЕРКА / ПРОЦЕСС"),
            tr(lang, "RESULT", "РЕЗУЛЬТАТ"),
        ),
    ):
        body += text(x, 202, label, 14, MUTED, 700)
    rows = [
        (
            "Entity Migrations",
            "light.table → switch.table",
            tr(
                lang,
                "Check role policy, capabilities and supported references",
                "Проверить роль, возможности и поддерживаемые ссылки",
            ),
            tr(
                lang,
                "Reviewable plan; conflicts block readiness",
                "План для ревью; конфликты блокируют готовность",
            ),
        ),
        (
            "Meter Contracts",
            "700 W + 0.02 kW + 0 W",
            tr(
                lang,
                "Normalize units; verify freshness and distinct sources",
                "Привести единицы; проверить свежесть и разные источники",
            ),
            tr(
                lang,
                "720 W total; review shared and duplicate sources",
                "Итого 720 Вт; проверить общие и повторные источники",
            ),
        ),
        (
            "Scenario Tests",
            "scenario_table_off",
            tr(
                lang,
                "Run real HA with synthetic callbacks and exact assertions",
                "Запустить настоящий HA с учебными обработчиками и ожиданиями",
            ),
            tr(
                lang,
                "1 expected call; new OFF, retired plug stays ON",
                "1 ожидаемый вызов; новый OFF, прежний остаётся ON",
            ),
        ),
        (
            "Assist Scenario Lab",
            tr(
                lang,
                "API finished; audible observation missing",
                "API завершён; нет наблюдения слышимого ответа",
            ),
            tr(
                lang,
                "Evaluate correctness, action and audibility separately",
                "Отдельно оценить команду, действие и слышимость",
            ),
            tr(
                lang,
                "Incomplete evidence; bundled example exits 3",
                "Недостаточно данных; неполный пример даёт код 3",
            ),
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
            "Верная сумма, готовый план, успешный тест и слышимый ответ отвечают на разные вопросы.",
        ),
        18,
        INK,
        600,
    )
    body += text(
        40,
        919,
        tr(
            lang,
            "Sources and exact commands: process-and-results.md.",
            "Источники и точные команды: process-and-results.ru.md.",
        ),
        16,
        MUTED,
    )
    return svg(lang, 949, title, desc, body)


def validation(lang="en"):
    evidence = json.loads((ROOT / "validation-evidence.json").read_text())
    title = tr(
        lang, "Recorded Linux test results", "Зафиксированные результаты Linux CI"
    )
    body = header(
        "HA HOMELAB / 03",
        title,
        tr(
            lang,
            f"{evidence['snapshot_date_utc']} UTC evidence snapshot · test counts, not device performance",
            f"Срез проверок: {evidence['snapshot_date_utc']} UTC · число тестов, не производительность устройств",
        ),
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
            f"{item['passed']} " + tr(lang, "passed", "прошло"),
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
                tr(lang, "1 skipped*", "1 пропуск*"),
                17,
                MUTED,
            )
        if item.get("runtime_cases"):
            body += text(
                left + 12,
                y + 66,
                tr(
                    lang,
                    "Includes 7 tests using the actual Home Assistant engine",
                    "Включая 7 тестов с настоящим движком Home Assistant",
                ),
                17,
                MUTED,
            )
    body += text(
        686,
        680,
        tr(lang, "Passed test cases (count)", "Успешные тесты (количество)"),
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
            "* Тест файловой системы без учёта регистра пропущен в Linux; выполнен на macOS.",
        ),
        18,
    )
    body += text(
        62,
        779,
        tr(
            lang,
            "Different suites cover different scopes. Bar length is not a quality or safety ranking.",
            "Наборы проверяют разные области. Длина столбца не означает качество или безопасность.",
        ),
        18,
    )
    body += text(
        40,
        857,
        tr(
            lang,
            "Source: validation-evidence.json → four linked GitHub Actions runs. No live polling.",
            "Источник: validation-evidence.json → четыре запуска GitHub Actions. Не live-мониторинг.",
        ),
        16,
        MUTED,
    )
    desc = tr(
        lang,
        "Passed tests: Entity Migrations 36 and one skip; Meter Contracts 75; Scenario Tests 54 including seven real-HA tests; Assist Scenario Lab 24. Counts do not rank quality.",
        "Успешные тесты: Entity Migrations 36 и один пропуск; Meter Contracts 75; Scenario Tests 54, включая семь с настоящим HA; Assist Scenario Lab 24. Числа не являются рейтингом качества.",
    )
    return svg(lang, 888, title, desc, body)


def role_transfer(lang="en"):
    title = tr(
        lang,
        "Role transfer: one event, two distinct outcomes",
        "Перенос роли: одно событие, два результата",
    )
    body = header(
        "HA HOMELAB / 04",
        title,
        tr(
            lang,
            "Bundled synthetic scenario · actual HA engine · in-memory device callbacks",
            "Комплектный учебный сценарий · настоящий HA · обработчики устройств в памяти",
        ),
    )
    for x, label in [
        (340, tr(lang, "INITIAL", "НАЧАЛО")),
        (700, tr(lang, "EVENT / ACTION", "СОБЫТИЕ / ДЕЙСТВИЕ")),
        (1080, tr(lang, "FINAL", "ИТОГ")),
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
        tr(lang, "Retired hardware", "Прежнее устройство"),
        16,
        22,
        COLORS[0],
        700,
    )
    body += text(
        62, 347, tr(lang, "No command sent", "Команда не отправлена"), 17, MUTED
    )
    body += lines(
        62,
        457,
        tr(lang, "Replacement role", "Новое устройство роли"),
        18,
        22,
        COLORS[2],
        700,
    )
    body += text(
        62, 520, tr(lang, "One turn_off call", "Один вызов turn_off"), 17, MUTED
    )
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
        tr(
            lang,
            "Logical sequence (not a measured time axis)",
            "Логическая последовательность (не измеренная шкала времени)",
        ),
        19,
        INK,
        600,
        "middle",
    )
    body += rect(40, 647, 548, 110, PALE[2])
    body += text(
        60, 679, tr(lang, "EXPECTED CALL", "ОЖИДАЕМЫЙ ВЫЗОВ"), 14, COLORS[2], 700
    )
    body += text(60, 711, "switch.turn_off → switch.scenario_table", 19, COLORS[2], 600)
    body += text(60, 739, tr(lang, "Final state: off", "Итоговое состояние: off"), 18)
    body += rect(612, 647, 548, 110, PALE[0])
    body += text(
        632, 679, tr(lang, "FORBIDDEN CALL", "ЗАПРЕЩЁННЫЙ ВЫЗОВ"), 14, COLORS[0], 700
    )
    body += text(
        632, 711, "turn_off → switch.scenario_retired_plug", 19, COLORS[0], 600
    )
    body += text(632, 739, tr(lang, "Final state: on", "Итоговое состояние: on"), 18)
    body += text(
        40,
        802,
        tr(
            lang,
            "Fixture requests 40 ms before the event and 100 ms to settle; these are not measured latency.",
            "Сценарий задаёт паузу 40 мс до события и 100 мс ожидания; это не измеренная задержка.",
        ),
        18,
    )
    body += text(
        40,
        838,
        tr(
            lang,
            "Source: role-transfer.scenario.json · physical relay / power delivery not tested by this chart.",
            "Источник: role-transfer.scenario.json · схема не подтверждает работу реле и подачу питания.",
        ),
        16,
        MUTED,
    )
    desc = tr(
        lang,
        "The old device stays on. One event turns the replacement off. Exactly one expected call, the old-device off call forbidden. Logical stages are not elapsed-time measurements.",
        "Прежнее устройство остаётся включённым. Событие выключает только новое. Ожидается один вызов; выключение прежнего запрещено. Логические этапы не являются измерениями времени.",
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
        for language in ("en", "ru"):
            suffix = ".ru" if language == "ru" else ""
            (ROOT / f"{name}{suffix}.svg").write_text(
                builder(language), encoding="utf-8"
            )


if __name__ == "__main__":
    render_all()
