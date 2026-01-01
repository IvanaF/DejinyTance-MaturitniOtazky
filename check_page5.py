#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check page 5 format."""

import sys
import io
from pypdf import PdfReader

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

reader = PdfReader("Dějiny tance a baletu.pdf")
page = reader.pages[4]  # 0-indexed, so page 4 = page 5
text = page.extract_text()

print("Raw text from page 5:")
print(repr(text[:500]))
print("\n" + "="*60 + "\n")
print("Formatted:")
lines = text.split('\n')
for i, line in enumerate(lines[:15]):
    print(f"Line {i}: {repr(line)}")

