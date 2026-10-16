# Profile visuals and sources

The localized organization profiles describe the public project
catalog checked on **16 October 2026 (America/Los_Angeles)**. All source
repositories were verified public through the GitHub API. This is an editorial
snapshot, not a live status board or a claim that every project is deployed.

## Original diagrams

- `ecosystem.svg` and its localized variants group the projects by role. Lines express
  related areas of work; they are not mandatory connections, network topology or
  automatic integrations. The numbers are project counts in each group.
- `portfolio.svg` and its localized variants chart those counts. There are 22 project
  repositories in five editorial categories, plus the `.github` profile repository.
  Every project is counted exactly once. These are not usage, maturity,
  performance, test-coverage or hardware-acceptance scores.
- `catalog.json` preserves the API source, collection time, categories and each
  public project's default-branch commit and README permalink.
- `related-projects.json` records the separately maintained public companion
  projects, their descriptions and audited README blob hashes. Blob hashes identify
  file contents; they are not commit SHAs. These projects are excluded from the chart.

Regenerate the two original, MIT-licensed SVGs per supported language with Python 3:

```sh
python3 assets/profile/render.py
```

The renderer uses only the standard library, makes no network requests and embeds
no scripts, external images, credentials or household data. SVGs include accessible
titles/descriptions and fixed background colors for GitHub light and dark themes.

When updating the snapshot, retrieve **all pages** of public GitHub repository
metadata, verify visibility, review current default-branch READMEs, assign one
category per project, and update the JSON and all localized profiles together. Update the
snapshot date in the catalog (chart labels are derived from it), regenerate,
check the count, preview every language, and verify links. Repository creation dates are not publication dates;
the profile deliberately does not chart publication growth from `created_at`.

## Language coverage

The shared [language registry](../../languages.json) covers the same 24 languages as
[Home Studio's editor registry](https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/locales/index.js):
English, Arabic, Bengali, Czech, German, Spanish, Persian, French, Hebrew, Hindi,
Indonesian, Italian, Japanese, Korean, Dutch, Polish, Portuguese, Russian, Thai,
Turkish, Ukrainian, Vietnamese, Simplified Chinese and Traditional Chinese.
Each has a complete organization profile, community project overview,
process-and-results guide and six localized diagrams/charts. The screenshots
remain faithful to the original captured interface.

Both renderers load reviewed UTF-8 dictionaries from their `locales/` directories.
The profile dictionaries also provide month names for snapshot captions.
Adding a language requires its complete pages and dictionaries, generation and
visual review of its six SVGs, and the existing documentation tests. Missing
translation keys fail generation instead of silently displaying English.

Run `python3 render_language_navigation.py` from the repository root to refresh
the marked navigation blocks in all pages. Keep language names in their native
script. Arabic, Persian and Hebrew pages use right-to-left text, with executable
examples kept left-to-right. Stable section anchors preserve cross-language links.
The SVG renderer shapes RTL labels and wraps CJK, Thai and combining characters
without relying on spaces alone. Review every translation after changing shared
facts, source links or examples; the checks detect missing pages, dictionaries,
navigation links, examples and source references, but do not judge prose quality.

Translations describe the same software; they do not add a CLI language, speech
model, wake word or device feature. Follow the individual project's support notes.

## Actual editor screenshots

Both embedded screenshots are existing Home Studio editor captures, using
**fictional example plans**. They are not photos of a household or generated
mockups. They are embedded from a pinned source commit, not copied or modified:

- [Garage, creative studio and patio](https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg)
  — 1440 × 1000 pixels.
- [Furniture palettes and surface patterns](https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg)
  — 1440 × 1000 pixels.

Copyright 2026 Home Studio contributors. Used under the
[source MIT license](https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/LICENSE).
See the source [drawing guide](https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html).

The linked DESLOC project contains a historical UI gallery. Its older two-button
screenshots are not embedded here because the current card uses one adaptive button.
The linked RuView replay image is a synthetic visualization, not a screenshot
of a real occupancy measurement. EchoMuse timing charts in its own documentation
retain their original test scope; no microphone-to-speaker latency or aggregate
performance claim is derived from them here.

## Existing identity and software evidence

The original logo remains unchanged; see [design and provenance](../README.md).
The separately linked [community-tool guide](../../community-tools/README.md)
maintains its own dated CI evidence and chart sources. Passing software tests
does not replace physical device acceptance.
