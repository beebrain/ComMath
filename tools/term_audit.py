#!/usr/bin/env python3
"""ตรวจความสม่ำเสมอของศัพท์ทั้งเล่ม

เล่มนี้ไม่มี glossary จึงถือว่า "คำแปลไทยที่ใช้คู่กับศัพท์อังกฤษตัวเดียวกัน
ต้องเหมือนกันทุกจุด" ตัวสคริปต์ดึงคู่ ไทย (English) จากทุกบท แล้วรายงาน
ศัพท์อังกฤษที่ถูกแปลไทยไม่ตรงกัน

    python3 tools/term_audit.py            # เฉพาะที่ขัดกัน
    python3 tools/term_audit.py --all      # ทุกคู่ที่พบ
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

CHAPTERS = sorted(Path("chapters").glob("chapter0[1-6].tex"))

# ไทยติดกันอย่างน้อย 2 ตัว ตามด้วยวงเล็บอังกฤษ  เช่น  ตัวดำเนินการ (operator)
PAIR = re.compile(r"([\u0E00-\u0E7F][\u0E00-\u0E7F\s]{1,40}?)\s*\(([A-Za-z][A-Za-z0-9\s\-'/,\.]{1,40})\)")
STRIP_CMD = re.compile(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?")


def norm_en(s):
    return re.sub(r"\s+", " ", s).strip().lower().rstrip(".,")


def norm_th(s):
    return re.sub(r"\s+", " ", s).strip()


def collect():
    """en -> {th -> [(chapter, line)]}"""
    terms = defaultdict(lambda: defaultdict(list))
    for f in CHAPTERS:
        ch = f.stem.replace("chapter", "ch")
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("%"):
                continue
            clean = STRIP_CMD.sub(" ", line).replace("{", " ").replace("}", " ")
            for th, en in PAIR.findall(clean):
                th = norm_th(th)
                # คำไทยยาวเกิน 6 คำมักเป็นวลี ไม่ใช่ศัพท์
                if len(th) < 2 or th.count(" ") > 5:
                    continue
                terms[norm_en(en)][th].append(f"{ch}:{n}")
    return terms


def main():
    show_all = "--all" in sys.argv
    terms = collect()
    conflicts = {en: v for en, v in terms.items() if len(v) > 1}

    print(f"พบศัพท์อังกฤษ {len(terms)} คำ  ขัดกัน {len(conflicts)} คำ\n")
    for en in sorted(conflicts):
        print(f"[{en}]")
        for th, locs in sorted(terms[en].items(), key=lambda kv: -len(kv[1])):
            print(f"   {len(locs):2d}x  {th:<28} {' '.join(locs[:6])}")
        print()

    if show_all:
        print("=" * 60)
        print("ศัพท์ที่ใช้ตรงกันทุกจุด\n")
        for en in sorted(terms):
            if en in conflicts:
                continue
            (th, locs), = terms[en].items()
            print(f"{len(locs):3d}x  {en:<34} {th}")


if __name__ == "__main__":
    main()
