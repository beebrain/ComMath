#!/usr/bin/env python3
"""ตรวจว่าเลขเฉลยตรงกับเลขโจทย์ทุกข้อ

บั๊กที่สคริปต์นี้จับ คือบล็อกเฉลยที่ตั้ง \\setcounter{enumi} เอง แล้วตั้งตามลำดับ
"บล็อกเฉลย" แทนที่จะตั้งตามเลข "โจทย์" ทำให้เลขเฉลยเหลื่อมไปทั้งชุด
ความผิดพลาดนี้มองด้วยตาไม่เห็น เพราะไฟล์ .tex ดูเรียบร้อยดี ปรากฏเฉพาะตอนเรียงพิมพ์

คืนค่า exit 1 เมื่อพบจุดที่ไม่ตรง

    python3 tools/check_answers.py                 # ทุกบท
    python3 tools/check_answers.py chapters/chapter02.tex
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def strip_comments(text):
    return re.sub(r"(?<!\\)%.*", "", text)


def count_items(block):
    """นับ \\item เฉพาะชั้นบนสุดของบล็อก ไม่นับ \\item ของ list ที่ซ้อนอยู่ข้างใน"""
    depth, n = 0, 0
    for tok in re.finditer(r"\\begin\{(enumerate|itemize|description)\}|"
                           r"\\end\{(enumerate|itemize|description)\}|"
                           r"\\item\b(?!\s*\[)", block):
        if tok.group(1):
            depth += 1
        elif tok.group(2):
            depth -= 1
        elif depth == 0:
            n += 1
    return n


def top_level_blocks(text):
    """คืนเนื้อของ \\item ชั้นบนสุดแต่ละข้อ ตามลำดับที่ปรากฏ พร้อมค่า setcounter ที่พบ"""
    out, depth, cur, start = [], 0, None, 0
    for tok in re.finditer(r"\\begin\{(enumerate|itemize|description)\}(\[[^\]]*\])?|"
                           r"\\end\{(enumerate|itemize|description)\}|"
                           r"\\item\b(?!\s*\[)|"
                           r"\\setcounter\{enumi\}\{(\d+)\}", text):
        if tok.group(4) is not None and depth == 1:
            out.append(("set", int(tok.group(4))))
            continue
        if tok.group(1):
            depth += 1
            continue
        if tok.group(3):
            if depth == 1 and cur is not None:
                out.append(("item", text[start:tok.start()]))
                cur = None
            depth -= 1
            continue
        if depth == 1:
            if cur is not None:
                out.append(("item", text[start:tok.start()]))
            cur, start = True, tok.end()
    return out


def check(path):
    text = strip_comments(path.read_text(encoding="utf-8"))
    if r"\answerkeyhead" not in text:
        return None

    body, key = text.split(r"\answerkeyhead", 1)
    key = re.split(r"\\QAChapter|\\sheetChapter|\\sectionbanner", key)[0]

    exercises = [count_items(m.group(1)) for m in
                 re.finditer(r"\\begin\{exercise\}(.*?)\\end\{exercise\}", body, re.S)]

    answers, n = [], 0
    for kind, val in top_level_blocks(key):
        if kind == "set":
            n = val
        else:
            n += 1
            answers.append((n, count_items(val)))

    bad = []
    for num, subs in answers:
        want = exercises[num - 1] if 1 <= num <= len(exercises) else None
        if want is None or subs != want:
            bad.append((num, subs, want))
    missing = sorted(set(range(1, len(exercises) + 1)) - {n for n, _ in answers})

    print(f"{path.name}  โจทย์ {len(exercises)} ข้อ · เฉลย {len(answers)} ข้อ", end="")
    if not bad and not missing:
        print("  ตรงครบ")
        return True
    print()
    for num, subs, want in bad:
        if want is None:
            print(f"   XX เฉลยข้อ {num} ไม่มีโจทย์ข้อนี้ (โจทย์มีถึงข้อ {len(exercises)} เท่านั้น)")
        else:
            print(f"   XX ข้อ {num} เฉลยมี {subs} ข้อย่อย แต่โจทย์มี {want} ข้อย่อย")
    if missing:
        print(f"   XX ไม่มีเฉลย ข้อ {', '.join(map(str, missing))}")
    return False


def main():
    args = sys.argv[1:]
    files = [Path(a) for a in args] or sorted((ROOT / "chapters").glob("chapter0[1-9].tex"))
    ok = True
    for f in files:
        if check(f) is False:
            ok = False
    if not ok:
        print("\nพบเลขเฉลยไม่ตรงกับเลขโจทย์ แก้ก่อน commit")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
