"""Regression checks for original public documentation and synthetic assets."""

import hashlib
import importlib.util
import json
import re
import unittest
from collections import Counter
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parent
LANGUAGES = tuple(
    item["code"]
    for item in json.loads((ROOT.parent / "languages.json").read_text(encoding="utf-8"))
)


def localized(stem, language, extension="md"):
    suffix = "" if language == "en" else f".{language}"
    return f"{stem}{suffix}.{extension}"


def documentation_pages(language):
    return (
        ROOT.parent / "profile" / localized("README", language),
        ROOT / localized("README", language),
        ROOT / localized("process-and-results", language),
    )


def section_ids(body):
    explicit = set(re.findall(r'<a (?:id|name)="([^"]+)"', body))
    for heading in re.findall(r"^#{1,6}\s+(.+)$", body, re.MULTILINE):
        # GitHub keeps Unicode letters, spaces, hyphens and underscores in slugs.
        explicit.add(re.sub(r"[^\w\s-]", "", heading.lower()).replace(" ", "-"))
    return explicit


class PublicAssetsTests(unittest.TestCase):
    def test_language_set_matches_home_studio(self):
        # Home Studio planner/locales/index.js at the documented source commit.
        expected = {
            "en",
            "ar",
            "bn",
            "cs",
            "de",
            "es",
            "fa",
            "fr",
            "he",
            "hi",
            "id",
            "it",
            "ja",
            "ko",
            "nl",
            "pl",
            "pt",
            "ru",
            "th",
            "tr",
            "uk",
            "vi",
            "zh-Hans",
            "zh-Hant",
        }
        self.assertEqual(set(LANGUAGES), expected)

    def test_companion_matches_the_published_linux_evidence(self):
        expected = "bb8544517eeb4895b80b049cf9e242d04635e7785bd198c1d57a7cf3f5fc8ab4"
        actual = hashlib.sha256(
            (ROOT / "role-transfer.scenario.json").read_bytes()
        ).hexdigest()
        self.assertEqual(actual, expected)
        for language in LANGUAGES:
            self.assertIn(
                expected,
                (ROOT / localized("README", language)).read_text(encoding="utf-8"),
            )

    def test_svg_is_reproducible_and_passive(self):
        spec = importlib.util.spec_from_file_location(
            "render_architecture", ROOT / "render_architecture.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for name, builder in module.BUILDERS.items():
            for language in LANGUAGES:
                with self.subTest(name=name, language=language):
                    body = (ROOT / localized(name, language, "svg")).read_text(
                        encoding="utf-8"
                    )
                    self.assertEqual(body, builder(language))
                    svg = ElementTree.fromstring(body)
                    self.assertEqual(svg.attrib["lang"], language)
                    self.assertIsNotNone(svg.find("{http://www.w3.org/2000/svg}title"))
                    self.assertIsNotNone(svg.find("{http://www.w3.org/2000/svg}desc"))
                    for element in svg.iter():
                        self.assertNotIn(
                            element.tag.rsplit("}", 1)[-1],
                            {"script", "image", "foreignObject"},
                        )
                        self.assertFalse(
                            any(
                                key.startswith("on") or key.endswith("href")
                                for key in element.attrib
                            )
                        )

    def test_chart_evidence_has_linked_sources_and_separate_skips(self):
        evidence = json.loads((ROOT / "validation-evidence.json").read_text())
        self.assertEqual(evidence["unit"], "count")
        self.assertEqual(len(evidence["projects"]), 4)
        for project in evidence["projects"]:
            self.assertRegex(
                project["source"],
                r"^https://github\.com/ha-homelab/[a-z-]+/actions/runs/\d+$",
            )
            self.assertGreater(project["passed"], 0)
            self.assertGreaterEqual(project["skipped"], 0)
            self.assertLessEqual(project.get("runtime_cases", 0), project["passed"])
            for language in LANGUAGES:
                self.assertIn(
                    project["source"],
                    (ROOT / localized("README", language)).read_text(encoding="utf-8"),
                )

    def test_all_languages_have_valid_relative_links(self):
        for language in LANGUAGES:
            for stem in ("README", "process-and-results"):
                body = (ROOT / localized(stem, language)).read_text(encoding="utf-8")
                for link in re.findall(r"\]\(([^)]+)\)", body):
                    if "://" not in link and not link.startswith("#"):
                        self.assertTrue((ROOT / link.split("#")[0]).exists(), link)

    def test_translations_preserve_executable_examples(self):
        for stem in ("README", "process-and-results"):
            english = (ROOT / localized(stem, "en")).read_text(encoding="utf-8")

            # Existing localized examples may select a documented CLI language.
            def commands(text):
                blocks = re.findall(r"```[^\n]*\n(.*?)```", text, re.DOTALL)
                return [
                    re.sub(r" --lang (?:en|ru|de|es)\b", "", block) for block in blocks
                ]

            examples = commands(english)
            for language in LANGUAGES:
                body = (ROOT / localized(stem, language)).read_text(encoding="utf-8")
                self.assertEqual(
                    examples,
                    commands(body),
                    language,
                )

    def test_language_navigation_and_project_coverage(self):
        catalog = json.loads(
            (ROOT.parent / "assets/profile/catalog.json").read_text(encoding="utf-8")
        )
        for language in LANGUAGES:
            for directory, stem in (
                (ROOT, "README"),
                (ROOT, "process-and-results"),
                (ROOT.parent / "profile", "README"),
            ):
                body = (directory / localized(stem, language)).read_text(
                    encoding="utf-8"
                )
                for target in LANGUAGES:
                    self.assertIn(
                        localized(stem, target), body, (language, stem, target)
                    )
                if directory.name == "profile":
                    for project in catalog["projects"]:
                        self.assertIn(
                            project["html_url"], body, (language, project["name"])
                        )

    def test_navigation_is_generated_from_one_registry(self):
        spec = importlib.util.spec_from_file_location(
            "language_navigation", ROOT.parent / "render_language_navigation.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(len(set(LANGUAGES)), len(LANGUAGES))
        for path, directory, stem in module.pages():
            body = path.read_text(encoding="utf-8")
            self.assertEqual(body, module.update(body, directory, stem), path)

    def test_translations_preserve_sections_examples_and_sources(self):
        def structure(body):
            return (
                Counter(re.findall(r"^(#+)\s", body, re.MULTILINE)),
                re.findall(r"^(\d+)\. ", body, re.MULTILINE),
                Counter(re.findall(r"(?<!`)`([^`\n]+)`(?!`)", body)),
            )

        def sources(body):
            links = []
            for url in re.findall(r'https?://[^\s)"<>]+', body):
                if "/ha-homelab/.github/" in url:
                    if "/profile/README" in url:
                        continue  # The navigation has all languages.
                    url = url.split("#")[0]
                url = re.sub(r"\.[a-z]{2}(?:-Hans|-Hant)?\.(md|svg)", r".\1", url)
                links.append(url)
            return Counter(links)

        for language in LANGUAGES:
            for english, translated in zip(
                documentation_pages("en"), documentation_pages(language)
            ):
                baseline = english.read_text(encoding="utf-8")
                body = translated.read_text(encoding="utf-8")
                self.assertEqual(structure(baseline), structure(body), translated)
                self.assertEqual(sources(baseline), sources(body), translated)

    def test_internal_document_links_and_fragments_resolve(self):
        for language in LANGUAGES:
            for path in documentation_pages(language):
                body = path.read_text(encoding="utf-8")
                links = re.findall(r'\]\(([^)]+)\)|(?:href|src)="([^"]+)"', body)
                for markdown, html in links:
                    link = unquote(markdown or html)
                    prefixes = (
                        "https://github.com/ha-homelab/.github/blob/main/",
                        "https://raw.githubusercontent.com/ha-homelab/.github/main/",
                    )
                    base = path.parent
                    for prefix in prefixes:
                        if link.startswith(prefix):
                            link = link.removeprefix(prefix)
                            base = ROOT.parent
                            break
                    if "://" in link:
                        continue
                    filename, _, fragment = link.partition("#")
                    target = base / filename if filename else path
                    self.assertTrue(target.is_file(), (path, link))
                    if fragment and target.suffix == ".md":
                        self.assertIn(
                            fragment,
                            section_ids(target.read_text(encoding="utf-8")),
                            (path, link),
                        )

    def test_unicode_wrapping_preserves_letters_and_marks(self):
        spec = importlib.util.spec_from_file_location(
            "unicode_renderer", ROOT / "render_architecture.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for label in (
            "入力を確認してから結果を評価します",
            "マニフェスト、スナップショット、対応するソースファイル",
            "意図、動作、可聴応答のローカル記録",
            "ตรวจสอบหลักฐานก่อนติดตั้ง",
            "परीक्षण के परिणाम और प्रमाण",
            "পরীক্ষার ফলাফল ও প্রমাণ",
        ):
            lines = module.wrapped(label, 10)
            self.assertGreater(len(lines), 1)
            self.assertEqual("".join(label.split()), "".join("".join(lines).split()))
            for line in lines:
                self.assertFalse(module.unicodedata.category(line[0]).startswith("M"))
                self.assertNotIn(
                    line[0], "、。，．？！：；ーっゃゅょッャュョ）］｝」』】"
                )
                self.assertFalse(
                    module.unicodedata.name(line[-1], "").endswith("VIRAMA")
                )

    def test_locale_dictionaries_are_complete(self):
        english = json.loads((ROOT / "locales/en.json").read_text(encoding="utf-8"))
        profile = ROOT.parent / "assets/profile/locales"
        profile_english = json.loads((profile / "en.json").read_text(encoding="utf-8"))
        for language in LANGUAGES:
            translations = json.loads(
                (ROOT / "locales" / f"{language}.json").read_text(encoding="utf-8")
            )
            self.assertEqual(set(english), set(translations), language)
            self.assertTrue(
                all(
                    isinstance(value, str) and value.strip()
                    for value in translations.values()
                )
            )
            self.assertIn(
                "{date}",
                translations[
                    "{date} UTC evidence snapshot · test counts, not device performance"
                ],
            )
            labels = json.loads(
                (profile / f"{language}.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                set(profile_english["labels"]), set(labels["labels"]), language
            )
            self.assertEqual(len(labels["months"]), 12)
            self.assertEqual(len(labels["labels"]["groups"]), 5)
            self.assertEqual([len(row) for row in labels["labels"]["details"]], [2] * 5)

    def test_profile_svgs_match_their_locales(self):
        directory = ROOT.parent / "assets/profile"
        spec = importlib.util.spec_from_file_location(
            "profile_render", directory / "render.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for language in LANGUAGES:
            for name, builder in (
                ("ecosystem", module.ecosystem),
                ("portfolio", module.portfolio),
            ):
                body = (directory / localized(name, language, "svg")).read_text(
                    encoding="utf-8"
                )
                self.assertEqual(body, builder(language))
                svg = ElementTree.fromstring(body)
                self.assertEqual(svg.attrib["lang"], language)
                for element in svg.iter():
                    self.assertNotIn(
                        element.tag.rsplit("}", 1)[-1],
                        {"script", "image", "foreignObject"},
                    )

    def test_example_asserts_retired_hardware_is_not_targeted(self):
        scenario = json.loads((ROOT / "role-transfer.scenario.json").read_text())
        self.assertEqual(scenario["schema"], "ha-scenario/v1")
        self.assertEqual(
            scenario["expect"]["states"]["switch.scenario_retired_plug"], "on"
        )
        self.assertIn(
            {"action": "switch.turn_off", "entity_id": "switch.scenario_retired_plug"},
            scenario["expect"]["forbidden"],
        )
        self.assertEqual(
            scenario["expect"]["calls"],
            [{"action": "switch.turn_off", "entity_id": "switch.scenario_table"}],
        )


if __name__ == "__main__":
    unittest.main()
