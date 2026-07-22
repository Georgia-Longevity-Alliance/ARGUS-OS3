# CONCEPT — ARGUS-OS3
**Version:** 3.0
**Date:** 2026-07-22
**Idea:** Jaba Tqemaladze — Centriole transplantation as causality test

---

## 0. What is ARGUS-OS3

ARGUS-OS3 tests **CAUSALITY**. OS1 measured correlation. OS2 tested predictive power. OS3 asks: **does changing the centriole CHANGE the cell's fate?**

**Method:** Transplant a centriole with known pedigree from one cell into another. If the recipient cell's fate follows the transplanted centriole → causality proven. If not → centriole is a marker, not a carrier.

---

## 1. Why OS3 is Necessary

| Project | Question | Answer type |
|---------|----------|:---:|
| OS1 | Does pedigree correlate with fate? | Correlation |
| OS2 | Does pedigree predict fate better than position? | Prediction |
| **OS3** | **Does changing the centriole change the fate?** | **Causality** |

Without OS3, even perfect results from OS1+OS2 leave open: "Is the centriole a CAUSE or just a MARKER?"

---

## 1b. De Novo Centriole Synthesis Risk
Khodjakov et al. (2002, PMID 12356862) showed cells CAN assemble new centrioles de novo after ablation — but presence of ONE centriole suppresses this pathway. Our single-centrosome ablation leaves one centriole → suppresses de novo synthesis. Control: CDK inhibitor to block S-phase if needed.

## 2. Two Systems for Causality Testing

### System A: Drosophila Neuroblasts (Primary)
**Why:** Centrioles are NOT eliminated. Asymmetric inheritance is PROVEN (Januschke 2011 — mother→differentiate (GMC), daughter→stem (NB). Januschke 2011: mother centrosome inherited by differentiating daughter.; Conduit & Raff 2010 — Cnn asymmetry). Laser ablation of one centrosome changes fate. **This is the gold standard causality system.**

| Step | Method |
|:---:|--------|
| 1 | Drosophila NB with Centrin-GFP + Cnn-mCherry |
| 2 | Laser-ablate one centrosome at prophase |
| 3 | Track daughter cells: does the cell WITHOUT centrosome differentiate differently? |
| 4 | Control: unablated NB from same brain |

**N:** 50 NB ablations + 50 controls | **Duration:** 12 weeks | **Budget:** $60,000

### System B: Centriole Transplantation (Definitive)
**Why:** The ultimate test. Take a centriole from a "bad fate" cell, transplant into a "good fate" cell. If fate follows the centriole → definitive proof.

| Step | Method |
|:---:|--------|
| 1 | RPE1 cells with photoconvertible Centrin (Dendra2-Centrin1) |
| 2 | Photoconvert ONE centriole — track its pedigree through 3 divisions |
| 3 | Microsurgically extract the centriole (microneedle + piezo) |
| 4 | Transplant into recipient RPE1 cell at G1 |
| 5 | Track recipient fate (cilium formation, proliferation, EMT markers) |

**N:** 30 successful transplantations | **Duration:** 24 weeks | **Budget:** $150,000

---

## 3. Budget

| Component | System A (Drosophila NB) | System B (Transplantation) | Total |
|-----------|:---:|:---:|:---:|
| Personnel (PI 50% + postdoc) | $40,000 | $80,000 | $120,000 |
| Drosophila facility + reagents | $10,000 | — | $10,000 |
| Laser ablation setup (405nm pulsed) | $20,000 | — | $20,000 |
| Micromanipulator + piezo + optics | — | $50,000 | $50,000 |
| Cell culture + transfection | — | $15,000 | $15,000 |
| Microscopy time | $8,000 | $15,000 | $23,000 |
| Contingency (15%) | $12,000 | $24,000 | $36,000 |
| **Subtotal** | **$90,000** | **$184,000** | **$274,000** |

---

## 4. Key References

| # | Reference | PMID |
|---|-----------|------|
| 1 | Januschke et al. (2011) — Drosophila NB daughter→stem | 21407209 |
| 2 | Conduit & Raff (2010) — Cnn dynamics, Curr Biol | 21145745 |
| 3 | Yamashita et al. (2007) — mGSC mother→stem | 17255513 |
| 4 | Barandun et al. (2025) — CD8+ T-cell ninein, Cell Rep | 39764850 |
| 5 | Anderson & Stearns (2009) — centriole age → cilium | 19682908 |
| 6 | Kalbfuss & Gönczy (2023) — 88% elimination | 37256957 |
| 8 | **Thomas & Giet (2022)** — live imaging Drosophila NB with photo-ablated centrosomes, STAR Protoc | 35776653 |
| 9 | **Khodjakov et al. (2002)** — de novo centrosome formation after ablation, J Cell Biol | 12356862 |
| 7 | Rebollo et al. (2007) — unequal centrosomes Drosophila | 17336911 |

---

## 4b. Operational Fate Definition
**System A (Drosophila NB):** stemness = Deadpan (Dpn)+, Asense (Ase)-, EdU+ (proliferation). Differentiation = Pros+, Elav+, EdU-.
**System B (RPE1):** cilium-forming = Arl13B+ AND Ki67- AND EdU- (>24h G0). Proliferative = Ki67+ OR EdU+. EMT = E-cadherin loss + vimentin gain.

## 4c. Alternative Hypothesis: Necessary but Not Sufficient
Centriole may be NECESSARY (without it, fate changes) but NOT SUFFICIENT (transplant alone does not change fate). If ablation changes fate but transplantation does NOT → centriole is permissive, not instructive. This outcome is scientifically important and publishable.

## 4d. Milestones
| Month | System A | System B |
|:---:|------|------|
| 1-2 | Line establishment + ablation calibration | Dendra2-Centrin1 line generation |
| 3-4 | Pilot: 10 ablations + optimize | Pilot: centriole extraction protocol |
| 5-6 | Main: 50 ablations | Pilot: first 5 transplantations |
| 7-8 | Analysis + write-up | Analysis + protocol refinement |

## 5. Success Criteria

| Result | Verdict |
|--------|---------|
| Ablated NB: fate changes vs control | 🔴 Causality supported in Drosophila |
| Transplanted centriole: recipient fate follows donor pedigree | 🔴 **DEFINITIVE PROOF** — centriole carries fate information |
| Both negative | Centriole is a marker, not a carrier — publish as important negative result |

---

*Version 3.0 — Causality. From correlation to causation. Jaba Tqemaladze, 2026-07-22.*
