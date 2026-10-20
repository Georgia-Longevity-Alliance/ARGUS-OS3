# TODO — ARGUS-OS3
- [x] System A: Drosophila NB laser ablation setup
- [x] System B: Centriole transplantation protocol development
- [x] Grant application for causality testing
- [x] Pre-registration on OSF

## 🔧 Automated Ablation Loop (2026-10-20, pattern: Kaneshiro 2022 DOI 10.1017/qpb.2022.24)
> Design: `docs/AUTOMATED_ABLATION_LOOP.md`. Converts click-to-ablate into a closed detect→classify→gate→mask→irradiate→verify→QC loop.
- [ ] P0: Pre-ablation viability gate (skip dead cells) — flag in classifier
- [ ] P0: Keep-out masking (protect non-ablated / sister-pair control / recipient cells) — wrong-cell kill <5%
- [ ] P1: In-loop post-ablation verification (H2B-GFP fragmentation + Centrin1-GFP loss, objective pass/fail)
- [ ] P1: Per-cell disruption-success QC log → Flight Recorder
- [ ] P1: Fail-safe retry policy (one retry +10% dose, cap at phototoxicity ceiling per Body Law)
- [ ] P2: Pilot validation — Pilot A (sham, no bystander) + Pilot B (whole-cell, ≥85% specific, wrong-cell <5%)
