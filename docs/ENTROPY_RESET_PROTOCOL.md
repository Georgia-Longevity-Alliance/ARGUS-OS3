# ENTROPY RESET PROTOCOL — Full Hallmark Coverage
## The Centriole as a Candidate Structural Aging Carrier

**Version:** 3.0 | **Date:** 2026-08-11 | **Author:** Jaba Tqemaladze, MD (Georgia Longevity Alliance)

**Goal:** Test whether a somatic cell can reset its aging-associated state the way nature does between **meiosis I and the first blastomeres** — centriole elimination followed by de novo assembly — producing **coordinated improvements across hallmark-associated readouts** (López-Otín et al., 2013, PMID 23746838; 2023, PMID 36599349), while **preserving the diploid chromosome set and avoiding crossing-over.**

**Central candidate:** the **centriole** — a cellular structure that undergoes programmed elimination and/or de novo biogenesis during specific stages of reproduction and early development in several metazoan systems. It is proposed as a **candidate structural aging carrier** (CEDAR: Centriolar Entropy-Damage Accumulation Ratchet; Tkemaladze, 2023, PMID 36583780).

> **Level-of-evidence declaration.** This document intentionally distinguishes four levels of statement: **[E] established evidence** (published, replicated), **[I] inference** (strong but indirect), **[H] hypothesis** (the CEDAR model), **[P] prediction** (falsifiable outcome of this protocol). Statements without a marker are protocol design. This separation is the primary response to peer review.

---

## 1. The Natural Template: What Nature Does Between Meiosis I and the First Blastomeres

**[E]** Across metazoans, the germline resets several aging-associated features at the start of each generation:

| Step | Event | Documented in |
|:---:|------|---------------|
| 1 | The oocyte **eliminates its centrioles** before/during meiotic maturation | Mouse (Simerly 2018, PMID 30143724); starfish (Borrego-Pinto 2016, PMID 27002173); Drosophila (Pimenta-Marques 2016, PMID 27229142) |
| 2 | The sperm contributes a centriole that acts as a **seed, not a template**, for embryonic biogenesis | Mammalian fertilization literature |
| 3 | First blastomeres assemble functional centrioles | De novo biogenesis pathways (PLK4–STIL–SAS-6) |
| 4 | The zygote undergoes **genome-wide epigenetic reprogramming** | Mammalian preimplantation development |
| 5 | **Telomeres** are re-extended in the germline/early embryo | Germline telomerase activity |
| 6 | **Mitochondria** are inherited through the maternal line with a bottleneck | Germline mtDNA transmission |

**[E]** The cost of the germline route: haploidization (loss of the diploid set) and crossing-over (meiotic recombination).

**[H] The question of this protocol:** can the germline-style reset be achieved in a **somatic** cell — centriole elimination → de novo assembly, plus targeted interventions on each hallmark — while keeping the diploid genome intact and avoiding crossing-over? **[P]** If the centriole is a structural aging carrier, this should produce coordinated, measurable improvements across multiple hallmark-associated readouts.

---

## 2. The Centriole as a Candidate

**[H]** The centriole is proposed as a **candidate structural memory component** of the aging cell. Unlike the epigenome (reprogrammable by transcription factors), the centriole is a long-lived, semi-conservatively duplicated structure that may transmit accumulated modifications to progeny:

> S_centriole(t) = S₀ + β·t + η(t)

where η(t) denotes stochastic damage (ROS, glycation, thermal fluctuations) and β the time-driven accumulation rate. Asymmetric divisions may further remodel the hypothetical Centriolar Aging-Associated Signaling Module (CAASM):

> CAASM(N) = CAASM₀ − λ·N_asym

> **Model status.** These equations are **phenomenological models** intended to generate falsifiable predictions, **not fitted quantitative laws**. β, λ, and η(t) have **not** been measured. Calibration requires longitudinal imaging, age-resolved centrosomal mass spectrometry, and EM series — proposed in §8.

**[E]** Evidence relevant to the candidate role (levels as marked):

| Statement | Level | Source |
|-----------|:---:|--------|
| Centrioles can be fully eliminated (chemical, genetic, developmental) | [E] | Wong 2015 (PMID 25931445); Renzova 2018 (PMID 30197118); Kalbfuss & Gönczy 2023 (PMID 37963546) |
| Vertebrate cells can assemble centrioles de novo after complete removal | [E] | Khodjakov 2002 (PMID 12356862) |
| Pre-existing centrosomal structures strongly suppress de novo assembly under the conditions of Khodjakov et al. | [E] | Khodjakov 2002 (PMID 12356862) |
| Centrosomes organize the mitotic spindle; supernumerary centrioles correlate with aneuploidy and p53 activation | [E] | Shin et al. 2021 (PMID 34711687) |
| Asymmetric centrosome inheritance biases fate in several stem-cell systems | [E] | Yamashita 2007 (PMID 17255513); Wang 2009 (PMID 19829375); Januschke 2011 (PMID 21407209); Barandun 2025 (PMID 39764850); Zhao 2025 (PMID 41315244) |
| The centrosomal region participates in stress-induced senescence signaling | [I] | Robichaud 2024 (PMID 39266565) — see §5 H8 |
| Centrioles accumulate age-associated structural changes (over-elongation) | [I] | Köhrer 2023 (PMID 37821581) — 45% over-elongated at 24 y → 76% at 67 y |
| Age-related centriole changes **cause** cellular aging | [H] | CEDAR model — **not yet directly tested** |
| Elimination + de novo assembly **rejuvenates** the cell | [P] | **Primary prediction of this protocol — no direct data yet** |

---

## 3. Protocol 0 — Centriole Elimination and De Novo Assembly (the Core)

### Phase 1 — Elimination (meiosis-like step)
Remove **all** centrioles from the somatic cell.

| Method | Agent | Notes |
|:---:|------|-------|
| A. Chemical | Centrinone (PLK4 inhibitor) | Reversible; >95% centriole loss within 3 days (Wong 2015, PMID 25931445) |
| B. Physical | 405 nm pulsed laser ablation | Complete removal; single surviving structures may suppress de novo biogenesis (Khodjakov 2002, PMID 12356862) |
| C. Genetic | Inducible PLK4 / STIL knockout | Cleanest for stable lines; requires inducible system |

**Elimination verification — three independent methods (mandatory):**
1. **Immunofluorescence** for multiple centriole markers: CETN2 (lumen), CEP152 (proximal), SAS-6 (cartwheel) — all three negative in ≥95% of cells;
2. **Electron microscopy** — serial-section EM of a representative sample: no centriolar remnants;
3. **Live-cell imaging** — centrin-GFP photobleaching/recovery control: no residual signal.

**De novo origin verification (mandatory) — exclude incomplete removal and regeneration from remnants:**
- **Photo-convertible centrin** (Dendra2-Centrin1): photoconvert at elimination, track appearance of *non-converted* (new) signal — proves de novo synthesis;
- **SNAP-tag pulse-chase** on centrin/SAS-6: pulse label before elimination, chase after — newly assembled centrioles are label-negative;
- **Correlative light-electron microscopy (CLEM)** on selected cells: ultrastructural confirmation of a genuinely new organelle.

### Phase 2 — De Novo Assembly (blastomere-like step)
Withdraw the inhibitor / switch off the knockout. De novo assembly proceeds through the canonical pathway (PLK4 → STIL → SAS-6 cartwheel → tubulin cylinder). Optional: mild STIL/PLK4 overexpression during recovery to raise de novo efficiency.

### Phase 3 — Core Verification

| Readout | Method | Expected if hypothesis holds |
|---------|--------|------|
| Centriole integrity | EM / centrin-GFP | Normal ultrastructure |
| De novo origin | Dendra2 photoconversion / SNAP chase | New organelle confirmed |
| Ploidy | Karyotype / FISH / WGS copy number | **Diploid preserved** — no haploidization |
| Genome configuration | SNP phasing / allelic ratios | Unchanged — no crossing-over |
| Polyglutamylation (structural age proxy) | GT335 immunofluorescence | Low — fresh tubulin |

---

## 4. The Geometric Accumulation Problem: Which Hallmark Readouts Are Affected

Centriolar aging, **if confirmed**, would accumulate in three regimes. For each we state what is [E], what is [I], and what is [H].

### Regime A — Chronological Age (β·t + η(t))
**[I]** Centrioles are long-lived: polyglutamylation (TTLL5/TTLL6) and stochastic damage may accumulate with time (model parameter β). **[E]** Over-elongation increases with age (Köhrer 2023, PMID 37821581).

| Readout | Mechanism (level) | Source |
|:---:|-----------|:---:|
| **H4** Proteostasis | Structural entropy of the organelle — polyE accumulation (hypothesis; direct longitudinal measurements missing) | [H]/[I] |
| **H8** Senescence | The centrosomal region organizes stress-induced senescence signaling (polyE MT → KIFC3 → FBF1 → PML); does **not** establish the centriole as the primary causal driver | [I] Robichaud 2024, PMID 39266565 |
| **H1** Genomic instability | Supernumerary/aberrant centrioles correlate with aneuploidy and p53 activation; causality of *age-related* centriole damage is not established | [E] Shin 2021, PMID 34711687 |
| **H3** Epigenetic alterations | The hypothetical CAMC on the aged mother centriole may maintain the differentiated state | [H] CEDAR |
| **H10** Intercellular communication | Primary cilium is built on the mother centriole — an aged centriole may build a functionally altered antenna | [I] Anderson & Stearns 2009, PMID 19682908 |
| **H7** Mitochondrial dysfunction | ROS may damage centrioles (η term) — the two candidate carriers may feed each other | [H] |

### Regime B — Asymmetric Divisions of Adult Stem Cells (−λ·N_asym)
**[E]** In several asymmetric stem-cell systems, the older centrosome is inherited preferentially (Yamashita 2007, PMID 17255513; Wang 2009, PMID 19829375; Januschke 2011, PMID 21407209). **[I]** Consequently the stem cell may retain the older structure across many divisions.

| Readout | Mechanism (level) | Source |
|:---:|-----------|:---:|
| **H9** Stem cell exhaustion | Older-centrosome retention is required to maintain stem-cell pools (ninein depletion exhausts progenitors); whether accumulated age *erodes* stemness is the CEDAR hypothesis | [E]–[H] Wang 2009 (PMID 19829375); Chen & Yamashita 2021 (PMID 33435817) |
| **H9** (fate bias) | Mother-centrosome localization biases effector vs. memory fate in CD8+ T-cells; PCM1 on the mother centrosome coordinates neural progenitor fate | [E] Barandun 2025 (PMID 39764850); Zhao 2025 (PMID 41315244) |
| **H8** Senescence of the niche | Long-term stem cells may accumulate senescence-initiation signals precisely because they never eliminate the older organelle | [I]—[H] |
| **H3** Epigenetic drift | Each asymmetric division may remodel the hypothetical CAASM | [H] |

### Regime C — Differentiating Daughters That Do Not Eliminate Centrioles
**[E]** Nature has two strategies at differentiation: **eliminate** (C. elegans — 88% of somatic cells; planarian neoblasts lack centrioles) or **retain** (mammals, Drosophila). **[I]** In retain-systems, differentiated cells carry the inherited organelle into the tissue — the "unpaid meiotic price."

| Readout | Mechanism (level) | Source |
|:---:|-----------|:---:|
| **H8** Senescence | Differentiated cells retaining aged structures may accumulate the senescence-initiation scaffold | [I] Robichaud 2024, PMID 39266565 |
| **H10** Communication | Post-mitotic cells signal through cilia built on the older mother centriole | [I] Anderson & Stearns 2009, PMID 19682908 |
| **H4** Proteostasis | A non-replaced organelle is a permanent PTM burden (if age-dependent PTM accumulation is confirmed) | [I]—[H] |
| **H1** Instability | Where differentiated daughters re-enter division, an inherited aberrant organelle may propagate segregation errors | [I] Shin 2021, PMID 34711687 |
| **H11** Inflammation | Senescent cells (H8) secrete SASP → tissue-level inflammaging | [I] SASP literature |

**Why this mapping matters:** the three regimes overlap in tissue — a stem cell (Regime B) produces a differentiating daughter (Regime C) whose fate is biased by the older mother centriole, in a body whose chronological age (Regime A) has already acted on every centriole. The germline escapes all three because it eliminates and rebuilds. Protocol 0 is the somatic version of that escape — **to be tested, not assumed.**

---

## 5. Hallmark-Associated Protocols (all 12)

Each protocol states: **(a)** what nature does, **(b)** the somatic intervention, **(c)** the centriole's candidate role with level marker, **(d)** verification readout. Where an intervention cannot be fully demonstrated in culture, it is marked **[in vivo required]**.

### H1. Genomic Instability
- **Nature:** zygote engages DNA-damage checkpoints; totipotent cells have high repair capacity.
- **Somatic:** transient DNA-damage-response priming (low-dose, p53-monitored); transient expression of repair factors (PARP1, RAD51) — **recombination for repair only, never shuffling**.
- **Candidate role:** [I] fresh, correctly duplicated centrioles minimize segregation errors; [H] age-related damage causes instability — untested.
- **Verification:** karyotype, FISH, micronucleus assay, γH2AX foci — within diploid normal range.

### H2. Telomere Attrition
- **Nature:** germline/early embryo re-extends telomeres.
- **Somatic:** transient hTERT during the reset window, then withdrawal.
- **Candidate role:** [H] MCARA treats the centriole as a structural analogue of the telomere counter — both semi-conservatively duplicated counters; reset complements, not replaces.
- **Verification:** qFISH/STELA length vs. baseline; no constitutive telomerase after reset.

### H3. Epigenetic Alterations
- **Nature:** zygotic genome-wide reprogramming to totipotency.
- **Somatic:** partial reprogramming (OSKM, 4–8 days, to plasticity not pluripotency) or chemical cocktail (VPA, ascorbic acid, A83-01, CHIR99021).
- **Candidate role:** [H] the hypothetical CAMC maintains the differentiated state; epigenetic reset alone may be transient if the structural counter is not reset.
- **Verification:** EPIC methylome, H3K27ac/H3K4me3, epigenetic clock; differentiated identity not lost.

### H4. Loss of Proteostasis
- **Nature:** oocyte clears and the embryo rebuilds the proteome.
- **Somatic:** HSP induction, proteasome activation, aggrephagy induction (trehalose/rapamycin) before and during reset.
- **Candidate role:** [I]—[H] the centriole is a proteostasis substrate (polyE accumulation) with no efficient dediglutamylase; de novo assembly is the only way to clear *structural* PTM burden.
- **Verification:** proteasome activity, insoluble fraction (ProteoStat), ubiquitin load, GT335.

### H5. Disabled Macroautophagy
- **Nature:** oocytes are autophagy-competent; zygotic clearance is selective.
- **Somatic:** transient autophagy/mitophagy activation (rapamycin, spermidine, TFEB) during reset; damaged organelles cleared before assembly.
- **Candidate role:** [H] complete elimination removes the need for autophagic disposal of the aged organelle (nothing to degrade), mirroring the oocyte.
- **Verification:** LC3-II/I, p62 flux, mito-Keima, autophagic flux.

### H6. Deregulated Nutrient-Sensing
- **Nature:** the oocyte-to-embryo transition resets the maternal mTOR/AMPK network.
- **Somatic:** transient mTORC1 inhibition (rapamycin) + AMPK activation (AICAR/metformin) during reset; return to baseline.
- **Candidate role:** [H] indirect — nutrient sensing gates division; the centriole is the division hardware.
- **Verification:** p-S6K1/p-4E-BP1, p-AMPK, Seahorse respiration, glucose uptake.

### H7. Mitochondrial Dysfunction
- **Nature:** maternal-line bottleneck + zygotic mitophagy purge damaged mtDNA.
- **Somatic:** mitophagy induction (urolithin A, NAD+ precursors, Parkin/PINK1), then biogenesis (PGC-1α) — selective bottleneck, **not** germline reduction.
- **Candidate role:** [H] mitochondrial ROS is a candidate source of centriolar damage (η term); resetting mitochondria helps the fresh organelle start clean.
- **Verification:** mtDNA copy number/heteroplasmy (ddPCR), mitoSOX, TMRM, respirometry.

### H8. Cellular Senescence
- **Nature:** the embryo is senescent-free.
- **Somatic:** senolytic clearance (dasatinib + quercetin, or BCL-2 inhibitors) before reset.
- **Candidate role:** [I] the centrosomal region participates in senescence initiation (Robichaud 2024, PMID 39266565); [P] a fresh centriole may lack the polyE scaffold needed to trigger it.
- **Verification:** SA-β-gal, p16/p21, SASP panel (IL-6, IL-8, MMPs), Ki67 re-entry; **blind analysis** (senescence scoring by operators blinded to condition).

### H9. Stem Cell Exhaustion
- **Nature:** the germline regenerates stemness every generation.
- **Somatic:** transient plasticity induction (H3), colony formation, serial passaging.
- **Candidate role:** [E] asymmetric inheritance biases fate; [H] fresh symmetric centriole pairs remove the asymmetry bias — the reset cell is no longer pre-aged toward differentiation.
- **Verification:** transient stemness markers (NANOG/SOX2/OCT4), colony formation, serial passaging, asymmetric division tracking (centrin-GFP + fate markers), **lineage tracing** to prove the *same cell* is rejuvenated (not selection of rare young subclones).

### H10. Altered Intercellular Communication
- **Nature:** the embryo rebuilds signaling de novo.
- **Somatic:** transient "young environment" (conditioned medium or defined cytokine cocktail); Notch/Wnt/TGF-β rebalancing.
- **Candidate role:** [I] the primary cilium (built on the mother centriole) is the cell's antenna; [P] a fresh centriole builds a fresh antenna.
- **Verification:** ciliary proteome (MS), Hedgehog/Wnt reporters, exosome/cytokine panel in co-culture. **[in vivo required] for full demonstration.**

### H11. Chronic Inflammation
- **Nature:** the embryo is immunologically naive.
- **Somatic:** anti-inflammatory window during reset (low-dose aspirin/curcumin/IL-1β blockade); SASP-cell clearance (H8); restoration of normal signaling.
- **Candidate role:** [H] indirect — inflammation/ROS drive centriolar damage (η); reset removes accumulated damage.
- **Verification:** cytokine panel (IL-1β, IL-6, TNF-α, CRP), NF-κB activity. **[in vivo required] for full demonstration.**

### H12. Dysbiosis
- **Nature:** the newborn is colonized de novo.
- **Somatic (organism level):** FMT or defined probiotic consortium after reset. **[in vivo required] — cannot be demonstrated in cell culture.**
- **Candidate role:** [H] indirect — microbial metabolites influence systemic metabolism/inflammation → cellular ROS → centriolar damage.
- **Verification:** 16S rRNA (Shannon diversity), SCFA levels, mycoplasma screening in culture.

> **Scope statement (peer-review response).** This protocol **tests whether centriole reset produces coordinated improvements across cellular hallmark-associated readouts**. Organism-level hallmarks (H10–H12: intercellular communication, chronic inflammation, dysbiosis) are **evaluated in subsequent in vivo studies**, not claimed as achievable in culture.

---

## 6. The Causal Design — 2 × 2 Factorial (the Central Experiment)

The core causal question: **does de novo centriole assembly improve cell state independently of OSK?** A 2×2 factorial addresses it:

| | **Aged centriole retained** | **De novo centriole (reset)** |
|---|:---:|:---:|
| **No OSK** | A (control) | **B — the critical comparison** |
| **With OSK** | C | D |

- **Main question:** does B outperform A on the primary endpoint **independently of OSK**? If yes → the centriole is a candidate structural aging carrier (sufficiency within the reset pathway).
- **Comparison B vs. D:** does the centriole reset add to OSK-mediated reprogramming?
- **Rescue experiment:** transplant/transfer an aged centriole (or aged centrosomal material) into a reset cell — if the aged phenotype **returns**, the structure carries the information (transplantation arm, see §6b).

### §6b. Transplantation Arm (crossing design)
- **Young → old:** inject a young centriole (known pedigree) into an aged cell → does cell state improve?
- **Old → young:** inject an aged centriole into a young cell → does cell state worsen?
- **If age transfers with the organelle in both directions** → Nature/Cell-level finding (per reviewer consensus).
- Controls: buffer-only, UV-killed centriole (structure without function), PCM-only injection.

### §6c. Falsification Criteria (pre-registered)
The CEDAR hypothesis is **falsified** if any of the following occur:
1. B ≤ A on the primary endpoint (de novo assembly does not improve state without OSK);
2. De novo origin of the "reset" centriole cannot be demonstrated (remnant regeneration instead);
3. Ploidy/genome changes accompany the reset (aneuploidy confound);
4. No hallmark-associated readout improves (scorecard all null);
5. In the transplantation arm, age does not transfer in either direction.

---

## 7. Statistical Design

| Element | Specification |
|---------|---------------|
| **Primary endpoint** | Pre-specified composite: replicative lifespan (Hayflick) + epigenetic clock ΔAge, co-primary |
| **Secondary endpoints** | All 12 hallmark readouts (§5, §9 scorecard) |
| **Effect size** | Expected: 20–40% improvement in primary composite (powered for 25%) |
| **Power** | N = 10 biological replicates per arm × 3 donor lines → >85% power at α = 0.05 (two-sided) for primary composite |
| **Models** | Mixed-effects models (random effects: donor line, experimenter, batch) |
| **Multiple testing** | FDR correction (Benjamini–Hochberg) across the 12 readouts |
| **Blinding** | Senescence scoring, EM assessment, and colony counting by operators blinded to condition |
| **Replication** | 3 independent donor lines: young (<30 y), middle (45–55 y), old (>65 y) |
| **Pre-registration** | Protocol registered before data collection (e.g., OSF/AsPredicted); falsification criteria §6c registered verbatim |
| **Stopping rules** | Pre-specified: interim analysis after 5 replicates; stop for futility if B ≤ A |

**Multi-omics (pre/post, per condition):** scRNA-seq, scATAC-seq, DNA methylation clock (EPIC), quantitative proteomics, phosphoproteomics, and (where material allows) metabolomics.

---

## 8. Parameter Calibration (Model Status Response)

To move from phenomenological model to quantitative theory, measure:
- **β** (time-driven accumulation): longitudinal imaging of GT335/acetyl-tubulin in arrested, non-dividing cells over 6–12 months;
- **λ** (per-asymmetric-division CAASM change): centrosomal proteomics across tracked asymmetric lineages (centrin-GFP lineage tracing + single-centrosome mass spectrometry);
- **η(t)** (stochastic damage): paired ROS measurements (mitoSOX, glycation adducts) with centriole damage readouts;
- **EM series** of age-resolved centrioles (Köhrer-style tomography) to correlate structural change with readout changes.

**Success:** fitted β, λ, η with confidence intervals; model predictions tested prospectively (A/B/D comparisons).

---

## 9. Hallmark Scorecard (pre/post, FDR-corrected)

| # | Readout | Pre | Post | Target |
|:---:|---------|:---:|:---:|:---:|
| H1 | γH2AX, micronuclei | — | — | ≤ baseline |
| H2 | qFISH telomere length | — | — | ≥ baseline |
| H3 | Horvath clock | — | — | ΔAge < 0 |
| H4 | ProteoStat, GT335 | — | — | insoluble fraction ↓ |
| H5 | LC3 flux | — | — | flux ↑ |
| H6 | p-S6K1, p-AMPK | — | — | rebalanced |
| H7 | heteroplasmy, mitoSOX | — | — | damage ↓ |
| H8 | SA-β-gal, SASP (blinded) | — | — | zero senescent |
| H9 | colony formation, lineage tracing | — | — | capacity restored, same-cell proven |
| H10 | ciliary proteome | — | — | young-like* |
| H11 | cytokine panel | — | — | zero chronic burden* |
| H12 | 16S diversity | — | — | young-like* |

*H10–H12 require in vivo follow-up (§5 scope statement).

**Success criterion:** ≥6 of 12 readouts improve in the predicted direction in arm B vs. A (FDR < 0.05), with invariants (§10) intact and de novo origin verified.

---

## 10. The Three Invariants

| Invariant | How it is preserved | Readout |
|-----------|---------------------|---------|
| **Diploidy** | Elimination targets the centriole, never the chromosomes | Karyotype, FISH, WGS copy number |
| **No crossing-over** | Recombination for repair only; no shuffling | Allelic configuration unchanged (SNP phasing) |
| **Full coverage** | All 12 readouts measured pre/post | Hallmark scorecard (§9) |

---

## 11. Timeline & Budget

| Phase | Duration | Budget |
|:---:|:---:|:---:|
| Protocol 0 — elimination + de novo (with 3-method verification) | 8–10 weeks | $45K |
| H1–H3 (genome, telomere, epigenome) | 10–12 weeks | $45K |
| H4–H7 (proteostasis, autophagy, nutrient, mitochondria) | 10–12 weeks | $45K |
| H8–H9 (senescence, stem cells — including 2×2 factorial) | 10–12 weeks | $50K |
| H10–H12 (in vivo follow-up planning) | 4–6 weeks | $15K |
| Multi-omics + statistics + pre-registration | continuous | $30K |
| **Total** | **8–12 months** | **~$230K** |

Fits inside the ARGUS-OS3 envelope ($477–557K, 36–48 months) as an integrated work package.

---

## 12. Controls (shared)

| Control | Purpose |
|---------|---------|
| Untreated cells, same passage | Baseline |
| Centrinone-only (no recovery) | Elimination phenotype |
| Recovery without de novo boost | De novo efficiency baseline |
| p53 inhibition (Pifithrin-α) | Rules out stress/apoptosis artifact |
| Buffer-only / mock injection | Mechanical stress control |
| UV-killed centriole re-injection | "Foreign body" effect |
| Each hallmark intervention alone (no Protocol 0) | Isolates centriolar contribution |

---

## 13. Alternative Hypotheses (peer-review response)

This protocol is designed to **discriminate** among competing models, not confirm CEDAR:

| Model | Prediction under reset protocol | Discriminated by |
|-------|--------------------------------|------------------|
| **Epigenetic (OSK-centered)** | OSK alone (arm C) improves state; centriole reset adds nothing (B ≈ A) | B vs. A comparison |
| **Mitochondrial** | Mitophagy alone (H7) improves state; centriole reset unnecessary | H7-alone control |
| **Proteostatic** | HSP/autophagy induction alone improves state | H4/H5-alone controls |
| **Telomeric** | hTERT alone restores lifespan | H2-alone control |
| **CEDAR (centriolar)** | Centriole reset improves state independently of OSK; age transfers with the organelle | Arm B, transplantation arm |
| **Multi-counter (MCARA)** | Several counters co-limit; combined reset > any single | Factorial decomposition |

---

## 14. Key References (APA 7, all verified via PubMed E-utilities, 2026-08-11)

1. Anderson, C. T., & Stearns, T. (2009). Centriole age underlies asynchronous primary cilium growth in mammalian cells. *Current Biology*, 19(18), 1498–1502. https://doi.org/10.1016/j.cub.2009.07.034 (PMID 19682908)
2. Barandun, N., Meier, B., Stehli, G., Gräbnitz, F., Zangger, N., & Oxenius, A. (2025). Targeted localization of the mother centrosome in CD8+ T cells undergoing asymmetric cell division. *Cell Reports*, 44(1), 115127. (PMID 39764850)
3. Borrego-Pinto, J., Somogyi, K., Karreman, M. A., et al. (2016). Distinct mechanisms eliminate mother and daughter centrioles in meiosis of starfish oocytes. *Journal of Cell Biology*, 213(5), 533–543. (PMID 27002173)
4. Chen, C., & Yamashita, Y. M. (2021). Centrosome-centric view of asymmetric stem cell division. *Current Opinion in Cell Biology*, 68, 6–13. (PMID 33435817)
5. Conduit, P. T., & Raff, J. W. (2010). Cnn dynamics drive centrosome size asymmetry to ensure daughter centriole retention in *Drosophila* neuroblasts. *Current Biology*, 20(24), 2187–2192. (PMID 21145745)
6. Hong, N., & Cohen, A. A. (2025). Aging as entropy: A quantifiable framework. (PMID 41299832)
7. Hong, N., Cho, S. W., Cohen, A. A., et al. (2026). Entropy of muscle fiber histology predicts mobility in older adults. (PMID 41724675)
8. Januschke, J., Llamazares, S., Reina, J., & Gonzalez, C. (2011). *Drosophila* neuroblasts retain the daughter centrosome. *Nature Communications*, 2, 243. (PMID 21407209)
9. Kalbfuss, N., & Gönczy, P. (2023). Towards understanding centriole elimination. *Open Biology*, 13, 230222. (PMID 37963546)
10. Khodjakov, A., Rieder, C. L., Sluder, G., Cassels, G., Sibon, O., & Wang, C.-L. (2002). De novo formation of centrosomes in vertebrate cells arrested during S phase. *Journal of Cell Biology*, 158(7), 1171–1181. (PMID 12356862)
11. Kochanski, R. S., & Borisy, G. G. (1990). Mode of centriole duplication and distribution. *Journal of Cell Biology*, 110(5), 1599–1605. (PMID 2335566)
12. Köhrer, S., Dittrich, T., Schorb, M., et al. (2023). High-throughput electron tomography identifies centriole over-elongation as an early feature of cell and organismal aging. (PMID 37821581)
13. López-Otín, C., Blasco, M. A., Partridge, L., Serrano, M., & Kroemer, G. (2013). The hallmarks of aging. *Cell*, 153(6), 1194–1217. https://doi.org/10.1016/j.cell.2013.05.039 (PMID 23746838)
14. López-Otín, C., Blasco, M. A., Partridge, L., Serrano, M., & Kroemer, G. (2023). Hallmarks of aging: An expanding universe. *Cell*, 186(2), 243–278. https://doi.org/10.1016/j.cell.2022.11.001 (PMID 36599349)
15. Pimenta-Marques, A., Bento, I., Lopes, C. A., et al. (2016). A mechanism for the elimination of the female gamete centrosome in *Drosophila* meiosis. *Science*, 353(6294), aaf4866. (PMID 27229142)
16. Rebollo, E., Sampaio, P., Januschke, J., Llamazares, S., Varmark, H., & González, C. (2007). Functionally unequal centrosomes drive spindle orientation in asymmetrically dividing *Drosophila* neural stem cells. *Developmental Cell*, 12(3), 467–474. (PMID 17336911)
17. Renzova, T., Bohaciakova, D., Esner, M., Pospisilova, V., Barta, T., & Hampl, A. (2018). Inactivation of the PLK4–STIL module prevents self-renewal and triggers p53-dependent differentiation in human embryonic stem cells. *Stem Cell Reports*, 11(4), 959–972. (PMID 30197118)
18. Robichaud, J. H., Zhang, Y., Chen, C., et al. (2024). Transiently formed nucleus-to-cilium microtubule arrays mediate senescence initiation. *Nature Communications*, 15, 7919. (PMID 39266565)
19. Sahu, S. K., Reddy, P., Lu, J., et al. (2024). Targeted partial reprogramming of age-associated cell states improves markers of health. (PMID 39259812)
20. Shin, B., Kim, M. S., Lee, Y., et al. (2021). Generation and fates of supernumerary centrioles in dividing cells. *Molecules and Cells*, 44(11), 805–816. (PMID 34711687)
21. Simerly, C., Manil-Ségalen, M., Castro, C., et al. (2018). Separation and loss of centrioles from primordial germ cells to mature oocytes in the mouse. *Scientific Reports*, 8, 12791. (PMID 30143724)
22. Thomas, C., & Giet, R. (2022). Live imaging of *Drosophila melanogaster* neural stem cells with photo-ablated centrosomes. *STAR Protocols*, 3(3), 101493. (PMID 35776653)
23. Tkemaladze, J. (2023). Reduction, proliferation, and differentiation defects of stem cells over time: A hypothesis of the centriole as the division counter. *Mechanisms of Ageing and Development* (verified via PubMed). (PMID 36583780)
24. Wang, X., Tsai, J.-W., Imai, J. H., Lian, W.-N., Vallee, R. B., & Shi, S.-H. (2009). Asymmetric centrosome inheritance maintains neural progenitors in the neocortex. *Nature*, 461(7266), 947–955. (PMID 19829375)
25. Warren, L., Manos, P. D., Ahfeldt, T., et al. (2010). Highly efficient reprogramming to pluripotency and directed differentiation of human cells with synthetic modified mRNA. *Cell Stem Cell*, 7(5), 618–630. (PMID 20888316)
26. Wong, Y. L., Anzola, J. V., Davis, R. L., et al. (2015). Reversible centriole depletion with an inhibitor of Polo-like kinase 4. *Science*, 348(6239), 1155–1160. (PMID 25931445)
27. Yamashita, Y. M., Mahowald, A. P., Perlin, J. R., & Fuller, M. T. (2007). Asymmetric inheritance of mother versus daughter centrosome in stem cell division. *Science*, 315(5811), 518–521. (PMID 17255513)
28. Zhang, C., Bai, Y., Yin, Q., et al. (2026). Hepatocyte-specific partial cellular reprogramming via selective OSK mRNA lipid nanoparticles. (PMID 41443352)
29. Zielke, L. G., & Ryan, T. J. (2026). Rescuing specific memories by rejuvenating engram cells. (PMID 41856040)
30. Zhao, X., Mouilleau, V., Wang, Y., et al. (2025). PCM1 coordinates centrosome asymmetry with polarized endosome dynamics to regulate daughter cell fate. *Nature Communications*, 16, 10728. (PMID 41315244)
31. De Man, R., McDonough, J. E., Adams, T. S., et al. (2026). Single-cell atlas of human lung aging identifies cell type dyssynchrony. (PMID 41571679)
32. Cummings, S. R., Hong, N., Cohen, A. A., et al. (2025). Entropy and human aging. (PMID 41230623)

> **Citation integrity statement.** All 32 references verified via NCBI E-utilities on 2026-08-11 (titles, authors, journals, years). Two corrections from v2.1: (1) PMID 34711687 is **Shin et al. 2021**, not "Rhee 2021"; (2) the first author of the 2021 *Current Opinion in Cell Biology* review is **Chen C**, not "Chen H". Volume/page data marked where available from PubMed; remaining fields to be completed from journal websites before submission.

---

*Part of the ARGUS-OS3 / CEDAR program — testing whether the germline's elimination-and-rebuild trick can be reproduced in a dish, without the meiotic price, across hallmark-associated readouts.*
