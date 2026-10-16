# HA Homelab organization profile

This repository publishes the [HA Homelab GitHub profile](https://github.com/ha-homelab)
and its original visual identity.

- `profile/README.md` is the public organization profile.
- `profile/README.<language>.md` contains the other 23 full translations.
- `languages.json` lists the 24 documentation languages, matching Home Studio.
- `render_language_navigation.py` regenerates the shared language links.
- `assets/ha-homelab-logo.png` is the full-resolution square logo.
- `assets/README.md` records the design intent and generation prompts.
- `assets/profile/` contains the public-project snapshot, reproducible ecosystem
  diagrams and project-count charts, plus screenshot attribution and source notes.
- `community-tools/` explains the four offline community tools with diagrams,
  synthetic examples and dated software-test evidence.

Keep this repository limited to public branding and documentation. Household
configuration, infrastructure addresses, credentials, and operational exports
belong in the private organization repositories.

Repository settings are managed by
[`4alvit/terraform-github-ha-homelab`](https://github.com/4alvit/terraform-github-ha-homelab).
Changes go through pull requests; preview the image and rendered Markdown before merging.

## Community tools

[Illustrated integration guide and roadmap](community-tools/README.md). Four independently useful tools connect role migration, metering contracts, synthetic automation tests and voice evidence through explicit review steps.

<!-- language-navigation:start -->
<p dir="ltr">
<a href="community-tools/README.md" lang="en" dir="ltr">English</a> · <a href="community-tools/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="community-tools/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="community-tools/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="community-tools/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="community-tools/README.es.md" lang="es" dir="ltr">Español</a> · <a href="community-tools/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="community-tools/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="community-tools/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="community-tools/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="community-tools/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="community-tools/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="community-tools/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="community-tools/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="community-tools/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="community-tools/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="community-tools/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="community-tools/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="community-tools/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="community-tools/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="community-tools/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="community-tools/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="community-tools/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="community-tools/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

The organization profile, community overview, process-and-results guide and six
diagrams are available in all 24 languages. Documentation translations do not
change the CLI or speech languages supported by individual projects.

Regenerate navigation and diagrams, then check the complete language set:

```sh
python3 render_language_navigation.py
python3 assets/profile/render.py
python3 community-tools/render_architecture.py
python3 -m unittest discover -s community-tools -p 'test_*.py'
```

## License

[MIT](LICENSE). The logo is an original independent identity, not the official
Home Assistant logo.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) for local checks and review expectations,
and [SECURITY.md](SECURITY.md) for private vulnerability reporting. This is a
community/profile repository; its CI does not claim an application certification.
