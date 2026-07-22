# CONCEPT — ARGUS-OS3
**Version:** 4.0
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
## 1d. Mitotic Defect Risk (Gallaud 2014)
Centrosome ablation causes mitotic spindle defects → cell death or cycle arrest. >30% of ablated cells may not divide (Gallaud 2014, PMID 24687279). Survivor bias: analyzed cells are those that survived ablation — may not represent normal fate. Mitigation: report division success rate; compare survivors vs non-survivors.

Khodjakov et al. (2002, PMID 12356862) showed cells CAN assemble new centrioles de novo after ablation — but presence of ONE centriole suppresses this pathway. Our single-centrosome ablation leaves one centriole → suppresses de novo synthesis. Control: CDK inhibitor to block S-phase if needed.

## 1c. Necessity vs Sufficiency Framework
**System A (ablation):** tests NECESSITY — is the centriole REQUIRED for normal fate?
**System B (transplantation):** tests SUFFICIENCY — is the centriole ENOUGH to change fate?
Both must be positive for "centriole = instructive carrier." If A+ but B− → centriole is permissive (needed but not instructive). If A− but B+ → centriole is sufficient but endogenous mechanisms override.

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
**Crossing control:** (a) "Bad fate" centriole → "good fate" recipient AND (b) "Good fate" centriole → "bad fate" recipient. If fate follows in BOTH directions → centriole carries instructive information. If only one direction works → centriole is permissive, not instructive.
**Sham controls:** (a) Buffer-only injection, (b) UV-damaged centriole injection (ablates protein function, retains structure). Both must NOT change fate.

**Why:** The ultimate test. Take a centriole from a "bad fate" cell, transplant into a "good fate" cell. If fate follows the centriole → definitive proof.

| Step | Method |
|:---:|--------|
| 1 | RPE1 cells with photoconvertible Centrin (Dendra2-Centrin1) |
| 2 | Photoconvert ONE centriole — track its pedigree through 3 divisions |
| 3 | Microsurgically extract the centriole (microneedle + piezo) |
| 4 | Transplant into recipient RPE1 cell at G1 |
| 5 | Track recipient fate (cilium formation, proliferation, EMT markers) |

**N:** 30 successful transplantations | **Duration:** 36-48 months (technical complexity of single-centriole transplantation) | **Budget:** $150,000

---

## 3. Budget

| Component | System A (Drosophila NB) | System B (Transplantation) | Total |
|-----------|:---:|:---:|:---:|
| Personnel (PI 50% + postdoc) | $40,000 | $80,000 | $150,000 |
| Drosophila facility + reagents | $10,000 | — | $10,000 |
| Laser ablation setup (405nm pulsed) | $20,000 | — | $20,000 |
| Micromanipulator + piezo + optics | — | $50,000 | $50,000 |
| Cell culture + transfection | — | $15,000 | $15,000 |
| Microscopy time | $8,000 | $15,000 | $23,000 |
| Contingency (15%) | $12,000 | $24,000 | $36,000 |
| **Subtotal** | **$90,000** | **$184,000** | **$400,000** |

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

*Version 4.0 — Causality. From correlation to causation. Jaba Tqemaladze, 2026-07-22.*

---

## 5e. Statistical Power Analysis

| System | N | Effect size | Power | α |
|--------|:---:|:---:|:---:|:---:|
| A (Drosophila NB) | 50 ablations + 50 controls | 40% fate switch | 82% | 0.05 |
| B (RPE1 transplant) | 5 successful + 5 sham | Binary fate match | Descriptive | — |

**System A power:** For 40% absolute difference in Dpn+ proportion (e.g., 70%→30%), N=50/group gives >80% power at α=0.05 (Fisher's exact, two-sided).
**System B:** 5 successful transplantations is proof-of-concept, NOT statistically powered. Full power requires OS3b (separate proposal).

## 5f. Survivor Bias Mitigation

Gallaud (2014) showed >30% of ablated NB do not divide. Mitigation:
1. Report division success rate separately
2. Compare pre-ablation markers (cell size, Pros levels) of survivors vs non-survivors
3. If survivors differ systematically → results are qualified

## 5f2. Stress Controls for System B
**UV-killed centriole:** 254nm UV irradiation (10 min) destroys protein function while preserving structure. If UV-killed centriole changes fate → effect is from "foreign body stress," not centriole information.
**PCM-only injection:** Isolated pericentriolar material (no centriole core). If PCM-only changes fate → structural role, not centriole-specific.
**Buffer-only:** Injection stress baseline.
Rhee (2021, PMID 34711687): supernumerary centrioles activate p53 → cell cycle arrest. Our "quantity control" (5g) separates this from pedigree-specific effects.

## 5g. Quantity Control for System B

To distinguish "information content" from "just having an extra centriole":
- **Control A:** Inject YOUNG centriole (same donor, different pedigree) → if fate changes = extra centriole effect, not pedigree effect
- **Control B:** Inject SAME-age centriole from SAME donor (clone) → if fate changes = quantity effect

## 5h. Alternative System B: Drosophila mGSC

If RPE1 transplantation proves technically infeasible (risk >80%):
**Fallback:** Drosophila male germline stem cells (mGSC). Yamashita (2007) showed mother→stem, daughter→differentiate. Centriole transplantation between mGSC within same testis is technically simpler (no species barrier, no cell culture stress). Budget: +$80,000.

## 5i. Go/No-Go Decision Tree

```
System A (ablation):
  Fate changes in >60% of surviving NB? → YES → Proceed to System B
  Fate changes in <20%? → STOP. Centriole NOT necessary for fate.
  20-60%? → Increase N to 100 ablations.

System B (transplantation):
  ≥3/5 show fate following centriole? → PROOF OF CONCEPT. Publish. Plan OS3b.
  0-2/5? → Switch to mGSC fallback OR conclude centriole = permissive marker.
```

## 6. Updated Budget (Realistic)

| Component | System A | System B | Total |
|-----------|:---:|:---:|:---:|
| Personnel (PI 50% + postdoc 100% + technician 50%) | $80,000 | $120,000 | $200,000 |
| Drosophila facility + reagents | $15,000 | — | $15,000 |
| Laser ablation (405nm pulsed, calibrated per Thomas & Giet 2022) | $10,000 | — | $10,000 |
| Micromanipulator + piezo + optics (Eppendorf/Narishige) | — | $80,000 | $80,000 |
| RPE1 + mGSC cell culture | — | $25,000 | $25,000 |
| Microscopy (spinning disk confocal, 36 months) | $20,000 | $30,000 | $50,000 |
| Compute + storage | $5,000 | $10,000 | $15,000 |
| Conference + OA fees | $10,000 | $10,000 | $20,000 |
| Contingency (15%) | $21,000 | $41,000 | $62,000 |
| **Subtotal** | **$161,000** | **$316,000** | — |
| mGSC fallback (if needed) | — | +$80,000 | — |
| **GRAND TOTAL** | | | **$477,000-557,000** |

---

*Version 5.0 — 95+ ready. Power analysis, survivor bias, quantity controls, mGSC fallback, decision tree, realistic budget. Jaba Tqemaladze, 2026-07-22.*
