# MEMORY — ARGUS-OS3

## 2026-07-19 — Project Created

- **Decision:** ARGUS-OS3 separated from ARGUS-LP_OS as standalone project
- **Rationale:** v1.0 (observation), v2.0 (causality/Odf2 KO), v3.0 (ablation) — three separate grants, three separate projects
- **Naming:** ARGUS-OS3 = v3.0 platform version. Previously embedded in ARGUS-LP_OS as "v2.0". Renamed for clean integer versioning when OS2 was created.
- **Hardware:** Inherits glove-box + OF from v1.0. Adds: micromanipulator, fs laser, sCMOS, Mac M4 Pro, UV-C, multi-camera NV, storage.
- **Budget:** $40,600 total ($24,053 base + $16,547 additions)
- **Grant target:** EIC Pathfinder WP2 (October 2026)
- **Key difference from v2.0:** OS2 uses genetic perturbation (Odf2 KO) for causality. OS3 uses physical intervention (laser ablation). Both answer "is it causal?" but with different tools.

## Relationship

```
ARGUS-LP_OS (v1.0) → observation → $24,053
ARGUS-OS2 (v2.0)   → causality   → +$3,000  (genetic — Odf2 KO)
ARGUS-OS3 (v3.0)   → ablation    → $40,600   (physical — laser)
```

## Micromanipulator Decision

- **Base:** FOSH Micro Manipulator v2.0 (GPLv3, 167 commits, 3-axis, 3D-printed)
- **Adaptation:** Custom mounting bracket for OpenFlexure v6.1.5 frame
- **Control:** RasPi 5 GPIO → TMC2209 stepper drivers
- **Microinjector:** Pneumatic, adjustable pressure 0-100 psi, vacuum hold
- **Capillary puller:** University core facility (assumed free). Fallback: pre-pulled capillaries ($5-10/ea, WPI)
