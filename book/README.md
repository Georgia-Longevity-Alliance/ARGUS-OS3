# REBUILD — автоматизация монографии

## Одна команда вместо 5 ручных шагов

```bash
bash /home/oem/Desktop/Marketing/ARGUS-OS3/book/rebuild.sh
```

Что делает автоматически:
1. Пересобирает монографию (md) из: титул + теория + **протокол (verbatim)** + рецензии (EN) + inquiry + Figure 1 + conclusion
2. Копирует на Desktop
3. Конвертирует в PDF (md2docx → LibreOffice)
4. Собирает полную печатную книгу (обложки + монография + QR)

## С push в GitHub

```bash
bash /home/oem/Desktop/Marketing/ARGUS-OS3/book/rebuild.sh --push
```

Дополнительно коммитит и пушит все 3 репозитория (ARGUS-OS3, Marketing, LC).

## Как это работает

```
ПРАВКА → протокол (docs/ENTROPY_RESET_PROGRAM_COMPLETE.md)
   ↓
rebuild.sh
   ↓
монография (md) → PDF (90 стр.) → полная книга (92 стр.) → Desktop → git push
```

## ВАЖНО

- **Источник истины — ПРОТОКОЛ.** Все научные правки вносятся в `docs/ENTROPY_RESET_PROGRAM_COMPLETE.md`.
- Монография берёт протокол **целиком** (verbatim) — ничего не теряется.
- Рецензии в монографии (Part V) — английские переводы из `book/02_part5_reviews_en.md`. При добавлении новой рецензии: создать `docs/PEER_REVIEW_vN_AUTOFIX.md` (англ.) + дописать её в `book/02_part5_reviews_en.md` → запустить rebuild.
- Русские оригиналы рецензий остаются в `docs/` (внутренние).
