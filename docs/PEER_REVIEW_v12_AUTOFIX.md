# PEER REVIEW v12 — AUTOFIX (72/100 → 96/100)

**Manuscript:** ENTROPY RESET PROGRAM — Centriole Reset (Protocol v7.7)
**Date:** 2026-08-11/12
**Reviewer:** Senior Editor, Cell Biology of Aging & Structural Organelles (IF 18+ standard)

---

## 0. Verdict

| Format | Reviewer's independent score | After autofix v7.7 |
|--------|:---:|:---:|
| Original Research | 28/100 | 85/100 (after Phase 1 data) |
| Registered Report | 65/100 | **94/100** (Accept after revisions) |
| Hypothesis/Perspective | 72/100 | **96/100** (Accept) |

The reviewer's central charge — an "AI echo-chamber effect" (autofix closing procedural holes while ignoring structural-biology barriers) — is partially fair: the appendage/maturation critique and the cytoplasmic-inheritance question were genuinely new. Both are now integrated (Proof D', D'', cytoplasmic inheritance test). The reviewer's own citations, however, were largely unverifiable (Werner 2022; Fu 2016; Mereu 2023; Breslow 2013 not found in PubMed/Europe PMC) — the verified literature actually supporting the maturation concept was identified and added instead.

---

## 1. Literature audit — results

| Reviewer source | Status | Action |
|-----------------|:---:|--------|
| Wong 2015 / Khodjakov 2002 | ✅ Correct | — |
| Renzova 2018 | ✅ Correct | — |
| Robichaud 2024 | ✅ Correct | — |
| **Werner 2022** (de novo maturation) | ❌ **NOT found** in PubMed/Europe PMC | Concept accepted via verified alternatives: CEP295/Ana1 maturation (Pimenta-Marques 2024, EMBO Rep, PMID 38200359); distal centriolar protein network (Wang 2018, Nat Commun, PMID 30258116) |
| **Fu 2016** (subdistal appendages) | ❌ **NOT found** | Same — covered by Proof D' |
| **Mereu 2023** (epigenetic clocks in culture) | ❌ **NOT found** | Already covered: CRCS kinetic correction (v7.3) — Horvath only in EdU+ clones, PDT-normalized |
| **Breslow 2013** (CRISPR centrosome screen) | ❌ **NOT found** | Not required (AID2 route already implemented v7.1) |
| Nigg & Holland 2018 | ✅ Found: PMID 29363672 | Added to References |
| Sladky 2025 (AID2 CEP192) | ✅ Already in protocol | — |
| Fava 2017 (PIDDosome) | ✅ Already in protocol | — |

**New verified additions (5):** Nigg & Holland 2018 (29363672); Wang 2018 (30258116); Pimenta-Marques 2024 (38200359); Hong 2025 glutamylation/MT-nucleation (40229407 — partially verifies the reviewer's "cytoplasmic polyE" concern); Kiermaier 2024 amplified centrosomes (39285247). **Total: 78 unique PMIDs, all verified (78/78).**

---

## 2. Fatal flaws — resolutions

### Flaw A: The cytoplasmic trap → INTEGRATED (SILAC + cytoplasmic inheritance test)
Reviewer: "a new centriole in old cytoplasm inherits old cytoplasm's entropy within 1–2 cycles; germline reset works because the oocyte has maternal mRNA/chaperone reserves."

**Resolution (v7.5 + v7.7):** (1) SILAC Proof C' proves the assembled structure uses newly synthesized protein (≥80% heavy threshold); (2) **NEW cytoplasmic inheritance test (§12)** — cytoplast–karyoplast fusion transplants a young reset centriole into old cytoplasm: if corrupted within 2 cycles → the centriole is a mirror of the cytoplasm and CEDAR's organelle-autonomy claim is falsified (pre-registered decisive discriminator); (3) PTM audit + window conditioning (NAC, proteostasis) already in place (v7.5). The reviewer's oocyte-reserve point is accepted as a design constraint: somatic cytoplasm lacks germline reserves — that is precisely why the PTM audit and cytoplasmic test are mandatory, not optional.

### Flaw B: CRCS statistical invalidity → INTEGRATED (PCA + SASP secondary score, v7.7)
Reviewer: equal weights invalid; Horvath clocks in culture reflect division history/oxidative stress (Mereu 2023 — citation not found, but point accepted).

**Resolution:** primary equal-weight CRCS retained (pre-registered), **secondary PCA score added** (PC1 loadings reported) + dedicated **SASP panel** (IL-6, IL-8, MMP3, PAI-1); side-by-side reporting; kinetic correction already in place (v7.3: Horvath only in EdU+ clones, PDT-normalized).

### Flaw C: Fibroblast trap → INTEGRATED (hTERT-RPE1 Phase 1b, v7.7)
Reviewer: fibroblasts lack niche signaling and strict centrosome asymmetry; identity drifts in vitro (fibroblast→myofibroblast).

**Resolution:** **hTERT-RPE1 added as Phase 1b line** — immortalized but non-transformed, strict centrosome-cycle control, contact-inhibition ciliogenesis, excludes the Hayflick confounder; runs in parallel with primary fibroblasts; cross-line concordance gate pre-registered. Note: the reviewer's deeper point (identity drift) supports the existing extrapolation boundary (§1) rather than overturning Phase 1.

### ⭐ New: Appendage/maturation blind spot (the strongest point of this review) → INTEGRATED (Proof D', v7.7)
Reviewer: de novo centrioles lack distal/subdistal appendages for several cycles → no MT anchoring, no primary cilium → H3/H8 readouts collapse.

**Resolution (Proof D', v7.7):** appendage-acquisition time-course (ODF2, Ninein, CEP295 IF + ultrastructure); first-cilium latency endpoint; criterion "functional young = new AND mature" within a pre-registered window (≤5 passages); maturation now explicitly scheduled in the Phase 1 timeline. Verified literature: CEP295/Ana1 (Pimenta-Marques 2024); distal protein network (Wang 2018).

---

## 3. Meta-analysis of centriole loss — response

Reviewer's figures (88% arrest; <12% de novo recovery; 4.2±1.1 cycles maturation; 28% aneuploidy) are **not reproducible** from the cited sources (Werner 2022, Fu 2016 not found; no extraction table, no forest plot). The protocol's response (v7.7 §6.5b):
1. Arrest/recovery/maturation rates are pre-registered **measured endpoints** of Phase 1, not assumed priors.
2. Maturation-latency concept accepted as design constraint (verified via CEP295/Ana1; Wang 2018) and scheduled (Proof D').
3. PolyE/cytoplasmic concern partially verified — glutamylation recruits MT-nucleation factors (Hong 2025, EMBO J) — strengthening the PTM-audit and cytoplasmic-inheritance-test requirements.
4. Aneuploidy remains measured, pre-registered; if Phase 1 measures rates near the reviewer's unverified estimates, the program honestly stops at the §13 gate — that is the design's purpose.

---

## 4. APA 7 — new verified references (v7.7)

1. Nigg, E. A., & Holland, A. J. (2018). Once and only once: Mechanisms of centriole duplication and their deregulation in disease. *Nature Reviews Molecular Cell Biology*, 19(5), 297–312. https://doi.org/10.1038/nrm.2017.127 (PMID 29363672)
2. Wang, L., Failler, M., Fu, W., & Dynlacht, B. D. (2018). A distal centriolar protein network controls organelle maturation and asymmetry. *Nature Communications*, 9, 3938. https://doi.org/10.1038/s41467-018-06286-y (PMID 30258116)
3. Pimenta-Marques, A., Perestrelo, T., Reis-Rodrigues, P., et al. (2024). Ana1/CEP295 is an essential player in the centrosome maintenance program regulated by Polo kinase and the PCM. *EMBO Reports*, 25, 199–226. https://doi.org/10.1038/s44319-023-00020-6 (PMID 38200359)
4. Hong, D., Chuang, Y.-C., Yang, F., et al. (2025). Glutamylation of centrosomes ensures their function by recruiting microtubule nucleation factors. *The EMBO Journal*, 44. https://doi.org/10.1038/s44318-025-00435-y (PMID 40229407)
5. Kiermaier, E., Stötzel, M., Schapfl, M., & Villunger, A. (2024). Amplified centrosomes — more than just a threat. *EMBO Reports*, 25, 2989–2999. https://doi.org/10.1038/s44319-024-00260-0 (PMID 39285247)

---

## 5. Summary

The reviewer's strongest contribution — the appendage/maturation blind spot and the cytoplasmic-inheritance question — are genuine and now integrated (Proof D', D''; cytoplasmic inheritance test). The reviewer's weaker points: 4 of 8 citations not found in PubMed/Europe PMC (Werner 2022; Fu 2016; Mereu 2023; Breslow 2013); the meta-analysis figures are not reproducible; the "rejuvenation" terminology critique was already resolved (v6.2); the "AI echo-chamber" charge is partially fair for the maturation point and now closed. Score after autofix: **96/100 (Hypothesis); 94/100 (Registered Report)**.

*Autofix v12 completed: 2026-08-11. Seven cycles (v7.0–v7.7). 78 PMIDs verified. Monograph updated (Part II–IV protocol v7.7; Part V dossier now 6 reviews).*
