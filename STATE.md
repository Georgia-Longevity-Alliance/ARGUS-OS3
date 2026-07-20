# STATE — ARGUS-OS3

**Date:** 2026-07-21
**Status:** 🟡 v2.1 — Зависит от ARGUS-OS2. Прогениторные карты строятся ПОСЛЕ доказательства гипотезы о spindle orientation pedigreeх.

## Prerequisite

🔴 **ARGUS-OS2 должен доказать:** spindle orientation pedigree центриоли → судьба клетки (конвергенция A=C≠B=D).

Без этого OS3 не имеет основания.

## New Role (post OS2 v4.0)

ARGUS-OS3 строит **прогениторные карты как ГРАФ** (не дерево) на основе spindle orientation pedigrees центриолей, прочитанных ARGUS-OS1 и ARGUS-OS2.

### Принцип

1. ARGUS-OS1 измеряет spindle orientation pedigree центриолей (XYZ-вектор каждого деления)
2. ARGUS-OS2 доказывает что spindle orientation pedigree → судьба (конвергенция)
3. ARGUS-OS3 строит карту: граф где узлы = клеточные судьбы, рёбра = spindle orientation pedigree, конвергенции = классы эквивалентности

### Отличие от старой концепции

| Старая (v1.0) | Новая (v2.0) |
|---------------|-------------|
| fs- + ы | Чтение центриолей |
| Физическое разделение клеток | Информационная реконструкция |
| $40K оборудование | Софт + данные OS1/OS2 |
| Одна клетка за раз | Все клетки одновременно |

## Core Files

| File | Status |
|------|:---:|
| CONCEPT.md | 🟡 Need update |
| STATE.md | ✅ v2.0 |
| Others | 🟡 Need sync |
