# MEMORY — ARGUS-OS3

## 2026-10-20 — Automated Ablation Loop (pattern: Kaneshiro 2022)
- **Analyzed:** Nikon application note 2311E + Kaneshiro et al. 2022 (Quant Plant Biol 3:e30, DOI 10.1017/qpb.2022.24) — fully automated detect→classify→mask→IR-laser→verify in-situ cell disruption (NIS-Elements GA+JOBS, inverted Ti2-E).
- **Decision:** OS3 laser ablation upgraded from semi-manual click-to-ablate to a **closed automated loop**: Cellpose classify → pre-ablation viability gate → keep-out masking (protect non-ablated/control/recipient cells) → galvo fs-800nm → in-loop verification (H2B fragmentation + Centrin1 loss) → per-cell QC log → fail-safe retry.
- **Corroborated:** Gokce 2014 PMID 25470130 (automated fs ablation in C. elegans); Kamei 2009 PMID 19079252 (IR-LEGO); Suzuki 2022 PMID 35596523; Tomoi 2024 PMID 39506095; Gallaud 2014 PMID 24687279 re-verified. All verified 2026-10-20.
- **Written:** `docs/AUTOMATED_ABLATION_LOOP.md` (design), `EVIDENCE.md` (created), `TODO.md` (tasks), `README.md` (link). Master analysis at index: `../docs/NIKON_AUTOMATED_LASER_SORTING_ANALYSIS_2026-10-20.md`.

## 2026-07-19 — Project Created

- **Decision:** ARGUS-OS3 separated from ARGUS-LP_OS as standalone project
- **Rationale:** v1.0 (observation), v2.0 (causality/Odf2 KO), v3.0 (ablation) — three separate grants, three separate projects
- **Naming:** ARGUS-OS3 = v3.0 platform version. Previously embedded in ARGUS-LP_OS as "v2.0". Renamed for clean integer versioning when OS2 was created.
- **Hardware:** Inherits glove-box + OF from v1.0. Adds: micromanipulator, fs laser, sCMOS, Mac M4 Pro, UV-C, multi-camera NV, storage.
- **Budget:** hardware $44,426 total (subtotal $38,631 + 15% contingency $5,795; corrected 2026-10-19 — was $40,600 with an inconsistent ≈5.1% contingency of 1,969). Full research-program budget: $477,000–557,000 (CONCEPT.md).
- **Grant target:** EIC Pathfinder WP2 (October 2026)
- **Key difference from v2.0:** OS2 uses genetic perturbation (Odf2 KO) for causality. OS3 uses physical intervention (laser ablation). Both answer "is it causal?" but with different tools.

## Relationship

```
ARGUS-LP_OS (v1.0) → observation → $24,053
ARGUS-OS2 (v2.0)   → causality   → +$3,000  (genetic — Odf2 KO)
ARGUS-OS3 (v3.0)   → ablation    → $44,426  (physical — laser, hardware)
```

## Micromanipulator Decision

- **Base:** FOSH Micro Manipulator v2.0 (GPLv3, 167 commits, 3-axis, 3D-printed)
- **Adaptation:** Custom mounting bracket for OpenFlexure v6.1.5 frame
- **Control:** RasPi 5 GPIO → TMC2209 stepper drivers
- **Microinjector:** Pneumatic, adjustable pressure 0-100 psi, vacuum hold
- **Capillary puller:** University core facility (assumed free). Fallback: pre-pulled capillaries ($5-10/ea, WPI)
