# CONCEPT — ARGUS-OS3

**Version:** 1.0
**Date:** 2026-07-19

---

## 0. What ARGUS-OS3 Is

ARGUS-OS3 is the **ablation-capable evolution** of the ARGUS-LP_OS platform. Where v1.0 observes, OS2 **intervenes** — it can separate sister cells, inject factors, and ablate specific cells with a femtosecond laser. The question graduates from "does centrosome age correlate with fate?" to "**is centrosome age causal for fate?**"

Builds on ARGUS-LP_OS v1.0 hardware (OpenFlexure v6.1.5, 60×/1.2 NA WI, glove-box, HEPA H13, night vision). Adds: micromanipulator, microinjector, femtosecond laser, sCMOS, AI agent.

---

## 1. Central Hypothesis

> **The mature mother centrosome is not merely a correlation — it is a causal determinant of daughter cell fate. Ablating the cell that inherits the mature mother centrosome produces a different outcome than ablating the cell that inherits the immature daughter centrosome.**

ARGUS-LP_OS v1.0 answers: "Is there a correlation?" (Phase 1 — observation).
ARGUS-OS3 answers: "Is it causal?" (Phase 3 — ablation).

---

## 2. Three Intervention Modes

| Mode | Tool | Purpose |
|:----:|------|---------|
| **Sister separation** | Micromanipulator (FOSH-adapted, 3-axis) + glass capillary 1-2 µm | Physically separate sister cells after mitosis. Alternative to CYTOO islands when single-cell manipulation is required. |
| **Microinjection** | Pneumatic microinjector | Inject apoptosis factors (cytochrome c, staurosporine), dyes (Lucifer Yellow, propidium iodide), siRNA (Cenexin/Odf2 knockdown) into specific cells identified by centrosome inheritance. |
| **Laser ablation** | Femtosecond laser NIR 800 nm | Whole-cell ablation of the daughter cell that inherited the mature mother centrosome (Arm A) vs. the daughter that inherited the immature centrosome (Arm B). Compare surviving sister fates. |

---

## 3. Experiment: Ablation Arms

### 3.1. Design

| Arm | Action | Track |
|:---:|--------|-------|
| **A** | Ablate cell inheriting MATURE mother centrosome | Surviving sister (immature centrosome) — fate |
| **B** | Ablate cell inheriting IMMATURE daughter centrosome | Surviving sister (mature centrosome) — fate |
| **Sham** | Laser at intercellular space (same energy, no cell hit) | Both sisters tracked |
| **Control** | No manipulation | Natural sister comparison |

### 3.2. Primary Outcome

> **H₀:** Fate of surviving sister is identical in Arm A and Arm B (centrosome identity of dead cell does not matter).
> **H₁:** Fate differs — centrosome identity IS causal.

### 3.3. Ablation Verification

- **Death criteria:** H2B-GFP nuclear fragmentation + loss of Centrin1-GFP signal + morphological collapse within 15-30 min.
- **Success rate target:** ≥85% specific ablation (wrong-cell kill <5%).
- **Sham control:** Laser at intercellular space. If sham significantly differs from control → laser-induced bystander effect, protocol adjustment required.

---

## 4. Optical Design

| Parameter | ARGUS-LP_OS v1.0 | ARGUS-OS3 |
|-----------|:---------------:|:---------:|
| Objective | 60×/1.2 NA WI | 60×/1.2 NA WI |
| Excitation | LED 488 nm | LED 488 nm |
| Camera | Camera HQ → sCMOS fallback | ZWO ASI183MM Pro (standard) |
| Laser | ❌ | ✅ fs NIR 800 nm |
| Laser path | — | Through objective (epi-illumination) or side port |
| Targeting | — | Click cell → galvo mirrors → ablate |
| Night vision | 1× Camera NoIR | 2× Camera NoIR (full box coverage) |

---

## 5. Micromanipulator

Based on **FOSH Micro Manipulator v3.0** (GPLv3, 3D-printed, 3-axis stepper).

| Parameter | Value |
|-----------|-------|
| Axes | X, Y, Z — independent stepper control |
| Resolution | ~1 µm per step (microstepping) |
| End effector | Glass capillary 1-2 µm tip (borosilicate, pulled) |
| Mount | 3D-printed bracket, OF v6.1.5 frame compatible |
| Control | RasPi 5 GPIO → stepper drivers (TMC2209) |
| Microinjector | Pneumatic, adjustable pressure (0-100 psi), vacuum hold |

---

## 6. Cell Strategy

| Stage | System | Duration | Go/No-Go |
|:-----:|--------|:--------:|----------|
| **Pilot A** | RPE1-hTERT, sham ablation, 20 pairs | 1 week | Laser does not affect un-targeted cells |
| **Pilot B** | RPE1-hTERT, whole-cell ablation, 20 pairs | 2 weeks | ≥85% specific ablation |
| **Main** | hTERT-NPCs, 100 pairs (50 Arm A, 50 Arm B) | 4 weeks | — |
| **Endpoint** | Fix + Cenexin + differentiation markers (Nestin → Tuj1/GFAP) | — | — |

---

## 7. AI Agent (v3.0)

| Component | Job |
|-----------|-----|
| **Mac M4 Pro** | Local LLM inference (Mixtral 8×7B / Llama 3.3 70B) |
| **Decision loop** | Observe → classify centrosome identity → decide: ablate or flag for human |
| **Post-hoc analysis** | Natural language experiment log, automated figure generation |
| **Self-learning** | LoRA fine-tuning on experiment outcomes, RAG over protocol docs |

**All models local. No API keys. No cloud.**

---

## 8. Budget

| Line item | $ |
|-----------|--:|
| **Base platform (ARGUS-LP_OS v1.0)** | 24,053 |
| Micromanipulator module (FOSH-adapted + microinjector) | 1,208 |
| UV-C sterilisation (254 nm lamp + interlock + timer) | 500 |
| Femtosecond laser NIR 800 nm (used, Thorlabs/Coherent) | 8,000 |
| Laser safety (OD6+ goggles, interlock, beam dump, signage) | 500 |
| ZWO ASI183MM Pro cooled sCMOS (standard) | 1,800 |
| Mac M4 Pro (AI agent) | 2,200 |
| 2× RasPi Camera NoIR + 3× IR LED 850 nm (multi-camera NV) | 70 |
| Internal shelving, drawers, wall rack | 300 |
| **Subtotal** | **38,631** |
| **+15% contingency** | **1,969** |
| **TOTAL (max)** | **$40,600** |

> **CW 405 nm alternative:** For whole-cell ablation only, a CW 405 nm diode laser (~$2,000) reduces budget to ~$34,000.

---

## 9. Results Publication Strategy

| Outcome | Action |
|---------|--------|
| **p<0.05, Arm A ≠ Arm B** | First causal demonstration of centrosome age → fate. High-impact paper. |
| **p≥0.05, no difference** | Honest null result. "Centrosome maturation state is not causal for fate in NPCs." Valuable negative data. |
| **Platform failure** | Technical report on OpenFlexure + laser integration. |

**We publish regardless.**

---

## 10. Grant Target

**EIC Pathfinder Challenges 2026 — WP2** (October 2026). ARGUS-OS3 as the ablation module of the CEDAR platform.

---

## 11. References

Key ablation & microinjection references (to be expanded):
1. Morsch M et al. *Sci Rep* 7:40967 (2017). **PMID: 28190072.** — 405 nm single-cell killing in Drosophila.
2. Loncarek J et al. *Nat Cell Biol* 10:322–328 (2008). **PMID: 18297061.** — Laser ablation of centrioles.
3. Sulston JE, White JG. *Dev Biol* 78:577–597 (1980). — Original C. elegans lineage by micropipette ablation.
4. Cordero-Maldonado ML et al. *PLoS One* 14:e0202377 (2019). **PMID: 30615627.** — Automated microinjection with deep learning.

See also: ARGUS-LP_OS CONCEPT.md for full centrosome biology references (23 PMIDs).

---

*Version 1.0 — 2026-07-19. Initial concept. Ablation arms, micromanipulator integration, AI agent, budget $40,600.*
