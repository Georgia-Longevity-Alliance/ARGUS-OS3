# ARGUS-OS3 — Entropy Reset & Causality Test

**The goal:** reset cellular entropy in a somatic cell the way nature does between **meiosis I and the first blastomeres** — centriole elimination followed by **de novo synthesis** — but **without loss of the diploid chromosome set and without crossing-over.**

Nature performs a complete hardware reset at the start of every generation: the oocyte eliminates its centrioles at meiosis I; the sperm delivers a centriole that becomes a *seed, not a template*; the first blastomeres synthesize centrioles **de novo**. The price: haploidization and crossing-over.

ARGUS-OS3 asks whether the same reset can be achieved in a somatic cell, keeping the diploid genome intact — and whether **changing the centriole changes the cell's fate** (causality, not correlation).

## The Protocol

📄 **[Entropy Reset Protocol](docs/ENTROPY_RESET_PROTOCOL.md)** — full coverage of **all 12 Hallmarks of Aging** (López-Otín), built around the **centriole as the candidate reset carrier**: elimination (meiosis-like) → de novo assembly (blastomere-like) → per-hallmark reset protocols → verification (diploidy preserved, no crossing-over, no haploidization).

## Three Questions

| Project | Question | Answer type |
|---------|----------|:---:|
| OS1 | Does pedigree correlate with fate? | Correlation |
| OS2 | Does pedigree predict fate better than position? | Prediction |
| **OS3** | **Does changing the centriole change the fate?** | **Causality** |

## Two Systems

- **A:** Drosophila NB laser ablation — tests NECESSITY
- **B:** Centriole transplantation — tests SUFFICIENCY

**Budget:** $477-557K | **Timeline:** 36-48 months | **14 references**

## V9 Upgrade — Robot Hands + Shared Local LLM Brain (V9-Full)

OS3 (V8) carries the full V9 autonomy configuration. Two cable-driven robot arms operate through the glove ports **instead of human hands**, providing 24/7 long-term servicing: sample exchange, medium replenishment, objective cleaning, capillary replacement, UV-C zone sterilization, and maintenance of the FOSH micromanipulator and micro-robots inside the enclosure.

The brain is an **external LLM on local hardware** — the same host that controls the micromanipulators and micro-robots (Mac Studio M3 Ultra 192GB, Mixtral/Llama/Qwen 70B, no cloud). Consumables and spare parts are sterilized outside (autoclave/VHP/UV-C/ultrasonic) and enter through the V8/V9-TRANSFER box with hardware interlock; the inner door is opened by the robot hand.

| V9 element | OS3 instantiation |
|-----------|-------------------|
| Hands | 2x cable-driven arms, 5-6 DOF, NEMA 17 + TMC2209, exchangeable end-effectors (gripper, pipette, wipe, UV, capillary, rake) |
| Brain | Shared local LLM host (Mac Studio 192GB); Planner + Tool Bridge + Safety Layer (Body Law) + Flight Recorder (AIS) |
| Transfer box | V8/V9-TRANSFER: 2 doors, hardware interlock, UV-C 254 nm, HEPA purge, VHP option |
| Sterilization | Autoclave + VHP + UV-C + ultrasonic (shared lab set); weekly validation |
| Budget | ~$22.4K base (arms + transfer box + host); ~$34.6K incl. shared sterilization set |

- Design: [ARGUS-OS1/docs/V9_PROTOTYPE.md](https://github.com/Georgia-Longevity-Alliance/ARGUS-OS1/blob/main/docs/V9_PROTOTYPE.md)
- Sterilization & transfer-box SOPs: [ARGUS-OS1/docs/STERILIZATION_TRANSFER.md](https://github.com/Georgia-Longevity-Alliance/ARGUS-OS1/blob/main/docs/STERILIZATION_TRANSFER.md)

## Related

- Part of the LC (LongevityCommon) platform — CEDAR program (centriole elimination for de-differentiation and rejuvenation)
- Jaba Tqemaladze, MD — Georgia Longevity Alliance — jaba@longevity.ge
