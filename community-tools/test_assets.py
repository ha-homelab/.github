"""Regression checks for original public documentation and synthetic assets."""

import importlib.util
import json
from pathlib import Path
import re
import unittest
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parent


class PublicAssetsTests(unittest.TestCase):
    def test_svg_is_reproducible_and_passive(self):
        spec = importlib.util.spec_from_file_location(
            "render_architecture", ROOT / "render_architecture.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        body = (ROOT / "architecture.svg").read_text()
        self.assertEqual(body, module.build())
        svg = ElementTree.fromstring(body)
        self.assertIsNotNone(svg.find("{http://www.w3.org/2000/svg}title"))
        self.assertIsNotNone(svg.find("{http://www.w3.org/2000/svg}desc"))
        for element in svg.iter():
            self.assertNotIn(
                element.tag.rsplit("}", 1)[-1], {"script", "image", "foreignObject"}
            )
            self.assertFalse(
                any(
                    key.startswith("on") or key.endswith("href")
                    for key in element.attrib
                )
            )

    def test_both_languages_have_valid_relative_links(self):
        for language in ("README.md", "README.ru.md"):
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
