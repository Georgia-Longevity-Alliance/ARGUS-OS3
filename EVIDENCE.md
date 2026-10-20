# EVIDENCE — ARGUS-OS3 (Laser Ablation Methodology)

**Created:** 2026-10-20
**Scope:** evidence for OS3 causality instrumentation — automated laser ablation, single-cell laser manipulation, and the in-situ cell-isolation paradigm. All PMIDs/DOIs verified via Europe PMC/OpenAlex 2026-10-20.
**Master analysis:** `docs/NIKON_AUTOMATED_LASER_SORTING_ANALYSIS_2026-10-20.md` (index-level); engineering note: `docs/AUTOMATED_ABLATION_LOOP.md`.

> **Knowledge credit:** primary papers are peer-reviewed (open access where noted). Vendor application notes are flagged as vendor claims.

## Automated laser ablation loop (the closed-loop pattern)

| PMID/DOI | Finding | Role in OS3 |
|:----:|---------|-------------|
| **10.1017/qpb.2022.24** | Kaneshiro et al. 2022 (Quant Plant Biol 3:e30, **open access CC BY**) — **fully automated detect→classify→mask→IR-laser→verify** loop for in-situ cell disruption (Nikon NIS-Elements GA/JOBS, inverted Ti2-E); target enrichment up to 8.3×; disruption success 78.9±9.8% (up to 87.2±13.4% at low density) | ⭐⭐ Primary pattern for the **automated ablation loop**: viability gate, keep-out masking, per-tile loop, in-loop verification, per-cell QC |
| **25470130** | Gokce et al. 2014 (PLoS ONE) — **fully automated microfluidic femtosecond-laser axotomy** in C. elegans, ~17 s/worm | ⭐⭐ Direct precedent of automated detect→laser in **C. elegans** (OS3's model organism) |

## Single-cell laser manipulation (IR-LEGO family)

| PMID | Finding | Role in OS3 |
|:----:|---------|-------------|
| **19079252** | Kamei et al. 2009 (Nat Methods) — **IR-LEGO**: 1480 nm laser heats cells (10⁵× water-heating vs 440 nm); targeted single-cell manipulation in living C. elegans with low photodamage | Foundation of laser single-cell precision in C. elegans |
| **35596523** | Suzuki et al. 2022 (Dev Growth Differ) — IR-LEGO single-cell gene induction in C. elegans (semaphorin–plexin mosaic) | IR laser is routine in C. elegans |
| **39506095** | Tomoi et al. 2024 (Commun Biol) — quantitative IR-LEGO calibration (power/duration → induction vs invasiveness) | Power/dose calibration methodology — mirrors OS3 pilot calibration |

## Cell-fate / ablation safety (causality rationale)

| PMID | Finding | Role in OS3 |
|:----:|---------|-------------|
| **24687279** | Gallaud et al. 2014 (J Cell Biol) — Ensconsin/Map7 & centrosome separation in Drosophila NB; ~30% of ablated cells may not divide (mitotic defects) | OS3 "Mitotic Defect Risk" — re-verified 2026-10-20 |
| **19079252** (Kamei) | IR-LEGO induces target-cell manipulation with **less photochemical damage than visible lasers** | Low-phototoxicity rationale for IR/fs approaches in OS3 |

## In-situ isolation preserves position (causality/lineage paradigm)

| Source | Finding | Role in OS3 |
|:----:|---------|-------------|
| Kaneshiro 2022 (Discussion) | "positional information before irradiation is completely maintained … facilitates continuous analysis, such as live imaging, for tracing individual cells" | Independent confirmation of the positional/lineage paradigm vs FACS/microfluidics — citable in grants |
| **42234731** | van den Brink et al. 2026 (Sci Adv) — image-based phenotypic sorting with real-time neural-network analysis (synthetic cells) | Automated image-analysis-driven selection — convergence with Cellpose+loop |

## Background (field maturity)

| PMID | Finding | Role in OS3 |
|:----:|---------|-------------|
| **41868091** | Liotta et al. 2025 (Nat Rev Methods Primers) — Laser capture microdissection (LCM) primer | Laser-based cell isolation is a mature field — OS3 method sits in a well-established lineage |

## Notes
- Kaneshiro 2022 is **stage K (proof-of-concept)**: N=5 samples main experiment, one plant species → pattern source, not a performance benchmark.
- The paper's weaknesses (whole-cell thermal ablation, ~79% disruption, ~8× enrichment, no deep learning, one-shot) are exactly where ARGUS OS3 is stronger (fs subcellular precision, Cellpose, multi-day tracking, open hardware) — see meta-analysis §4/§6 in the master document.
