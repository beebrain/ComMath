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
# lookbehind กันไม่ให้เริ่มจับกลางคำ เพราะภาษาไทยไม่มีช่องว่างคั่นคำ
# ถ้าไม่มีบรรทัดนี้จะได้ขยะอย่าง "รกะที่พบบ่อย เรียกว่าการยืนยันเงื่อนไขตาม"
PAIR = re.compile(
    r"(?<![\u0E00-\u0E7F])"
    r"([\u0E00-\u0E7F][\u0E00-\u0E7F\s]{1,40}?)\s*\(([A-Za-z][A-Za-z0-9\s\-'/,\.]{1,40})\)"
)
STRIP_CMD = re.compile(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?")
# คำเชื่อมที่มักติดมาหน้าศัพท์จริง ตัดทิ้งก่อนบันทึก
LEAD = re.compile(
    r"^(และ|หรือ|คือ|เป็น|ที่|ของ|ใน|จึง|แต่|ตาม|เรียกว่า|ได้แก่|กับ|โดย|ให้|มี|ทั้ง"
    r"|ส่วน|จาก|เมื่อ|ถ้า|ซึ่ง|นั่นคือ|ยัง|ก็|จะ|ต้อง|กล่าวคือ|พร้อม|อีก)\s*"
)


def norm_en(s):
    return re.sub(r"\s+", " ", s).strip().lower().rstrip(".,")


def norm_th(s):
    s = re.sub(r"\s+", " ", s).strip()
    while True:
        stripped = LEAD.sub("", s)
        if stripped == s:
            return s
        s = stripped


def canonical(variants):
    """คืน (คำที่ถือเป็นศัพท์จริง, ขัดกันจริงหรือไม่)

    ศัพท์อยู่ท้ายวลีเสมอ เพราะเขียนติดหน้าวงเล็บอังกฤษ ส่วนที่ต่างกันจึงเป็น
    คำแวดล้อมที่นำหน้ามา ถ้าทุกตัวแปรลงท้ายเหมือนกัน แปลว่าเป็นศัพท์เดียวกัน
    """
    squeezed = [re.sub(r"\s+", "", t) for t in variants]
    shortest = min(squeezed, key=len)
    n = 0
    while n < len(shortest) and all(s[-(n + 1)] == shortest[-(n + 1)] for s in squeezed):
        n += 1
    suffix = shortest[-n:] if n else ""
    if len(suffix) >= 4:
        # เลือกตัวแปรที่สั้นที่สุดซึ่งลงท้ายด้วยส่วนท้ายร่วม
        pick = min((t for t in variants if re.sub(r"\s+", "", t).endswith(suffix)), key=len)
        return pick, False
    return min(variants, key=len), True


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


# ตัวดำเนินการ ไม่ใช่ศัพท์ที่ต้องบัญญัติ จึงไม่นับเป็นความขัดแย้ง
OPERATORS = {"and", "or", "not", "xor", "if", "iff"}


def main():
    show_all = "--all" in sys.argv
    terms = collect()

    conflicts = {}
    for en, variants in terms.items():
        if len(variants) < 2 or en in OPERATORS:
            continue
        if canonical(variants)[1]:
            conflicts[en] = variants

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
            th = canonical(terms[en])[0]
            n = sum(len(v) for v in terms[en].values())
            print(f"{n:3d}x  {en:<34} {th}")


if __name__ == "__main__":
    main()
