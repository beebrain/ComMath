# แผน Slide + Worksheet + การบ้าน — Chapter 1 สัปดาห์ที่ 3

> **อนุมัติแล้ว:** Worksheet ระดับง่าย-กลาง (5 ข้อ) | การบ้าน 5 ข้อ (ข้อ 5 บังคับ)

## 🎯 เป้าหมายการเรียนรู้
1. ใช้ตัวเชื่อมเพิ่มเติม (XOR, NAND, NOR) และเข้าใจ Universal Gate
2. แปลงประโยคที่มีตัวบ่งปริมาณ $\forall, \exists$ เป็นสัญลักษณ์
3. ประยุกต์กฎการอนุมาน (Modus Ponens, Tollens, HS, DS) และตรวจ fallacy
4. พิสูจน์ความสมเหตุสมผลด้วย truth table

---

## 📊 โครงสร้าง Slide (รวม ~28 frames)

### Frame 1–3: ปก + ทบทวนสัปดาห์ 2 + วัตถุประสงค์ (มีอยู่แล้ว ✓)

### Section 1: ตัวเชื่อมเพิ่มเติม (3 frames)
1. **XOR** ($\oplus$) — นิยาม + truth table + ตัวอย่าง Half-Adder
2. **NAND ($\uparrow$) / NOR ($\downarrow$)** — นิยาม + truth table
3. **➕ Universal Gate** — สร้าง NOT, AND, OR จาก NAND (สูตร + ตัวอย่าง)

### Section 2: ประพจน์เปิดและตัวบ่งปริมาณ (3 frames)
1. **นิยาม $\forall x P(x)$, $\exists x P(x)$** + ตัวอย่างเอกภพ
2. **ตัวอย่างหาค่าความจริง** — เอกภพจำนวนจริง, เอกภพเซต
3. **➕ นิเสธของตัวบ่งปริมาณ** + การยกตัวอย่างค้าน

### Section 3: กฎการอนุมาน (8 frames)
1. **บทนำ inference rules** — นิยาม + ความสำคัญ
2. **Modus Ponens** — truth table proof ✓
3. **ตัวอย่าง Modus Ponens** ✓
4. **Modus Tollens** — truth table proof ✓
5. **ตัวอย่าง Modus Tollens** ✓
6. **➕ Hypothetical Syllogism (HS)** — truth table proof (ใหม่)
7. **➕ Disjunctive Syllogism (DS)** — truth table proof (ใหม่)
8. **➕ Fallacy: Affirming the Consequent / Denying the Antecedent** (alertblock)

### Section 4: กรณีศึกษา (4 frames, มีอยู่แล้ว ✓)
- ระบบสินเชื่อ + ทฤษฎีบท $p \to q \equiv \neg p \lor q$

### Section 5: กิจกรรม + สรุป + การบ้าน (5 frames)
1. วิธีทำกิจกรรม
2. **➕ Worksheet ในห้อง** (5 ข้อ — ดูรายละเอียดด้านล่าง)
3. **สรุปสัปดาห์ที่ 3** (4 กรอบหัวข้อหลัก)
4. **➕ การบ้าน 5 ข้อ** (ใหม่ — ดูรายละเอียดด้านล่าง)
5. ปกจบ

---

## 📝 Worksheet: ในห้องเรียน (5 ข้อ, 15-20 นาที)

> **เป้าหมาย:** ง่าย-กลาง เน้น recall + ประยุกต์เบื้องต้น ไม่ต้องพิสูจน์ยาว

| ข้อ | ประเภท | ระดับ | เนื้อหา | เวลา |
|----|--------|------|---------|------|
| 1 | เติมตาราง | ง่าย | วาด truth table ของ $p \oplus q$, $p \uparrow q$, $p \downarrow q$ | 3 นาที |
| 2 | ระบุชื่อกฎ | ง่าย | จาก 4 ประพจน์ที่กำหนด ระบุว่าใช้ Modus Ponens/Tollens/HS/DS อันไหน | 3 นาที |
| 3 | แปลงเป็นสัญลักษณ์ | กลาง | เขียน "ทุกนักศึกษาสอบผ่าน" / "มีนักศึกษาบางคนได้ A" เป็น $\forall x P(x)$, $\exists x P(x)$ | 4 นาที |
| 4 | ยกตัวอย่างค้าน | กลาง | จาก $\forall x \in \mathbb{N}, x > 0$ ให้ยกตัวอย่างที่ทำให้เป็นเท็จ | 4 นาที |
| 5 | ตรวจ fallacy | กลาง | การอนุมาน "ถ้าฝนตก ดินเปียก, ดินเปียก → ฝนตก" ผิดแบบไหน (Affirming the Consequent) | 4 นาที |

**เฉลย:** ใส่ใน frame ถัดไปของ slide (สำหรับครู)

---

## 📚 การบ้านท้ายบทเรียน (5 ข้อ, ส่งสัปดาห์หน้า)

> **เป้าหมาย:** ฝึกพิสูจน์ + ประยุกต์ ข้อ 5 บังคับทำทุกคน

| ข้อ | ประเภท | ระดับ | เนื้อหา | คะแนน |
|----|--------|------|---------|--------|
| 1 | Truth table proof | กลาง | พิสูจน์ว่า HS เป็นสัจนิรันดร์: $((p \to q) \land (q \to r)) \to (p \to r)$ | 2 |
| 2 | Truth table proof | กลาง | พิสูจน์ว่า DS เป็นสัจนิรันดร์: $((p \lor q) \land \neg p) \to q$ | 2 |
| 3 | Universal Gate | กลาง-ยาก | เขียน $p \lor q$ และ $p \to q$ โดยใช้ NAND ($\uparrow$) อย่างเดียว (มีเฉลยให้ตรวจสอบ) | 2 |
| 4 | ตัวบ่งปริมาณ | กลาง | เอกภพ $U = \{1,2,3,4,5\}$ ประพจน์ $P(x)$: "$x$ หารด้วย 2 ลงตัว" → หาค่าความจริงของ $\forall x P(x)$ และ $\exists x P(x)$ + เขียนนิเสธ | 2 |
| 5 | ประยุกต์โปรแกรม **(+บังคับ)** | ยาก | ระบบรับสมัครงาน: ผ่านถ้า (อายุ ≥ 22 และ GPA ≥ 3.0) หรือ (ประสบการณ์ ≥ 2 ปี) เขียนเป็นสูตรตรรกศาสตร์ + truth table ของเงื่อนไข | 2 |

**รวม: 10 คะแนน**

---

## 🔧 การแก้ไขไฟล์

### ไฟล์ที่ต้องแก้
1. **`slides/_week3_body.tex`** (448 บรรทัด → ~520 บรรทัด)
   - ➕ เพิ่ม 3 frames ใน Section 1: Universal Gate exercise
   - ➕ เพิ่ม 1 frame ใน Section 2: นิเสธของตัวบ่งปริมาณ + ตัวอย่างค้าน
   - ➕ เพิ่ม 2 frames ใน Section 3: HS proof, DS proof
   - ➕ เพิ่ม 1 frame ใน Section 3: Fallacy alert
   - ➕ เพิ่ม 1 frame กิจกรรม worksheet
   - ➕ เพิ่ม 1 frame สรุปสัปดาห์ที่ 3 (แยกจากสรุปบท)
   - ➕ เพิ่ม 1 frame การบ้าน 5 ข้อ (แทน 3 ข้อเดิม)
   - แก้ฟอนต์ตารางจาก `\scriptsize` เป็น `\footnotesize` ใน truth tables

2. **`slides/chapter01_week3_worksheet.tex`** (82 บรรทัด → ~180 บรรทัด)
   - ขยายจาก 2 กิจกรรม เป็น 5 ข้อ (ง่าย-กลาง)
   - ➕ เพิ่มคำแนะนำ + เวลา + ตัวอย่างคำตอบสั้นๆ

3. **`slides/chapter01_week3_handout.tex`** — คงเดิม (compile จาก _week3_body.tex)

### ไฟล์ที่ไม่ต้องแก้
- `slides/_preamble.tex` (theme คงเดิม)
- `slides/chapter01_week3_slides.tex` (wrapper)
- `chapters/chapter01.tex` (textbook คงเดิม)

---

## ⏱️ Workflow

### Phase 1: สำรวจ (เสร็จแล้ว ✓)
- ✅ อ่าน chapter01.tex + slide + worksheet เดิม
- ✅ สรุปช่องว่างและจุดอ่อน
- ✅ วางแผน + ได้รับอนุมัติ

### Phase 2: แก้ไข Slide (slide body)
1. เปิด `_week3_body.tex`
2. เพิ่ม frame ใหม่ทีละ section ตามลำดับ
3. ตรวจสอบว่าใช้ macro/macro เดิม (\TT, \FF, \eng)

### Phase 3: เขียน Worksheet ใหม่
1. เปิด `chapter01_week3_worksheet.tex`
2. แทนที่กิจกรรมเดิมด้วย 5 ข้อใหม่
3. เพิ่มตัวอย่าง/เฉลยสั้นๆ

### Phase 4: Compile + ตรวจสอบ
1. รัน `xelatex` × 2-3 รอบ
2. ตรวจ PDF ว่า frame ใหม่ปรากฏครบ
3. ตรวจ worksheet PDF แยก

---

## 📌 หมายเหตุ

- ใช้สี/ฟอนต์/รูปแบบเดิมทั้งหมด เพื่อความต่อเนื่องจากสัปดาห์ 1-2
- ไม่ต้องเพิ่มภาพใหม่ (ใช้ TikZ logic gates เดิม)
- ระดับ worksheet = ง่าย-กลาง (ทำได้ใน 15-20 นาที) ไม่เกินนี้
- การบ้านข้อ 5 บังคับทำทุกคน แม้จะยาก
- ฟอนต์ truth table ใช้ `\footnotesize` แทน `\scriptsize` (อ่านง่ายขึ้น)