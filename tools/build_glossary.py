#!/usr/bin/env python3
"""สร้าง glossary.tsv จากตัวเล่มจริง เพื่อใช้เป็นฐานศัพท์เดียวกันทั้งเล่ม

ดึงคู่ ``ไทย (English)`` ที่เขียนไว้ในบททั้งหกด้วยตัวสกัดของ tools/term_audit.py
แล้วรวมกับคำตัดสินเดิมที่บันทึกไว้แล้วใน glossary.tsv โดยไม่เขียนทับ

    python3 tools/build_glossary.py

คอลัมน์
    english        ศัพท์อังกฤษที่ปรากฏในวงเล็บ
    thai_used      คำไทยที่ใช้จริง (เลือกคำที่สั้นที่สุด เพราะคำยาวมักเป็นวลีที่จับติดมา)
    orst_official  คำของราชบัณฑิตยสภา เติมด้วยมือจาก skill orst-lookup
    chapters       บทที่ปรากฏ
    decision       adopt = ใช้ตามนี้ · keep = จงใจต่างจากราชบัณฑิต · escalate = ต้องให้ผู้เขียนตัดสิน
    notes          เหตุผล โดยเฉพาะกรณี keep และ escalate
"""
import csv
import importlib.util
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
GLOSSARY = HERE.parent / "glossary.tsv"


def load_audit():
    spec = importlib.util.spec_from_file_location("term_audit", HERE / "term_audit.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read_decisions():
    if not GLOSSARY.exists():
        return {}
    with GLOSSARY.open(encoding="utf-8") as fh:
        return {
            r["english"].strip().lower(): r
            for r in csv.DictReader(fh, delimiter="\t")
            if r.get("english")
        }


def main():
    terms = load_audit().collect()
    prev = read_decisions()

    rows, conflicts = [], 0
    for en in sorted(terms):
        variants = terms[en]
        # คำที่สั้นที่สุดคือศัพท์จริง ตัวที่ยาวกว่ามักเป็นวลีที่ครอบศัพท์นั้นอยู่
        canonical = min(variants, key=len)
        chapters = sorted({loc.split(":")[0] for locs in variants.values() for loc in locs})

        # เทียบโดยตัดช่องว่างออกก่อน เพราะ "วิธี การกำจัดแบบเกาส์" กับ
        # "วิธีการกำจัดแบบเกาส์" เป็นคำเดียวกัน ต่างแค่การเว้นวรรค
        squeeze = lambda t: t.replace(" ", "")
        core = squeeze(canonical)
        real_conflict = not all(core in squeeze(th) for th in variants)
        decision = "escalate" if real_conflict else "adopt"
        notes = ""
        if real_conflict:
            conflicts += 1
            notes = "ขัดกัน " + " / ".join(sorted(variants, key=len))

        old = prev.get(en)
        if old:
            canonical = old.get("thai_used") or canonical
            decision = old.get("decision") or decision
            notes = old.get("notes") or notes
            orst = old.get("orst_official") or "—"
        else:
            orst = "—"

        rows.append([en, canonical, orst, ",".join(chapters), decision, notes])

    with GLOSSARY.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["english", "thai_used", "orst_official", "chapters", "decision", "notes"])
        w.writerows(rows)

    kept = sum(1 for r in rows if r[0] in prev)
    print(f"ศัพท์ {len(rows)} คำ · ยังขัดกัน {conflicts} คำ · คงคำตัดสินเดิม {kept} คำ")


if __name__ == "__main__":
    main()
