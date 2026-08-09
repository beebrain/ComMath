#!/usr/bin/env python3
"""ตรวจกฎ ทุกหัวข้อต้องมีร้อยแก้วเกริ่นนำก่อนขึ้นกล่องหรือรายการ

ห้ามขึ้น section หรือ subsection แล้วเข้า definition, ex, table, figure,
enumerate หรือสมการทันที เพราะผู้เรียนที่อ่านเองจะไม่รู้ว่ากล่องนั้นตอบคำถามอะไร

ตรวจเฉพาะหัวข้อเนื้อหา ไม่รวม section* ซึ่งเป็นหัวข้อวัตถุประสงค์และคำชี้แจง
ในใบงาน ที่ตามด้วยรายการข้อโดยธรรมชาติ

    python3 tools/check_intro.py            # รายงานจุดที่ผิดกฎ
    python3 tools/check_intro.py --min 300  # ปรับเกณฑ์ความยาวเกริ่นนำขั้นต่ำ

คืนค่า exit 1 เมื่อพบจุดที่ไม่มีเกริ่นนำเลย เพื่อใช้เป็นด่านก่อน commit ได้
"""
import pathlib
import re
import sys

HEAD = re.compile(r"^\\(?:sub)*section\{")
SKIP = re.compile(r"^\\(label|index|zlabel)\{|^\s*$|^%")
BLOCK = re.compile(
    r"^\\begin\{(definition|ex|thrm|prop|rem|law|principle|table|figure"
    r"|enumerate|itemize|align|equation|exercise|warning|cor)\}|^\\\["
)


def scan(min_chars):
    missing, thin = [], []
    for f in sorted(pathlib.Path("chapters").glob("chapter0[1-6].tex")):
        lines = f.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines):
            if not HEAD.match(line):
                continue
            j = i + 1
            while j < len(lines) and SKIP.match(lines[j]):
                j += 1
            if j >= len(lines):
                continue
            if BLOCK.match(lines[j]):
                missing.append((f.name, i + 1, line.strip()))
                continue
            length, k = 0, j
            while k < len(lines) and not BLOCK.match(lines[k]) and not HEAD.match(lines[k]):
                length += len(lines[k].strip())
                k += 1
            if length < min_chars:
                thin.append((f.name, i + 1, line.strip(), length))
    return missing, thin


def main():
    min_chars = 200
    if "--min" in sys.argv:
        min_chars = int(sys.argv[sys.argv.index("--min") + 1])

    missing, thin = scan(min_chars)

    print("ไม่มีเกริ่นนำเลย ขึ้นหัวข้อแล้วเข้ากล่องทันที")
    for name, ln, head in missing:
        print(f"   {name}:{ln}  {head[:70]}")
    print(f"   รวม {len(missing)} จุด\n")

    print(f"มีเกริ่นนำแต่สั้นกว่า {min_chars} ตัวอักษร")
    for name, ln, head, n in thin:
        print(f"   {name}:{ln}  ({n} ตัวอักษร)  {head[:60]}")
    print(f"   รวม {len(thin)} จุด")

    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
