# CONCEPT — ARGUS-OS3

**Version:** 3.0 (НОВАЯ КОНЦЕПЦИЯ)
**Date:** 2026-07-21
> **v3.0:** Полная смена. Старая концепция (fs-лазер + манипуляторы) отброшена. Новая: прогениторные карты как ГРАФ с генетическими сетями. Зависит от успеха OS2.
> **v1.0-2.x:** Лазерная абляция. Устарело.

---

## 0. Что такое ARGUS-OS3

ARGUS-OS3 строит **прогениторные карты** на основе centriole pedigrees центриолей (OS1) и доказательства конвергенции (OS2).

> **🔴 Зависит от успеха OS2.** Без доказательства что centriole pedigree → судьба, карты строить не из чего.

---

## 1. Прогениторная карта = ГРАФ

```
Не дерево (каждый узел = одна клетка)
А ГРАФ (узлы = генетические сети, рёбра = centriole pedigree)
```

| Элемент графа | Что это |
|--------------|---------|
| **Узел** | Паттерн генной экспрессии (генетическая сеть) |
| **Ребро** | Centriole pedigreeия центриоли (∥/⟂ или θ) |
| **Конвергенция** | Разные centriole pedigree → один узел |

### Пример

```
∥→∥→⟂ → узел «нейральная сеть» → нейроны
⟂→∥→∥ → узел «нейральная сеть» → нейроны  ← КОНВЕРГЕНЦИЯ
∥→⟂→⟂ → узел «кожная сеть»    → кожа
```

---

## 2. Что нужно для построения

| Данные | Источник |
|--------|----------|
| Centriole pedigreeии центриолей (∥/⟂, θ) | ARGUS-OS1 |
| Доказательство конвергенции | ARGUS-OS2 |
| Профили генной экспрессии | Single-cell RNA-seq (конечные точки) |
| Судьбы клеток | Дифференцировочные маркеры |

---

## 3. Метод

| Шаг | Действие |
|:---:|----------|
| 1 | Получить centriole pedigree + судьбы от OS1 |
| 2 | Верифицировать конвергенцию от OS2 |
| 3 | scRNA-seq клеток в узлах конвергенции |
| 4 | Построить граф: узлы = кластеры экспрессии |
| 5 | Валидация: предсказание судьбы по узлу |

---

## 4. Бюджет (после OS2)

| Позиция | $ |
|---------|--:|
| scRNA-seq (10X Genomics, 500 клеток) | 8,000 |
| Биоинформатика (анализ графа) | 5,000 |
| Валидация (IF маркеры) | 3,000 |
| **Total** | **~16,000** |

---

## 5. Ключевые источники

| # | Reference | Тема |
|---|-----------|------|
| 1 | Sulston & Horvitz (1977) | Клеточная линия C. elegans |
| 2 | ARGUS-OS1/CONCEPT.md | Centriole pedigreeии центриолей |
| 3 | ARGUS-OS2/CONCEPT.md | Конвергенция |

---

*OS3 — прогениторные карты = граф с генетическими сетями. После OS2.*

---

## Reproducibility & Quality

**Power analysis:** N≈40 sister-cell pairs for OR≥1.5 (α=0.05, β=0.2).
**Blinding:** analyst blinded to pedigree.
**Pre-registration:** OSF before data collection.
**Reproducibility:** all code + data on GitHub + Zenodo (CC-BY).
**Limitations:** (1) Depends on OS2 success. (2) Requires OS1 trajectory data. (3) Single-cell RNA-seq costs not in Core budget. (4) Genetic networks are inferred — require independent validation.

## Key References (additional)

| # | Reference | PMID |
|---|-----------|------|
| 9 | Sulston & Horvitz (1977) — lineage | 838129 |
| 10 | Kalbfuss & Gönczy (2023) — elimination | 37256957 |
| 11 | Gönczy & Balestra (2023) — stochastic | 36988082 |
| 12 | Anderson & Stearns (2009) — age | 19682908 |
