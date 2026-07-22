# PARAMETERS — ARGUS-OS3

**Version:** 4.0
**Date:** 2026-07-19

## Platform Parameters

| Parameter | Value |
|-----------|-------|
| **Base platform** | ARGUS-LP_OS v1.0 (OpenFlexure v6.1.5, 60×/1.2 NA WI, glove-box, HEPA H13) |
| **Camera** | ZWO ASI183MM Pro cooled sCMOS (standard) |
| **Laser** | Femtosecond NIR 800 nm (Thorlabs/Coherent, used) |
| **Laser path** | Through objective (epi-illumination) or side port |
| **Targeting** | Galvo mirrors, click-to-ablate |
| **Ablation verification** | H2B-GFP nuclear fragmentation + Centrin1-GFP loss within 15-30 min |
| **Micromanipulator** | FOSH v2.0 adapted, 3-axis, NEMA 11 steppers, TMC2209 drivers |
| **Microinjector** | Pneumatic, 0-100 psi, vacuum hold |
| **Capillary** | Borosilicate 1.0 mm OD, pulled to 1-2 µm tip |
| **AI agent** | Mac M4 Pro, Mixtral 8×7B / Llama 3.3 70B, local |
| **Night vision** | 2× Camera NoIR + 4× IR LED 850 nm |
| **Sterilisation** | UV-C 254 nm, timer, interlock with glove sensors |

## Ablation Parameters

| Parameter | Value |
|-----------|-------|
| **Wavelength** | 800 nm (NIR, subcellular precision via multiphoton) |
| **Alternative** | CW 405 nm (whole-cell only, $2,000) |
| **Pulse duration** | ~100 fs |
| **Repetition rate** | 80 MHz |
| **Power at sample** | 10-50 mW (cell-type dependent, calibrated in pilot) |
| **Success rate target** | ≥85% specific ablation |
| **Wrong-cell kill** | <5% |
| **Bystander effect** | Assessed via sham (laser at intercellular space) |

## Cell Strategy

| Stage | System | Duration | Go/No-Go |
|:-----:|--------|:--------:|----------|
| Pilot A | RPE1, sham ablation, 20 pairs | 1 week | No bystander effect |
| Pilot B | RPE1, whole-cell ablation, 20 pairs | 2 weeks | ≥85% specific |
| Main | hTERT-NPCs, 100 pairs (50A+50B) | 4 weeks | — |

## Budget

| Line item | $ |
|-----------|--:|
| **Base platform (ARGUS-LP_OS v1.0)** | 24,053 |
| Micromanipulator module (FOSH + microinjector) | 1,208 |
| UV-C sterilisation | 500 |
| Femtosecond laser (used) | 8,000 |
| Laser safety | 500 |
| ZWO ASI183MM Pro sCMOS | 1,800 |
| Mac M4 Pro | 2,200 |
| Multi-camera night vision | 70 |
| Internal storage | 300 |
| **Subtotal** | **38,631** |
| **+15% contingency** | **1,969** |
| **TOTAL** | **$40,600** |
