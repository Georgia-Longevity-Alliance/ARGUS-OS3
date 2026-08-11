#!/bin/bash
# ============================================================
# REBUILD — пересборка монографии + PDF + полной книги из протокола
# Использование: bash rebuild.sh  [--push]
#   (без флагов) — пересобрать монографию + PDF + книгу
#   --push        — дополнительно git push (ARGUS-OS3 + Marketing + LC)
# ============================================================
set -e
cd "$(dirname "$0")"
ROOT=/home/oem/Desktop/Marketing/ARGUS-OS3
DESKTOP=/home/oem/Desktop
VERSION=$(grep -oP '(?<=\*\*Version:\*\* )\S+' "$ROOT/docs/ENTROPY_RESET_PROGRAM_COMPLETE.md" | head -1)
echo "=== Версия протокола: $VERSION ==="

# 1. Пересборка монографии (md) из протокола + теории + рецензий
python3 "$ROOT/book/rebuild_monograph.py"
echo "✅ Монография (md) пересобрана"

# 2. Копия на Desktop
cp "$ROOT/book/MONOGRAPH_Centriole_Reset.md" "$DESKTOP/MONOGRAPH_Centriole_Reset.md"
echo "✅ Desktop-копия (md)"

# 3. PDF: md → docx → pdf
"$DESKTOP/Services/target/release/md2docx" "$DESKTOP/MONOGRAPH_Centriole_Reset.md" -o "$DESKTOP/MONOGRAPH_Centriole_Reset.docx" 2>/dev/null
soffice --headless --convert-to pdf "$DESKTOP/MONOGRAPH_Centriole_Reset.docx" --outdir "$DESKTOP/" 2>/dev/null
echo "✅ PDF монографии"

# 4. Полная книга (обложки + монография + QR)
python3 "$ROOT/book/rebuild_book.py"
echo "✅ Полная книга (обложки + PDF)"

# 5. Опциональный push
if [ "$1" == "--push" ]; then
  echo "=== Push ARGUS-OS3 ==="
  cd "$ROOT" && git add -A && git commit -m "Rebuild: protocol $VERSION → monograph/PDF/book" 2>/dev/null | tail -1; git push origin main 2>&1 | tail -1
  echo "=== Push Marketing ==="
  cd /home/oem/Desktop/Marketing && git add -A && git commit -m "Rebuild sync: $VERSION" 2>/dev/null | tail -1; git push origin main 2>&1 | tail -1
  echo "=== Push LC ==="
  cd /home/oem/Desktop/LC && git add -A && git commit -m "Rebuild sync: $VERSION" 2>/dev/null | tail -1; git push origin main 2>&1 | tail -1
  echo "✅ Все репозитории запушены"
fi
echo "=== ГОТОВО: протокол $VERSION → монография + PDF + книга на Desktop ==="
