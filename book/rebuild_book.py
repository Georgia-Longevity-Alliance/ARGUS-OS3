#!/usr/bin/env python3
"""Пересборка полной печатной книги: передняя обложка + монография PDF + задняя обложка (QR)."""
from PIL import Image
from pypdf import PdfWriter, PdfReader

DESKTOP = "/home/oem/Desktop"
COVER = f"{DESKTOP}/MONOGRAPH_cover"

for name, src in [("_front", f"{COVER}/cover_front.png"), ("_back", f"{COVER}/cover_back_qr.png")]:
    img = Image.open(src).convert("RGB").resize((2480, 3508), Image.LANCZOS)
    img.save(f"/tmp/cover{name}.pdf")

w = PdfWriter()
w.append("/tmp/cover_front.pdf")
w.append(f"{DESKTOP}/MONOGRAPH_Centriole_Reset.pdf")
w.append("/tmp/cover_back.pdf")
with open(f"{DESKTOP}/MONOGRAPH_Book_Print_Complete.pdf", "wb") as f:
    w.write(f)
r = PdfReader(f"{DESKTOP}/MONOGRAPH_Book_Print_Complete.pdf")
print(f"Полная книга: {len(r.pages)} стр. (обложки + монография + QR)")
