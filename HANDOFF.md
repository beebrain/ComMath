# HANDOFF — ComMath (คณิตศาสตร์สำหรับคอมพิวเตอร์)

อัปเดต: 2026-08-06 · branch: `book-cleanup-2568` · commit ล่าสุด: `9b35a2d` (ยังไม่ commit งานรอบ ch3)

## รอบล่าสุด (2026-08-06) — กู้และปรับปรุงบทที่ 3
ไฟล์ `chapters/chapter03.tex` เสียจากการแก้ค้างกลางคัน (ไบต์ invalid UTF-8 2 จุด, เนื้อหาซ้ำ ~200 บรรทัด, `\end{solution}` เกิน) ทำให้ build ไม่ผ่าน — ซ่อมแล้วและปรับต่อดังนี้
- **ซ่อมโครง** ลบสำเนาซ้ำของ §ฟังก์ชัน/§ลำดับ-อนุกรม (เก็บฉบับที่เกริ่นนำเชิงรูปธรรม), ซ่อมย่อหน้าบทนำที่ถูกกลืน, ย้าย `\solhere` ออกจากโหมดคณิต (`$...\solhere$` ทำให้ `Missing $ inserted`)
- **เติมเนื้อหาที่ขาด** §3.1.1 โดเมน/เรนจ์/ความสัมพันธ์ผกผัน + §3.2.2 การประกอบความสัมพันธ์ ($S \circ R$, $R^n$) — เดิมสูตร $s(R)=R\cup R^{-1}$ และ $t(R)=R\cup R^2\cup\dots$ ใช้สัญลักษณ์ที่ไม่เคยนิยาม และแบบฝึกหัดถาม $\mathcal{D}(R),\mathcal{R}(R),R^{-1}$
- **แก้คณิตผิด** เฉลย $R_3=\{(1,1),(1,2),(2,2),(2,3),(1,3)\}$ บน $A=\{1,2,3,4\}$ เดิมตอบ "สะท้อน" ผิด (ขาด $(3,3),(4,4)$) · เพิ่มกรณี $r=1$ ของอนุกรมเรขาคณิต ($S_n=na_1$) และแก้เงื่อนไข $r>1/r<1$ เป็น $r\neq1$ · ย้าย $S_\infty$ เข้าบทนิยาม · เพิ่มหมายเหตุ mod ค่าลบ (คณิตให้ 1 แต่ C/C++/Java/JS ให้ $-3$)
- **สไตล์** วิธีทำทุกบล็อกกลับเป็น `align*` (เดิมถอยไปเป็นลิสต์ 1-2-3), ตัด `:` เชื่อมคำ, ตัด `\textbf` ในเนื้อเฉลย, หัวข้อ §3.5 เป็นไทยนำ + เขียนเนื้อหาให้ลึกขึ้น (เดิมหัวข้อละ 1 ย่อหน้า)
- **cross-ref** `\zlabel`→`\label` ทั้งบท (zref ไม่เคยถูกอ้าง และ `\autoref` ต้องใช้ `\label`), เพิ่ม `\label{sec:cartesian-product}` ใน ch2, ลบ `\label{sec:set-intro}` ซ้ำใน ch2, เพิ่ม `\autoref` ให้รูปทั้ง 3 รูป
- **autoref ภาษาไทย** เพิ่มใน `main.tex` — `\sectionautorefname/\subsectionautorefname/\subsubsectionautorefname` = "หัวข้อที่", `\figureautorefname` = "ภาพที่", `\tableautorefname` = "ตารางที่" (เดิมขึ้น "subsection 2.5.2" ภาษาอังกฤษ)
- **อ้างอิง** เพิ่ม `codd1970relational` (DOI 10.1145/362384.362685) ใน `references.bib` + `\cite` ย่อหน้าประวัติและ §3.5.1 (เดิมทั้งบทมี 0 cite)
- **ตัดศัพท์ "ความสัมพันธ์สมมูล" และ "ความสัมพันธ์อันดับเชิงส่วน (Poset)" ออกจากบทที่ 3 ทั้งหมด** (ตามคำสั่งผู้ใช้ — ไม่เอาหัวข้อสมมูล/คลาสเชิงสมมูล/Poset-Hasse/ตารางสรุปคุณสมบัติ) แก้ 5 จุด คือ ย่อหน้า §3.2.1, โจทย์+เฉลยตัวอย่าง mod 3 (เปลี่ยนเป็น "จงพิสูจน์ว่ามีคุณสมบัติสะท้อน สมมาตร และถ่ายทอด" คงตัวอย่างไว้), §3.5.2 และเฉลยแบบฝึกหัดข้อ 3 · ตรวจแล้วบทที่ 3 ไม่เหลือคำเหล่านี้เลย
- **แก้ label ซ้ำหมดทั้งเล่ม (multiply defined = 0)** — ch2 กล่อง `\begin{definition}[คอมพลีเมนต์]` ถูกวางซ้ำ 2 ที่ ตัวแรกวางผิดที่ (แทรกกลางหัวข้อเซตว่าง/เซตย่อย ไม่มีเกริ่นนำ) ลบตัวแรก เหลือตัวใน §คอมพลีเมนต์ ที่มีเกริ่นนำถูกต้อง · ch4 ลบ `\zlabel{sec:binary-system}` ที่ซ้ำตัวที่สอง (บรรทัด 79) · ch2 ลบ `\label{sec:set-intro}` ซ้ำ
- **ลบรูปกำพร้า 12 ไฟล์** `Figures/tikz/{19-reflexive,20-symmetric,21-antisymmetric,22-transitive,23-equivalence,24-partial-order-hasse}.tex` + `Figures/{19..24}-*.jpg` — ไม่มีบทไหนเรียกใช้ (ทุกไฟล์ track ใน git กู้คืนได้ด้วย `git checkout -- <path>`)
- **Build เขียว** `latexmk -xelatex main.tex` EXIT 0, **259 หน้า**, 0 error / 0 undefined ref-cite / 0 missing char / 0 overfull / 0 multiply defined

**ค้าง:** `tikztest.tex` (ไฟล์ทดสอบที่ root ไม่ได้ include ใน main.tex) ยังอ้างชื่อรูป 19–24 ที่ลบไปแล้ว ถ้าจะคอมไพล์ไฟล์นี้ต้องแก้หรือลบทิ้ง · `imagepromt.md`, `FIGURE_REVIEW.md`, `temp_render_ch3/` ยังมีชื่อรูปเหล่านี้อยู่ (เป็นเอกสาร/ที่เก็บชั่วคราว ไม่กระทบ build)

## งานที่กำลังทำ
Rework ตำรา ComMath (XeLaTeX) ให้เป็นสไตล์ตาม **prinmath.pdf** (หลักคณิตศาสตร์ ม.นเรศวร — ที่ book root; เอาแค่ **รูปแบบการนำเสนอ ห้ามเอาเนื้อหา**) และเปลี่ยน "วิธีทำ/เฉลย" ทุกอันจากบรรยาย/ลิสต์ 1-2-3 → **ขั้นตอนคณิตศาสตร์** (align/⇔ chain)

## สถานะ
- ✅ **thrm + proof เป็นกล่องแถบหัวเข้มเหมือนนิยาม** (2026-07-25): `mathstyle.sty` `\renewenvironment{thrm}` (แถบหัวน้ำเงิน thrmTitle "ทฤษฎีบท X.Y ชื่อ" รองรับ optional arg) + `\renewenvironment{proof}` (แถบหัวเทาเข้ม proofTitle "พิสูจน์" + ∎ ท้ายกล่อง) แทน `\tcolorboxenvironment` แบบแถบข้างเดิม — counter thrm ยังใช้ร่วมกับ ex/prop/rem/cor/warning (เลขต่อเนื่อง). เพิ่มสี `proofTitle=#566573`. Build 261pp เขียว.
- ✅ **prinmath style** ใช้แล้วทั้งเล่ม: `\linespread{1.5}` (เดิม 2.25), กล่องนิยามแถบหัวเข้ม "บทนิยาม X.Y ชื่อ" (ไม่มี `:`) ตัวนับ `defcnt` รันต่อกันต่อบท, นิยาม = เกริ่นก่อน→กล่องนิยามล้วน→สมบัติออกนอกกล่อง
- ✅ สมการมีเลข (`equation`) จัดกึ่งกลาง; `align*`/`\[` วิธีทำยังชิดซ้าย (fleqn)
- ✅ ch1 หัวข้อตัวเชื่อม/ตารางค่าความจริง เลิกใช้ 2 คอลัมน์ (minipage) → คอลัมน์เดียว
- **solsteps → math-steps: เสร็จครบทุกบท ✅** ch1..ch6 = 0 ทั้งหมด (แปลง ch3=32, ch5=48, ch6=38 ในรอบนี้)
- **Build เขียว:** `latexmk -xelatex main.tex` = EXIT 0, 251 หน้า, 0 undefined/multiply/missing-char (เหลือ overfull 1 อัน = ex statement ch3 เซตความสัมพันธ์ยาว ไม่ใช่ solution)

## next step
- solsteps → math-steps **เสร็จทั้งเล่มแล้ว** ไม่มีงานส่วนนี้เหลือ
- **ต้องให้ user รีวิว 4 จุดที่แก้ "เนื้อหาผิด" ตอนแปลง (ไม่ใช่แค่ format):**
  1. ch6 K-map 4 ตัวแปร `\sum(0,1,2,3,4,6,8,9,12,14)` — map เดิมไม่ตรงกับ minterm list (มี m10 แทน m12,m14) แก้ค่าในตาราง 2 แถว (wx=11, wx=10) ให้ตรง แล้วเฉลย `f = w'x' + xz' + x'y'` (ตรวจครอบคลุมครบแล้ว)
  2. ch6 "วงจรเลขคู่ 3-bit" — เดิมเฉลย even-parity `f=x⊕y⊕z` (ผิด 2 ชั้น: โจทย์ถาม "เลขคู่"=ค่าคู่ ไม่ใช่ parity, และสูตร parity ก็ผิดเครื่องหมาย) แก้เป็น `f=z'` (LSB=0)
  3. ch6 K-map 2 ตัวแปร `\sum(1,2,3)` — เดิมเฉลย `f=x+y'` (ผิด) แก้เป็น `f=x+y`
  4. ch6 K-map 2 ตัวแปร `xy+xy'+x'y'` — เดิมเฉลย `f=x'+x=1` (ผิด) แก้เป็น `f=x+y'`
- ~~ch5 ตัวอย่างซ้ำ~~ **แก้แล้ว:** ตัด ex "หาตัวผกผัน A=(2 1 1;0 1 1;1 0 1)" ตัวที่ 2 (อยู่ผิดที่ หลัง §สมบัติตัวผกผัน) ออก เหลือตัวแรกในหัวข้อการคำนวณ
- ~~overfull ch3~~ **แก้แล้ว:** ประโยคโจทย์ Poset ({1,2,3,4,6,12},|) ดึงเซต R 18 คู่ออกเป็น display `\begin{aligned}` หัก 2 บรรทัด → **overfull = 0 ทั้งเล่ม** แล้ว

## แหล่งความจริงเดียว
- เนื้อหา: `chapters/chapter01.tex`..`chapter06.tex` (ไฟล์ `_or` = หน้า มคอ./แผนการสอน อย่าแตะเนื้อ)
- สไตล์: `mathstyle.sty` (กล่องนิยาม+`\solhere`+solution env), `main.tex` (counters/equation-centering/theorem envs + `\exercisepart{}` = หัวข้อ "ส่วนที่ N"/"เฉลยส่วนที่ N" **กึ่งกลาง** แทน `\subsection*` เดิมที่เยื้อง 1.5cm + `\sectionbanner{title}` = แบนเนอร์ **ขึ้นหน้าใหม่+กึ่งกลาง+เข้า TOC (ไม่มีเลข)** ใช้กับหัว "แบบฝึกหัด"/"แบบฝึกหัดท้ายบท" (ch1-6) และ "เฉลยแบบฝึกหัด" (`\answerkeyhead`=alias) แทน `\section{...}` เดิม), `kkubee_edit_all.cls` (linespread/fleqn; `\titlespacing{\subsection}{1.5cm}...`; `\theenumii=\theenumi.\arabic{enumii}` = เลขย่อย 1.1)
- **เฉลยแบบ nested (ch2/4/6):** enumerate ชั้นนอกใช้ `[label={},ref=\arabic*,leftmargin=0pt,itemindent=0pt,labelwidth=0pt,labelsep=0pt]` เพื่อซ่อนเลขนอก "1." ให้ขึ้น "1.1" เลย (ต้องมี `ref=\arabic*` ไม่งั้น `\theenumi` ว่าง เลขกลายเป็น ".1"); ch1/3/5 เฉลยเป็น enumerate ชั้นเดียว ไม่ต้องแก้
- Template สไตล์: `STYLE_prinmath.md` · อ้างอิงต้นแบบ: `../prinmath.pdf` (รูปแบบเท่านั้น)

## เครื่องมือ / รันย่อ
- Build: `latexmk -xelatex -interaction=nonstopmode main.tex` (macOS ไม่มี `timeout`)
- นับงานเหลือ: `for f in chapters/chapter0[1-6].tex; do echo "$f $(grep -c 'begin{solsteps}' $f)"; done`
- ดูผลจริง: `pdftoppm -f <หน้า> -l <หน้า> -r 120 -png main.pdf out` แล้วเปิดรูป (เลขหน้า PDF ≠ เลขหน้าในเล่ม)

## กฎสำคัญ (พลาดบ่อย)
- **วิธีทำ/เฉลย = ขั้นตอนคณิต** (align จัดที่ `=`/`≡`/`⇔`) ไม่ใช่บรรยาย/1-2-3 · จบด้วย `\therefore ...` + `\solhere` (วาง ∎ บนบรรทัดคำตอบ)
- pattern ที่ใช้: ประเมิน→`≡ T/F`; ผลเซต/คำนวณ→`= {...}` + วงเล็บเหตุผลสั้น; พิสูจน์→`⇔ chain`; ตรวจสมบัติ→`R={...} ⇒ สมบัติ`; ตัวอย่างเชิงคำ→prose กระชับ
- นิยาม: กล่อง = นิยามล้วน (ห้ามยัดสมบัติ/กฎ) · axiom/นิยามหลายคำเก็บ enumerate ในกล่องได้
- ศัพท์: ไทยตัวหนา(อังกฤษ), เอกภพสัมพัทธ์=Universal Set, set-difference ใช้ `-` (ไม่ใช่ `\setminus`)
- ห้ามคัดลอกเนื้อหาจาก prinmath.pdf — เอาแค่รูปแบบ
- ไม่มี `\ref` ไป ex/thrm/def (อ้างแค่ tab/fig/ch/sec) — เปลี่ยน counter นิยามได้ปลอดภัย

## bug pattern
- **OneDrive ล็อกไฟล์ตอน build** → เกิด `main.bcf-SAVE-ERROR`/`main.bbl-SAVE-ERROR`, build พัง → ลบไฟล์ `-SAVE-ERROR` ก่อน rebuild (pause OneDrive ตอน compile จะกันได้)
- อักขระหลุด: U+2082(₂), U+060C(،), U+2423(␣), curly-quote → `grep -rnP '[\x{2080}-\x{209F}\x{0600}-\x{06FF}\x{2423}]'`
- env ไม่ balance (เช่น minipage) ทำ table float พัง "Not in outer par mode" → memory exceeded; เช็ค begin/end ต่อไฟล์
- `\c@defn` ชนแพ็กเกจอื่น → ใช้ชื่อ counter `defcnt`

## backup / memory
- git branch `book-cleanup-2568` (commit checkpoint เป็นระยะ)
- memory: `commath-rework-conventions`, `commath-solution-style` (โหลดอัตโนมัติทุก session)
