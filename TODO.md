# TODO — ARGUS-OS3

**Version:** 1.0
**Date:** 2026-07-19

## Pre-Build

- [ ] Source used femtosecond laser (Thorlabs/Coherent, eBay/LabX)
- [ ] Adapt FOSH micromanipulator STL to OpenFlexure frame
- [ ] Design micromanipulator mounting bracket (FreeCAD)
- [ ] Order NEMA 11 steppers + TMC2209 drivers
- [ ] Order pneumatic microinjector (WPI/Eppendorf)
- [ ] Order ZWO ASI183MM Pro
- [ ] Order Mac M4 Pro
- [ ] Design UV-C interlock circuit (glove sensors → relay)
- [ ] Order UV-C lamp + timer + IR beam break sensors
- [ ] Design internal shelving (FreeCAD → stainless fab)

## Pilot A — Sham Ablation

- [ ] RPE1-hTERT on CYTOO islands
- [ ] Laser at intercellular space, 20 pairs
- [ ] Track both sisters 72h
- [ ] Compare with untouched control
- [ ] Go/No-Go: no significant difference (Δ<10%)

## Pilot B — Ablation Calibration

- [ ] RPE1-hTERT, 20 pairs
- [ ] Ablation power sweep (10-50 mW)
- [ ] Death criteria: H2B-GFP fragmentation + morphological collapse
- [ ] Go/No-Go: ≥85% specific at ≤50 mW, ≤30 min

## Main — NPC Ablation

- [ ] hTERT-NPCs (ReNcell/Lonza), Centrin1-GFP + H2B-GFP
- [ ] Arm A: 50 pairs, ablate mature-mother cell
- [ ] Arm B: 50 pairs, ablate immature-daughter cell
- [ ] Sham: 20 pairs, laser at intercellular space
- [ ] Control: 20 pairs, untouched
- [ ] 72h tracking + endpoint differentiation markers

## Grants

- [ ] Submit EIC Pathfinder WP2 (October 2026)
- [ ] Laser safety protocol for IRB
- [ ] Designate laser safety officer

## Software

- [ ] Laser targeting GUI (click cell → galvo → ablate)
- [ ] Ablation verification (automated death detection)
- [ ] AI agent: Mixtral 8×7B local inference
- [ ] Multi-camera night vision stitching
- [ ] UV-C cycle automation + HEPA status monitoring
