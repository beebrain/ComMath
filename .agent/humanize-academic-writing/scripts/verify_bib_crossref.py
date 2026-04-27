#!/usr/bin/env python3
"""Verify DOIs in a .bib file against Crossref (best-effort metadata check)."""
from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ENTRY_START = re.compile(r"^@(\w+)\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
DOI_LINE = re.compile(r"doi\s*=\s*\{([^}]+)\}", re.IGNORECASE)


def split_entries(text: str) -> list[tuple[str, str, str]]:
    """Return list of (entry_type, cite_key, block_text)."""
    matches = list(ENTRY_START.finditer(text))
    out = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out.append((m.group(1), m.group(2), text[m.start() : end]))
    return out


def normalize_doi(raw: str) -> str:
    s = raw.strip()
    s = s.replace(r"\_", "_")
    return s


def crossref_work(doi: str, timeout: int = 20) -> tuple[int, dict | None, str]:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "NewBookBibVerify/1.0 (mailto:academic; https://github.com)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode())
            return resp.status, data, ""
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode()[:500]
        except Exception:
            pass
        return e.code, None, body
    except Exception as e:
        return -1, None, str(e)


def main() -> int:
    bib_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("references.bib")
    text = bib_path.read_text(encoding="utf-8", errors="replace")
    entries = split_entries(text)
    doi_ok = []
    doi_fail = []
    no_doi = []

    for et, key, block in entries:
        dm = DOI_LINE.search(block)
        if not dm:
            no_doi.append((key, et))
            continue
        doi = normalize_doi(dm.group(1))
        status, data, err = crossref_work(doi)
        if status == 200 and data and "message" in data:
            msg = data["message"]
            title = (msg.get("title") or [""])[0]
            year = None
            if "published-print" in msg:
                parts = msg["published-print"].get("date-parts", [[]])[0]
                if parts:
                    year = parts[0]
            elif "published-online" in msg:
                parts = msg["published-online"].get("date-parts", [[]])[0]
                if parts:
                    year = parts[0]
            elif "issued" in msg:
                parts = msg["issued"].get("date-parts", [[]])[0]
                if parts:
                    year = parts[0]
            doi_ok.append((key, doi, title[:80] + ("…" if len(title) > 80 else ""), year))
        else:
            doi_fail.append((key, doi, status, err[:200]))

    print("=== DOI verification via Crossref ===")
    print(f"OK: {len(doi_ok)}")
    print(f"FAIL: {len(doi_fail)}")
    print(f"No DOI in entry: {len(no_doi)}")
    if doi_fail:
        print("\n-- FAILED DOIs --")
        for row in doi_fail:
            print(row)
    print("\n-- Entries without doi = {...} field --")
    for key, et in no_doi:
        print(f"  {key} ({et})")
    return 0 if not doi_fail else 1


if __name__ == "__main__":
    sys.exit(main())
