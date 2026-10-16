# Profile visuals and sources

The English and Russian organization profiles describe the public project
catalog checked on **16 October 2026 (America/Los_Angeles)**. All source
repositories were verified public through the GitHub API. This is an editorial
snapshot, not a live status board or a claim that every project is deployed.

## Original diagrams

- `ecosystem.svg` and `ecosystem.ru.svg` group the projects by role. Lines express
  related areas of work; they are not mandatory connections, network topology or
  automatic integrations. The numbers are project counts in each group.
- `portfolio.svg` and `portfolio.ru.svg` chart those counts. There are 22 project
  repositories in five editorial categories, plus the `.github` profile repository.
  Every project is counted exactly once. These are not usage, maturity,
  performance, test-coverage or hardware-acceptance scores.
- `catalog.json` preserves the API source, collection time, categories and each
  public project's default-branch commit and README permalink.
- `related-projects.json` records the separately maintained public companion
  projects, their descriptions and audited README blob hashes. Blob hashes identify
  file contents; they are not commit SHAs. These projects are excluded from the chart.

Regenerate the four original, MIT-licensed SVGs with Python 3:

```sh
python3 assets/profile/render.py
```

The renderer uses only the standard library, makes no network requests and embeds
no scripts, external images, credentials or household data. SVGs include accessible
titles/descriptions and fixed background colors for GitHub light and dark themes.

When updating the snapshot, retrieve **all pages** of public GitHub repository
metadata, verify visibility, review current default-branch READMEs, assign one
category per project, and update the JSON and both profiles together. Update the
snapshot date in the chart labels, regenerate, check the count, preview both
languages, and verify links. Repository creation dates are not publication dates;
the profile deliberately does not chart publication growth from `created_at`.

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
