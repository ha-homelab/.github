"""Regression checks for original public documentation and synthetic assets."""

import hashlib
import importlib.util
import json
import re
import unittest
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parent


class PublicAssetsTests(unittest.TestCase):
    def test_companion_matches_the_published_linux_evidence(self):
        expected = "bb8544517eeb4895b80b049cf9e242d04635e7785bd198c1d57a7cf3f5fc8ab4"
        actual = hashlib.sha256(
            (ROOT / "role-transfer.scenario.json").read_bytes()
        ).hexdigest()
        self.assertEqual(actual, expected)
        for language in ("README.md", "README.ru.md"):
            self.assertIn(expected, (ROOT / language).read_text())

    def test_svg_is_reproducible_and_passive(self):
        spec = importlib.util.spec_from_file_location(
            "render_architecture", ROOT / "render_architecture.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for name, builder in module.BUILDERS.items():
            for language in ("en", "ru"):
                with self.subTest(name=name, language=language):
                    suffix = ".ru" if language == "ru" else ""
                    body = (ROOT / f"{name}{suffix}.svg").read_text()
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
            for document in ("README.md", "README.ru.md"):
                self.assertIn(project["source"], (ROOT / document).read_text())

    def test_both_languages_have_valid_relative_links(self):
        for language in (
            "README.md",
            "README.ru.md",
            "process-and-results.md",
            "process-and-results.ru.md",
        ):
            body = (ROOT / language).read_text()
            for link in re.findall(r"\]\(([^)]+)\)", body):
                if "://" not in link and not link.startswith("#"):
                    self.assertTrue((ROOT / link.split("#")[0]).exists(), link)

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
