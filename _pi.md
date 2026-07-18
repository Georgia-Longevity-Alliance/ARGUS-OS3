# _pi.md — ARGUS-OS3

**Parent:** Marketing
**GitHub:** https://github.com/Georgia-Longevity-Alliance/ARGUS-LP (v3.0 branch)

> RULE: before any action, read MAP.md, MEMORY.md, CONCEPT.md.

## Summary
ARGUS-OS3 is an autonomous robotic platform for 24/7 centrosome-aware lineage tracking WITH femtosecond laser ablation capability. Based on OpenFlexure v6.1.5 inside a custom glove-box enclosure. Fully open (GPLv3/CC-BY-SA). Primary system: hTERT-NPCs. Adds to ARGUS-LP_OS v1.0: micromanipulator (FOSH-adapted, 3-axis), pneumatic microinjector, femtosecond laser NIR 800 nm, cooled sCMOS, Mac M4 Pro AI agent, multi-camera night vision, UV-C sterilisation.

> RULE: CONCEPT.md and all core files — ENGLISH only. Any non-English text → translate immediately.

## Relationship to ARGUS-LP_OS
- **ARGUS-LP_OS** — v1.0. First grant. Observation only. Glove-box, no laser, no micromanipulator. RPE1-hTERT.
- **ARGUS-OS3** — v3.0. Causality. Odf2 KO. Same hardware + reagents.
- **ARGUS-OS3** — v3.0. Third grant. Ablation + injection. Same glove-box + laser + micromanipulator. hTERT-NPCs.
- Shared hardware base: OpenFlexure v6.1.5, 60×/1.2 NA WI, glove-box, HEPA H13, night vision.
- OS3 adds: laser, micromanipulator, sCMOS, Mac M4 Pro, UV-C, internal storage.

## Directory Structure
- `hardware/` — laser integration, micromanipulator mount, sCMOS adapter, enclosure upgrades
- `software/` — AI agent, laser control, multi-camera NV, biosafety
- `firmware/` — laser shutter, UV-C controller, micromanipulator driver
- `docs/` — laser safety, ablation protocols
- `letters/` — EIC Pathfinder WP2 correspondence
- `grants/` — EIC Pathfinder WP2 grant
- `refs/` — ablation literature

## Rules
- All hardware — CC-BY-SA 4.0
- All code — GPLv3
- All data — CC0
- Do not duplicate v1.0 materials from ARGUS-LP_OS
- Laser safety documentation MANDATORY before any ablation experiment
- Minimum 2 commits/week (activity for grants)

## Current Status (v1.0 — initial)
- Platform: OpenFlexure v6.1.5 + glove-box + femtosecond laser + micromanipulator
- Budget: ~$40,600
- Primary experiment: hTERT-NPC progenitor map + whole-cell ablation
- Grant target: EIC Pathfinder WP2 (October 2026)
