# HANDOFF — ComMath (คณิตศาสตร์สำหรับคอมพิวเตอร์)

อัปเดต: 2026-07-24 · branch: `book-cleanup-2568` · commit ล่าสุด: `9b35a2d`

## งานที่กำลังทำ
Rework ตำรา ComMath (XeLaTeX) ให้เป็นสไตล์ตาม **prinmath.pdf** (หลักคณิตศาสตร์ ม.นเรศวร — ที่ book root; เอาแค่ **รูปแบบการนำเสนอ ห้ามเอาเนื้อหา**) และเปลี่ยน "วิธีทำ/เฉลย" ทุกอันจากบรรยาย/ลิสต์ 1-2-3 → **ขั้นตอนคณิตศาสตร์** (align/⇔ chain)

## สถานะ
- ✅ **prinmath style** ใช้แล้วทั้งเล่ม: `\linespread{1.5}` (เดิม 2.25), กล่องนิยามแถบหัวเข้ม "บทนิยาม X.Y ชื่อ" (ไม่มี `:`) ตัวนับ `defcnt` รันต่อกันต่อบท, นิยาม = เกริ่นก่อน→กล่องนิยามล้วน→สมบัติออกนอกกล่อง
- ✅ สมการมีเลข (`equation`) จัดกึ่งกลาง; `align*`/`\[` วิธีทำยังชิดซ้าย (fleqn)
- ✅ ch1 หัวข้อตัวเชื่อม/ตารางค่าความจริง เลิกใช้ 2 คอลัมน์ (minipage) → คอลัมน์เดียว
- **solsteps → math-steps:** ch1 ✅(0) · ch2 ✅(0) · ch4 ✅(0) · **ch3 กำลังทำ 13/45 (เหลือ 32)** · ch5 ⬜(48) · ch6 ⬜(38)
- **Build เขียว:** `latexmk -xelatex main.tex` = EXIT 0, 264 หน้า, 0 undefined/multiply/missing-char

## next step
1. ทำ **ch3 solsteps ที่เหลือ 32** อันต่อ (เริ่มจากบรรทัดที่ `grep -n 'begin{solsteps}' chapters/chapter03.tex` แรกสุด) แล้ว **ch5 (48), ch6 (38)**
2. หลังทุกชุด: `latexmk -xelatex -interaction=nonstopmode main.tex` ต้อง EXIT 0; เช็ค `grep -c 'begin{solsteps}'` ต้องลดลง

## แหล่งความจริงเดียว
- เนื้อหา: `chapters/chapter01.tex`..`chapter06.tex` (ไฟล์ `_or` = หน้า มคอ./แผนการสอน อย่าแตะเนื้อ)
- สไตล์: `mathstyle.sty` (กล่องนิยาม+`\solhere`+solution env), `main.tex` (counters/equation-centering/theorem envs), `kkubee_edit_all.cls` (linespread/fleqn)
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
