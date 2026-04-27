#!/usr/bin/env python3
"""
Rough prose metrics for Thai (and mixed) LaTeX chapters.
Strips common LaTeX noise, then flags long run-on blocks (humanize-academic-writing helper).

Usage:
  python analyze_tex_thai.py path/to/chapter.tex
  python analyze_tex_thai.py path/to/chapter.tex --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def strip_latex_noise(text: str) -> str:
    text = re.sub(r"%.*?$", " ", text, flags=re.MULTILINE)
    # Remove \index{...}, \cite{...}, \label{...}
    text = re.sub(r"\\(index|cite|label|ref|pageref)\s*\{[^}]*\}", " ", text)
    # Remove environments (keep inner text loosely)
    text = re.sub(r"\\begin\{[^}]+\}.*?\\end\{[^}]+\}", " ", text, flags=re.DOTALL)
    # Remove remaining commands with braced args (one pass, non-nested)
    for _ in range(4):
        text = re.sub(r"\\[a-zA-Z@]+\*?(\[[^\]]*\])?\{[^{}]*\}", " ", text)
    text = re.sub(r"\\[a-zA-Z@]+\*?(\[[^\]]*\])?", " ", text)
    text = re.sub(r"\$\$?[^$]+\$\$?", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_prose_blocks(text: str) -> list[str]:
    parts = re.split(r"\n\s*\n", text)
    return [p.strip() for p in parts if p.strip() and not p.strip().startswith("%")]


def thai_sentence_splits(s: str) -> list[str]:
    """Split on Thai/English sentence boundaries (heuristic)."""
    chunks = re.split(r"(?<=[\.!\?])\s+", s)
    return [c.strip() for c in chunks if c.strip()]


def analyze_block(block: str) -> dict:
    sents = thai_sentence_splits(block)
    lens = [len(x) for x in sents]
    n = len(lens)
    avg = sum(lens) / n if n else 0
    var = 0.0
    if n > 1:
        var = sum((x - avg) ** 2 for x in lens) / (n - 1)
    std = var**0.5
    ratio = (std / avg) if avg else 0.0
    return {
        "chars": len(block),
        "sentence_count": n,
        "avg_sentence_chars": round(avg, 1),
        "sentence_length_std": round(std, 1),
        "burstiness_ratio": round(ratio, 2),
        "flag_long_block": len(block) > 520,
        "flag_uniform": n >= 4 and ratio < 0.25,
    }


def split_tex_sections(raw: str) -> list[tuple[str, str]]:
    """Split on \\section / \\subsection; return (heading, body) pairs."""
    parts = re.split(r"(?=\\(?:sub)*section\*?\{)", raw)
    out: list[tuple[str, str]] = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        m = re.match(r"(\\(?:sub)*section\*?\{[^}]+\})", p)
        if m:
            head = m.group(1)[:80]
            body = p[m.end() :].strip()
        else:
            head = "(preamble)"
            body = p
        out.append((head, body))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Analyze Thai LaTeX chapter prose (heuristic).")
    ap.add_argument("tex_path", type=Path)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    raw = args.tex_path.read_text(encoding="utf-8", errors="replace")
    sections = split_tex_sections(raw)
    results = []
    for i, (head, body) in enumerate(sections):
        cleaned = strip_latex_noise(body)
        if len(cleaned) < 40:
            continue
        m = analyze_block(cleaned)
        m["section_index"] = i + 1
        m["heading"] = head
        m["preview"] = cleaned[:140].replace("\n", " ") + ("…" if len(cleaned) > 140 else "")
        results.append(m)

    summary = {
        "file": str(args.tex_path),
        "sections_analyzed": len(results),
        "blocks": results,
        "notes": [
            "burstiness_ratio: higher usually means more varied sentence lengths (good).",
            "flag_long_block: consider splitting for readability.",
            "English ai_detector.py is tuned for English; use it for English abstracts only.",
        ],
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass
        print(f"File: {args.tex_path}")
        print(f"Sections with prose: {len(results)}\n")
        for r in results:
            tags = []
            if r["flag_long_block"]:
                tags.append("LONG")
            if r["flag_uniform"]:
                tags.append("UNIFORM?")
            tag_s = "/".join(tags) if tags else "ok"
            print(f"[{r['section_index']}] {tag_s} | chars={r['chars']} sents~={r['sentence_count']} burst={r['burstiness_ratio']}")
            print(f"    {r['heading']}")
            if tags:
                print(f"    {r['preview']}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
