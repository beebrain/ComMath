# รายงานตรวจ Format (รอบที่ 2 — หลังปรับเนื้อหา)

- วันที่ตรวจ: 2026-06-13
- ไฟล์: `main.pdf` (**317 หน้า** physical) / log: `main.log` (compile ล่าสุด 2026-06-13 20:07)
- Engine: XeLaTeX | Class: `kkubee_edit_all.cls` | Main font: TH Sarabun New | `\linespread{2.25}`
- ขอบเขต: ตรวจ **format/compile cleanliness** เท่านั้น (ไม่ตรวจความถูกต้องของเนื้อหา/คณิตศาสตร์)
- วิธี: parse `main.log` ทั้งหมด + `pdftotext`/`pdftoppm` ตรวจหน้าต้องสงสัยด้วยภาพ (ch5 หัวข้อ applications + longtable แผนการสอน + หน้าที่ log flag) รวม ~20 หน้า
- หมายเหตุ offset: เลขหน้าที่พิมพ์ (Thai) = physical PDF index − 13 (ยืนยันแล้ว เช่น physical 250 = printed 237, physical 17 = printed 4)
- เทียบกับรอบก่อน: เดิม 321 หน้า → ปัจจุบัน 317 หน้า (ลดลง 4 หน้า สอดคล้องกับการตัด PageRank/Sobel/Gaussian/PCA ออกจาก ch5)

---

## เทียบกับรอบก่อน

| ปัญหาเดิม (รอบ 1) | ตำแหน่งเดิม | สถานะรอบนี้ | หลักฐาน |
|---|---|---|---|
| Overfull \hbox 58.49pt × 3 (longtable แผนการสอน) | `organize.tex` | **แก้แล้ว** | `organize.tex:63–65` ใส่ `\small` + `\setlength{\tabcolsep}{4pt}` + `{|c|p{4.3cm}|c|p{4.3cm}|c|}`; log ไม่มี Overfull เลย; ภาพ physical 17 ตารางพอดีกรอบ |
| Overfull \hbox 61.76pt (display `\det(A)` บรรทัดเดียว) | `chapter05.tex:823` (เดิม) | **แก้แล้ว** | ตอนนี้ใช้ `align*` 2 บรรทัด (`chapter05.tex:826–829`); log ไม่มี Overfull |
| Undefined reference `sec:logical-equivalence` | `chapter01.tex:85` ↔ `:447` (เดิม `\zlabel`) | **แก้แล้ว** | `chapter01.tex:447` เปลี่ยนเป็น `\label`; aux: `newlabel{sec:logical-equivalence}{{1.7}{27}}`; log ไม่มี undefined; PDF ไม่มี "??" |
| Orphan heading + ช่องว่างแนวตั้ง (ตัวอย่าง inverse) | physical 236 (printed 223) | **ยังอยู่ (เปลี่ยนรูป)** | `needspace` กันไม่ให้หัวข้อตกค้างเดี่ยว ๆ แล้ว แต่ทำให้เกิดช่องว่างท้ายหน้า ~30–40% เมื่อ block ตัวอย่างถูกดันทั้งก้อนไปหน้าใหม่ (ดูรายหน้า) — เป็น cosmetic |
| Empty bibliography × 5 | `\RefChapter` ท้ายแต่ละบท | **ยังอยู่** | log บรรทัด 2427/2586/2647/2713/2765; `\RefChapter` (cls:692) เรียก `\printbibliography[segment=...,heading=none]` ต่อบท แต่ไม่มี `\cite` ใน refsegment |
| Underfull \hbox badness สูง (34 จุด) | หลายหน้า | **ยังอยู่ (เท่าเดิม 34 จุด)** | ผลของ `\linespread{2.25}` + บรรทัดหัวบท/ย่อหน้าสั้น — cosmetic |
| Font shape `.../sc` undefined × 2 | small-caps fallback | **ยังอยู่** | log 2297/2337 — fallback อัตโนมัติ ไม่กระทบสายตา |
| `h`→`ht` float | LaTeX ปรับเอง | **ยังอยู่ (ปกติ)** | log 2231/2279/2287/2301–2315 — ไม่ใช่ error |
| Missing character (glyph) | — | **สะอาด (0)** | grep `Missing character` = 0 |
| Multiply-defined labels | — | **สะอาด (0)** | grep = 0 |

**ปัญหาใหม่ที่พบรอบนี้:** ไม่มี error/overfull ใหม่จากการตัด/จัดเรียง ch5. ตรวจยืนยันว่าเนื้อหาที่ลบ (PageRank/Sobel/Gaussian/PCA) เหลืออยู่เฉพาะใน `chapters/chapter05.tex.bak` (ไฟล์สำรอง ไม่ถูก compile) เท่านั้น ไม่มีใน `chapter05.tex` ที่ใช้จริง และไม่มี cross-reference ค้าง.

---

## สรุปภาพรวม

| รายการ | จำนวนรอบนี้ | รอบก่อน | หมายเหตุ |
|---|---|---|---|
| Overfull \hbox (> 15pt) | **0** | 4 | แก้หมดแล้ว (longtable + display det) |
| Overfull \hbox (ทั้งหมด) | **0** | 4 | — |
| Overfull \vbox | 0 | 0 | — |
| Underfull \hbox | 34 | 34 | badness 2200–10000 จาก linespread — cosmetic |
| Undefined references | **0** | 1 | `sec:logical-equivalence` แก้แล้ว |
| Citation undefined | 0 | 0 | — |
| Missing character (glyph) | **0** | 0 | สะอาด |
| Multiply-defined labels | **0** | 0 | สะอาด |
| Empty bibliography warnings | 5 | 5 | จาก `\RefChapter` ต่อบท (ดูข้อเสนอ) |
| หน้าที่มีช่องว่างแนวตั้งมาก (จาก needspace) | ≥ 3 (physical 236, 251, 254) | ≥ 1 | trade-off ของ `\needspace{3\baselineskip}` |
| Font `/sc` undefined | 2 | 2 | fallback |

**Verdict:** PDF อยู่ในสภาพ **"สะอาดมาก / พร้อมตีพิมพ์เชิง format"** — ปัญหา "ต้องแก้" รอบก่อนทั้ง 3 กลุ่ม (overfull longtable, overfull display det, undefined ref) **แก้หมดแล้ว**. ไม่มี Overfull เหลือเลย, ไม่มี missing glyph, ไม่มี undefined ref/label ซ้ำ. การตัด/จัดเรียง ch5 สะอาด ไม่มีปัญหาใหม่. ที่เหลือเป็น cosmetic ล้วน: (1) ช่องว่างท้ายหน้าจาก `needspace` 3 จุด (กลาง–ต่ำ), (2) บรรณานุกรมต่อบทว่าง 5 จุด (กลาง — เชิงนโยบาย), (3) Underfull จาก linespread (ต่ำ ทั้งเล่ม).

---

## ปัญหารายหน้า (Page-by-page)

> ตรวจด้วยภาพแล้วสะอาด ไม่ระบุไว้: ตารางแผนการสอน physical 18 (printed 5), Computer Graphics physical 250 (printed 237, ภาพที่ 29 TikZ พอดี textwidth), Hill Cipher physical 252 (printed 239), Adjacency physical 253 (printed 240), ML สรุป physical 255 (printed 242, §5.8 สรุปไหลต่อเนื่อง), หน้านิยาม inverse physical 236 ส่วนกล่อง tcolorbox (เขียว/ม่วง/เทา) พอดีกรอบ.

| Physical (printed) | ประเภทปัญหา | รายละเอียด | ความรุนแรง | วิธีแก้ที่แนะนำ |
|---|---|---|---|---|
| 236 (223) | ช่องว่างแนวตั้งท้ายหน้า (needspace) | หัวข้อ "ตัวอย่างที่ 5.48 จงหาตัวผกผันของ A=(1 2;3 4)" ถูก `\needspace{3\baselineskip}` ดันทั้งก้อนลงท้ายหน้า เหลือพื้นที่ว่างล่าง ~35%; วิธีทำไปอยู่หน้า 237 | กลาง | ยอมรับได้ (ดีกว่า orphan heading เดิม). ถ้าต้องการเต็มหน้า: ลด `\needspace` เป็น `2\baselineskip` ใน `main.tex:71`, หรือใส่ `\enlargethispage{2\baselineskip}` เฉพาะจุด |
| 251 (238) | ช่องว่างแนวตั้งท้ายหน้า (needspace) | จบ "ตัวอย่างที่ 5.70" แล้วขึ้น §5.7.2 Hill Cipher + "ตัวอย่างที่ 5.71" หัวข้อค้างท้ายหน้า วิธีทำไปหน้า 252 เหลือว่างล่าง ~40% | กลาง | เหมือนข้างบน — เป็น trade-off ของ needspace; ไม่กระทบความถูกต้อง |
| 254 (241) | ช่องว่างแนวตั้งท้ายหน้า (needspace) | "ตัวอย่างที่ 5.76 (โครงข่ายประสาทเทียมหนึ่งชั้น)" + ข้อมูล x,W,b ถูกจับคู่ค้างท้ายหน้า วิธีทำไปหน้า 255 เหลือว่างล่าง ~25% | ต่ำ–กลาง | ยอมรับได้; ถ้าจะลดช่องว่างใช้ `\enlargethispage` หรือลด needspace |
| ท้ายแต่ละบท ×5 (printed ≈ ท้ายบท 1–6) | Empty bibliography | `\RefChapter` (cls:692) เรียก `\printbibliography[segment=\therefsegment,heading=none]` แต่ไม่มี `\cite` ใน refsegment ของแต่ละบท → ขึ้นหัวข้อ "เอกสารอ้างอิง" (cls:687) แล้วเว้นว่าง (log 2427/2586/2647/2713/2765) | กลาง | ถ้าต้องการบรรณานุกรมต่อบท: ใส่ `\cite{...}`/`\nocite{...}` ในเนื้อบทให้อยู่ใน `\begin{refsegment}...\end{refsegment}`; ถ้าไม่ต้องการ: comment การเรียก `\printbibliography` ใน `\RefChapter` (cls:691–692) ออก (บรรณานุกรมรวมท้ายเล่ม `main.tex:221` ทำงานปกติแล้ว 7 entry) |
| หลายหน้า (ดู appendix) | Underfull \hbox badness 2200–10000 | บรรทัดยืดจาก `\linespread{2.25}` + บรรทัดหัว `\chapter*`/ย่อหน้าสั้น (เช่น log lines 23–25 ของหลายบท) | ต่ำ | ไม่ต้องแก้รายจุด (ดูข้อเสนอเชิงระบบ) |

---

## รายการ Overfull/Underfull (จาก log)

### Overfull
```
(ไม่มี — 0 รายการ ทั้ง \hbox และ \vbox)   ← เดิมรอบ 1 มี 4 รายการ แก้หมดแล้ว
```

### Underfull \hbox (รวม 34 จุด — ความรุนแรงต่ำ, ผลของ linespread; ไม่กระทบการอ่าน)
ตำแหน่งบรรทัด log (badness):
2204(10000), 2209(10000), 2219(10000), 2224(4995), 2246(10000), 2272(6876), 2327(10000), 2353(10000), 2375(2213), 2414(2932), 2420(3612), 2439(10000), 2461(10000), 2474(10000), 2483(10000), 2496(10000), 2503(4229), 2514(2662), 2524(10000), 2533(3108), 2548(10000), 2554(10000), 2565(3471), 2573(3460), 2598(10000), 2628(2846), 2640(10000), 2659(10000), 2695(3138), 2706(10000), 2727(10000), 2752(2671), 2758(2600), 2771(7796).
ส่วนใหญ่อยู่บรรทัด 23–25 ของหลายบท = บรรทัดหัว `\chapter*`/ย่อหน้าแรกภายใต้ spacing 2.25.

### Warning อื่น (ไม่ใช่ error)
```
LaTeX Warning: Empty bibliography on input line 190/197/204/211/218          (×5, จาก \RefChapter ต่อบท)
LaTeX Font Warning: Font shape `TU/THSarabunNew(0)/m/sc' undefined            (small caps fallback)
LaTeX Font Warning: Font shape `TU/THSarabunNew(0)/b/sc' undefined
LaTeX Warning: `h' float specifier changed to `ht'                            (×6, ปกติ)
LaTeX Warning: Unused global option(s)                                        (option class ที่ไม่ใช้)
Package fancyhdr Warning: \headheight is too small (12.0pt)                   (×8, cosmetic header)
Package caption Warning: Unused \captionsetup[sub] on input line 12           (subcaption ที่ไม่ได้ใช้)
LaTeX Font Warning: Size substitutions ... up to 2.25pt have occurred         (เลขเล็กในหัว fancyhdr cmr/cmm ขนาด 5.5)
Package rerunfilecheck Info: File `main.out' has not changed                  (ไม่ต้อง rerun — อ้างอิงนิ่งแล้ว)
```
> หมายเหตุ: log รอบนี้ **ไม่มี** "There were undefined references" และ **ไม่มี** "Label(s) may have changed" แล้ว → ไม่ต้อง rerun.

---

## ข้อเสนอเชิงระบบ

1. **`needspace` ช่องว่างท้ายหน้า (ลำดับสำคัญที่สุดที่เหลือ):** `\AtBeginEnvironment{ex}{\needspace{3\baselineskip}}` (main.tex:71) กันหัวข้อตัวอย่างตกค้างได้ดี แต่ภายใต้ `\linespread{2.25}` ค่า `3\baselineskip` ค่อนข้างใหญ่ ทำให้ block ตัวอย่างกระโดดทั้งก้อนไปหน้าใหม่บ่อย เหลือช่องว่างท้ายหน้า. แนะนำลองลดเป็น `2\baselineskip` แล้ว rebuild ดูว่าช่องว่าง physical 236/251/254 ลดลงโดยไม่กลับมา orphan. หรือคงไว้ (ยอมแลกช่องว่างกับการไม่มี orphan).
2. **บรรณานุกรมต่อบทว่าง 5 จุด:** ตัดสินใจเชิงนโยบาย — (ก) ถ้าต้องการ "เอกสารอ้างอิงท้ายบท" จริง ให้ `\cite`/`\nocite` ภายใน `refsegment` ของแต่ละบท; (ข) ถ้าใช้บรรณานุกรมรวมท้ายเล่มอย่างเดียว (ปัจจุบันมี 7 entry ที่ printed 290) ให้ comment `\printbibliography` ใน `\RefChapter` (cls:691–692) เพื่อไม่ให้หัวข้อ "เอกสารอ้างอิง" ว่างปรากฏ 5 จุด.
3. **ความสม่ำเสมอ `\zlabel` vs `\label`:** ยังมี `\zlabel` (zref) เหลืออยู่ 37 จุดใน ch01/03/04 ที่ "นิยามแต่ไม่ถูกอ้าง" (referenced 0 ครั้ง) — ไม่ทำให้เกิด error แต่เป็น dead label และทำให้ระบบ label ปนกัน. แนะนำเลือกระบบเดียวทั้งเล่ม: ถ้าไม่ได้ใช้ zref จริง ให้แทน `\zlabel`→`\label` ทั้งหมด (เหมือนที่ทำกับ `sec:logical-equivalence` แล้ว) เพื่อลดความสับสนในอนาคต.
4. **`\headheight` too small (×8):** fancyhdr เตือนหัวกระดาษ 12pt เล็กไป (ฟอนต์ไทยสูง). ไม่กระทบ output ปัจจุบัน แต่ถ้าจะเงียบ warning ให้เพิ่ม `\setlength{\headheight}{15pt}` (หรือ `\addtolength`) ใน preamble.
5. **`\captionsetup[sub]` ไม่ถูกใช้:** ถ้าไม่ใช้ subfigure/subcaption แล้ว สามารถลบบรรทัด captionsetup[sub] ออก (ลด warning 1 จุด) — ไม่เร่งด่วน.
6. **Underfull badness 10000 (34 จุด):** เป็นผลจาก `\linespread{2.25}` ของ class (มาตรฐานตำรา/วิทยานิพนธ์ไทย). มี `\emergencystretch=6em`, `\tolerance=2000`, `\hbadness=2000` ตั้งไว้แล้วใน main.tex:169–171 ซึ่งช่วยได้ระดับหนึ่ง. ไม่แนะนำแก้รายจุด.
7. **Small caps `/sc`:** TH Sarabun New ไม่มี shape `sc` — เกิดเมื่อมี `\textsc{}`/`scshape` (พบที่บรรณานุกรม biblatex และหัวข้อบางจุด). fallback ทำงานอยู่ ไม่เร่งด่วน; ถ้าต้องการความเป๊ะให้ `\DeclareFontShape` fallback หรือเลี่ยง small caps.

---

### หมายเหตุการตรวจด้วยภาพ (ยืนยันแล้ว รอบนี้)
- **ch5 หัวข้อ applications (จัดเรียงใหม่):** physical 250 (Graphics + ภาพที่ 29 TikZ การหมุน/ขยาย/เฉือน พอดี textwidth, caption + `\ref{fig:matrix-transformation}` ถูกต้อง) → 252 (Hill Cipher เข้ารหัส/ถอดรหัส 5.71/5.72 เมทริกซ์ไม่ล้นขอบ) → 253 (Adjacency 5.73/5.74) → 254–255 (ML: Linear Regression 5.75 ได้ β=(1,1); Neural Network 5.76 weighted sum→ReLU→กล่องผลลัพธ์). **ลำดับตัวอย่างไหลต่อเนื่อง 5.69–5.76 ไม่มีเลขขาด** จากการลบเนื้อหา.
- **longtable แผนการสอน (physical 17–18):** ตาราง 5 คอลัมน์อยู่ในกรอบ ไม่ล้น margin หลังใส่ `\small`+tabcolsep 4pt+p{4.3cm}.
- **เนื้อหาที่ลบ (PageRank/Sobel/Gaussian/PCA):** ไม่มีใน PDF/`chapter05.tex` ที่ใช้จริง — เหลือเฉพาะ `chapter05.tex.bak` (สำรอง, ไม่ compile). ไม่มี cross-reference ค้าง, ไม่มีหน้าครึ่งว่างจากการลบ.
- **det(A) display:** ใช้ `align*` 2 บรรทัดแล้ว (chapter05.tex:826–829) ไม่ overfull.
