# APPENDIX — Systematic Search Protocol (novelty verification)
**Entropy Reset Protocol v6.2 · Date of search: 2026-08-11 · Method: NCBI E-utilities (PubMed) + Europe PMC (incl. preprints) + Crossref**

## 1. Objective
Verify the novelty statement: *"To our knowledge, no study has yet directly tested whether controlled centriole elimination followed by bona fide de novo biogenesis produces OSK-independent improvements in defined cellular aging phenotypes."*

## 2. Databases (search expanded per 7th review)

| Database | Coverage | Status |
|----------|----------|:---:|
| PubMed (NCBI E-utilities) | peer-reviewed | ✅ done 2026-08-11 |
| Europe PMC | PubMed + preprints (bioRxiv/medRxiv) | ✅ done 2026-08-11 |
| Crossref | global DOI metadata (journals + preprints) | ✅ done 2026-08-11 |
| **OpenAlex** (free, ~250M works, Scopus-level coverage) | journals + preprints + books | ✅ done 2026-08-11 |
| Semantic Scholar | — | ⚠️ rate-limited (HTTP 429) on 2026-08-11; to be re-run pre-submission |
| Scopus / Web of Science | — | ⏳ planned pre-submission (institutional access required) |

## 3. Queries and results

### 3.1 PubMed (2026-08-11)
| # | Query | Hits | Relevant |
|---|-------|:---:|:---:|
| 1 | `centriole AND rejuvenation` | 1 | 0 |
| 2 | `centriole elimination AND rejuvenation` | 0 | — |
| 3 | `centrinone AND rejuvenation` | 0 | — |
| 4 | `de novo centriole AND rejuvenation` | 0 | — |
| 5 | `centriole AND reprogramming AND somatic` | 0 | — |
| 6 | `centriole AND OSK` | 1 | 0 |
| 7 | `centriole AND pluripotency AND elimination` | 1 | 0 |
| 8 | `centrosome AND de novo AND aging` | 2 | 0 |
| 9 | `centriole replacement AND cell aging` | 1 | 0 |
| 10 | `centriole AND longevity` | 3 | 0 |

### 3.2 Europe PMC (2026-08-11)
| Query | Hits | Relevant |
|-------|:---:|:---:|
| `centriole AND rejuvenation` | 28 | 0 (reviews on asymmetric division, conference posters) |
| `centriole elimination AND rejuvenation` | 10 | 0 (reviews; conference abstracts) |
| `de novo centriole AND rejuvenation` | 15 | 0 |
| `centrinone AND rejuvenation` | 0 | — |
| **Preprints** (`AND SRC:PPR`): `centriole AND rejuvenation` | 1 | **1 — author's own MCARA preprint (2026)** — theoretical, no experiment; excluded as non-test |
| Preprints: `centriole elimination AND SRC:PPR` | 19 | 1 — author's own "Centriole Elimination as a Gateway to a New Differentiation State" (2026) — protocol, no data; excluded as non-test. Remaining 18: non-relevant (axoneme elimination in *Naegleria*; MOCT in protists) |

### 3.3 OpenAlex (2026-08-11) — Scopus-level coverage, free
| Query | Works | Relevant |
|-------|:---:|:---:|
| `centriole rejuvenation` | 243 | 0 direct tests (phrase-level; top hits unrelated: "Rejuvenation Biotechnology"; "Centrioles and Cellular Differentiation") |
| `centriole elimination rejuvenation` | 144 | 0 direct tests (top hit: "Centrioles as Structural Damage Reservoirs" — theory, no experiment) |
| `de novo centriole aging` | 1,745 | 0 direct tests (reviews of centriole/cilium biogenesis) |
| `centrinone rejuvenation` | 15 | 0 direct tests |

### 3.4 Crossref (2026-08-11)
| Query | Total | Relevant |
|-------|:---:|:---:|
| `centriole rejuvenation` | 13,024 (full-text phrase matches) | 0 direct tests (top hits: 2010 "Centriole, Differentiation, and Senescence"; author's gametogenesis preprint) |
| `centriole elimination rejuvenation` | 83,615 | 0 direct tests |

> **Transparency note (per 7th review):** Crossref full-text counts are phrase-level and not informative alone; relevance assessed on the top-10 titles per query. Two hits are **the author's own preprints** (MCARA; Centriole Elimination Gateway) — they are listed here explicitly, are theoretical/protocol-only (no experimental test of the aging-phenotype question), and are excluded from the novelty claim. Scopus/WoS to be run pre-submission.

## 4. DOI cross-check of the 47 verified references (per 7th review)
All 47 PMIDs verified via E-utilities batch (2026-08-11). Of these, **39 have DOI records in PubMed**; 8 are pre-DOI-era (1991–2009) and carry no PubMed DOI (e.g., Szöllosi 1991, PMID 1756312; Khodjakov 2002, PMID 12356862; Yamashita 2007, PMID 17255513 — DOI resolvable via publisher/journals directly: 10.1083/jcb.200205102; 10.1126/science.1134910). DOI table available on request; independent four-eyes re-check by a non-author recommended pre-submission.

## 5. Inclusion/exclusion (PRISMA-style)
- **Included:** experimental centriole/centrosome removal + post-removal aging/rejuvenation readout + somatic cells.
- **Excluded (documented):** removal without aging readouts (Khodjakov, La Terra, Uetake, Wong); germline/meiotic elimination; pluripotency-only (Renzova); theory-only preprints (author's own).

## 6. Conclusion

**Search completion status (per 7th review):** PubMed ✅ · Europe PMC (incl. preprints) ✅ · Crossref ✅ · **OpenAlex ✅ (2026-08-11)** · Semantic Scholar ⚠️ rate-limited (re-run planned) · Scopus/WoS ⏳ (institutional access; OpenAlex covers equivalent indexing for the novelty screen). The novelty claim is supported across all completed databases; final Scopus/WoS leg is scheduled before submission.
The novelty claim is supported for the *specific combination* (aging readouts + verified de novo origin + OSK factorial in somatic cells) across PubMed, Europe PMC (incl. preprints), and Crossref. It is **not** claimed that elimination or de novo assembly are novel per se — the four prototypes solved those pieces separately (§3.4–3.5 of the protocol).
