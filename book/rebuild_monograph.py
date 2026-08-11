#!/usr/bin/env python3
"""Чистая научная монография: титул + теория + протокол (Red Thread, Protocol, Search Appendix) + фигуры + references.
Без рецензий, писем, грантовых и внутренних документов."""
import re, sys, os

ROOT = "/home/oem/Desktop/Marketing/ARGUS-OS3"
BOOK = os.path.join(ROOT, "book")
DOCS = os.path.join(ROOT, "docs")

def read(p):
    with open(p) as f:
        return f.read()

def extract_protocol_sections(text):
    """Извлечь PART 0 + PART 1 + PART 3 (научные части), без PART 2 (Grant Core) и PART 4 (Gakely)."""
    parts = re.split(r'\n(?=# PART \d)', text)
    keep = []
    for p in parts:
        if p.startswith("# PART 0") or p.startswith("# PART 1") or p.startswith("# PART 3"):
            keep.append(p)
    return "\n\n".join(keep)

out = []
out.append(read(f"{BOOK}/00_front_matter.md"))
out.append("\n\n---\n\n")
out.append(read(f"{BOOK}/01_part1_theory.md"))
out.append("\n\n---\n\n# Part II — The Complete Protocol (Red Thread · Protocol · Search Appendix)\n\n")
out.append("> **Source:** `docs/ENTROPY_RESET_PROGRAM_COMPLETE.md` (Version 8.3, 2026-08-12). Included in full — Red Thread, Protocol, and Systematic-Search Appendix; no part omitted.\n\n")
proto = read(f"{DOCS}/ENTROPY_RESET_PROGRAM_COMPLETE.md")
out.append(extract_protocol_sections(proto))
out.append("\n\n---\n\n# Figures\n\n")
figures = [
    ("Figure 1 — The Centrosome as a Unidirectional Ratchet of Cellular Identity and Aging",
     "(A) Pluripotent cell: ratchet released down upon centriole loss (Renzova 2018). (B) Somatic cell: ratchet released to plasticity, then re-locked younger (this protocol).",
     "FIGURE_1_Ratchet_Model.png"),
    ("Figure 2 — Experimental Design: 2×2 Factorial with Override and Control Arms",
     "Arms A–D (OSK × reset), control arms E/E' (p53-suppression vs. USP25/28 + PIDD1-KD), perturbation and cGAS/STING-KO dissociation arms, and arm F (temporal dissociation: reset → washout → 10 passages → OSK).",
     "FIGURE_2_Experimental_Design.png"),
    ("Figure 3 — Proof Ladder and Verification Gates",
     "Proofs A–D'''' (de novo origin, SILAC purity, maturation, geometry), gates E–E'' (number, STED structural verification, live first-mitoses), and the phased go/no-go ladder from Phase 1A feasibility to Phase 3 in vivo.",
     "FIGURE_3_Proof_Ladder.png"),
    ("Figure 4 — p53-Surveillance Architecture and Override Strategy",
     "Loss arm (53BP1–USP28–p53; USP25/28 inhibitor preserves p53 for genuine DNA damage) and amplification/inflammation arm (PIDDosome–ANKRD26; cGAS–STING; PIDD1-KD, KO arms; cytostatic window RO-3306).",
     "FIGURE_4_Override_Architecture.png"),
    ("Figure 5 — Transformation Surveillance: Five Pre-Registered Anti-Neoplastic Layers",
     "p53 re-competence, karyotype/ploidy, immortalization screen, anchorage independence, clonal dynamics; any clone failing a layer is excluded; ≥5% flag rate triggers the safety futility stop.",
     "FIGURE_5_Surveillance.png"),
    ("Figure 6 — The 13-Puzzle Schematic (supplementary; schematic only, not a 13th-hallmark claim)",
     "12 Hallmarks of Aging (López-Otín framework) + centriole elimination and de novo synthesis as the candidate mechanistic axis.",
     "ENTROPY_RESET_13_PUZZLES.png"),
]
for title, caption, fname in figures:
    out.append(f"\n![{title}]({DOCS}/{fname})\n\n**{title}.** {caption}\n\n")

result = "\n".join(out)
with open(f"{BOOK}/MONOGRAPH_Centriole_Reset.md", "w") as f:
    f.write(result)
words = len(result.split())
cyr = len(re.findall(r'[а-яА-Я]', result))
print(f"Монография (чистая): {words} слов, {cyr} кириллицы (должно быть 0)")
