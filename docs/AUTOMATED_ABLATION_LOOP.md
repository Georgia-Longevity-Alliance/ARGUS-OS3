# ARGUS-OS3 — Automated Ablation Loop (design note)

**Date:** 2026-10-20
**Source pattern:** Kaneshiro et al. 2022 (Quant Plant Biol 3:e30, DOI 10.1017/qpb.2022.24) — automated IR-laser in-situ cell disruption (Nikon NIS-Elements GA/JOBS); corroborated by Gokce et al. 2014 (PMID 25470130) — fully automated fs-laser axotomy in C. elegans.
**Master analysis:** `../../docs/NIKON_AUTOMATED_LASER_SORTING_ANALYSIS_2026-10-20.md`

> **Knowledge credit:** all performance values below are from the cited papers (PMID/DOI-verified 2026-10-20); design choices are ARGUS's own.

---

## Problem

OS3 currently ablates with a galvo mirror ("**click-to-ablate**") — a human clicks each target cell on screen. This is (a) slow, (b) not scalable to N=50–100 ablations, (c) subject to operator drift, (d) produces no continuous per-cell QC, (e) risks bystander hits near the target. The Kaneshiro 2022 system demonstrates the exact pattern to close this loop automatically.

## Goal

Turn OS3 laser ablation into a **fully automated closed loop**, per tile, per cell, with continuous QC:

```
┌─────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│ 1. Acquire  │ →  │ 2. Segment/Classify│ →  │ 3. Pre-ablation     │
│ (sCMOS tile)│    │ Cellpose + markers │    │ viability gate      │
└─────────────┘    └──────────────────┘    └─────────────────────┘
      ▲                    │                        │
      │                    ▼                        ▼
┌─────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│ 6. Verify   │ ←  │ 5. Irradiate     │ ←  │ 4. Keep-out masking  │
│ (H2B frag + │    │ galvo, fs 800nm  │    │ (protect target/     │
│  Centrin1)  │    │ dose-calibrated  │    │  control cells)      │
└─────────────┘    └──────────────────┘    └─────────────────────┘
      │
      ▼
 7. QC log (per-cell success rate, Flight Recorder)
```

## Loop stages (mapped from Kaneshiro's 5-step JOBS loop)

| # | Stage | Kaneshiro analog | ARGUS-OS3 implementation |
|:-:|-------|------------------|---------------------------|
| 1 | **Acquire** | Tiled acquisition (80–120 tiles, >20 mm²) | sCMOS tiled acquisition (ZWO ASI183MM Pro); multi-position over embryo/cell dish |
| 2 | **Segment & classify** | GA binarization; FDA+ threshold >9,600; tdTomato+ >65,535; size >12 µm | **Cellpose/StarDist** (stronger than thresholding): nuclei (H2B), centrioles (Centrin1/SAS-4), cell bodies |
| 3 | **Pre-ablation viability gate** | FDA viability gate (77% viable in pollen) | Skip cells failing health markers (H2B intact, centriole present, no blebbing) → save laser time, clean data |
| 4 | **Keep-out masking** | 60 µm mask (≈3× cell radius) around each target | Mask = per-cell protective zone around (a) the cell whose centriole is NOT ablated (sister-pair control), (b) the recipient cell in System B transplantation. Radius configurable per cell type. |
| 5 | **Irradiate** | 145 mW focal / 10 ms IR (thermal, whole-cell) | **fs 800 nm multiphoton (10–50 mW, ~100 fs, 80 MHz)** → subcellular single-centriole ablation. Dose per-cell-type calibrated in pilot (already in PARAMETERS.md) |
| 6 | **Verify** | Post-irradiation tiled re-acquisition (FDA loss + shrinkage) | In-loop verification: **H2B-GFP nuclear fragmentation + Centrin1-GFP loss within 15–30 min** (already ARGUS's marker) — now automated into the loop with objective pass/fail |
| 7 | **QC log** | Per-tile disruption-success statistics (Table 2) | Per-cell success rate + wrong-cell-kill rate → Flight Recorder + continuous stats |

## Design decisions

1. **Viability gate BEFORE ablation** (new): prevents firing at already-dead cells — directly cuts false-negative verification and wasted laser time. Cheap (a classification flag), high value.
2. **Masking is explicit, not implicit** (new): OS3 relied on aiming precision; now add a keep-out zone. Directly targets OS3's "<5% wrong-cell kill" requirement.
3. **Loop reuse primitive** (V9-BRAIN): implement `acquire→analyze→act→verify` as a reusable V9 workflow primitive (JOBS-like), so the same loop runs ablation (OS3), isolation (OS4), and routine acquisition (OS1).
4. **Fail-safe:** if verification fails for a cell (no fragmentation, no Centrin1 loss), mark and **retry once** with +10% dose (cap at phototoxicity ceiling per Body Law), else log as failed — never exceed the ceiling.

## Acceptance criteria (pilot)

- [ ] Pilot A (RPE1, sham): no bystander effect — 100% of cells outside keep-out mask survive 3 h (matches OS3 Pilot A).
- [ ] Pilot B (RPE1, whole-cell): ≥85% specific ablation, wrong-cell kill <5% (matches OS3 Pilot B).
- [ ] Main (hTERT-NPCs): ≥85% specific single-centriole ablation with in-loop verification.
- [ ] Automation latency: detect→verify < 2 s/cell; ablation throughput ≥ 20 cells/hour unattended.
- [ ] Flight Recorder: per-cell log (position, dose, verify result, retries) complete for 100% of cells.

## References (PMID/DOI-verified 2026-10-20)
- Kaneshiro et al. 2022 — DOI 10.1017/qpb.2022.24 (primary pattern)
- Gokce et al. 2014 — PMID 25470130 (automated fs ablation in C. elegans, ~17 s/worm)
- Kamei et al. 2009 — PMID 19079252 (IR-LEGO foundation)
- Gallaud et al. 2014 — PMID 24687279 (mitotic-defect risk; already in OS3)
