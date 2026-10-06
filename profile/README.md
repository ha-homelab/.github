<p align="center">
  <img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab: a turquoise house with connected network nodes" width="192" />
</p>

<h1 align="center">HA Homelab</h1>
<p align="center">A thoughtful home. Understandable automation.</p>

Public Home Assistant integrations, device conversion guides and recovery tools.
Each project documents its tested hardware, limitations and verification steps.

## Integrations and dashboards

- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — unofficial DESLOC cloud
  integration for lock state, controls, battery and Wi-Fi signal. Check its
  [model compatibility notes](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md)
  before relying on a particular feature.
- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — a separate
  Home Assistant dashboard card for that integration, with confirmed unlock controls.

## Reuse and recover devices

- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — convert an Echo
  Dot 2 into an EchoLocal Home Assistant voice satellite; includes an ordered
  runbook and wake-word training/evaluation tools.
- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — convert an
  Echo Show 5 Gen2 into an Android display and voice client. Read the hardware,
  backup and attended-operation requirements before starting.
- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — backup,
  upgrade and legacy Ethernet recovery for the original SMLIGHT SLZB-06.
  Core firmware and Zigbee radio firmware are separate targets.

These repositories publish reusable source and instructions. They do not include
household configuration, credentials, device backups or training recordings.
Tests and case studies are scoped evidence, not certification of every device variant.

## Related public projects

Energy reports for an unmodified Echo or Google/Nest device are separate adapters:
[Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) and
[Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats).
Their voice/account setup differs from converting hardware into a Home Assistant client.

Our public [GitHub infrastructure](https://github.com/4alvit/terraform-github-ha-homelab)
is managed with Terraform. This profile repository holds our
[original logo and design notes](https://github.com/ha-homelab/.github/blob/main/assets/README.md).

---

An independent homelab built with [Home Assistant](https://www.home-assistant.io/).
Not affiliated with the Home Assistant project or device manufacturers.
