# Image Generation Prompts — บทที่ 1 ตรรกศาสตร์ (สัปดาห์ที่ 1)

ชุด prompt สำหรับสร้างภาพประกอบ (nanobanana2 / image generator) เพื่อนำไปวางในสไลด์
`chapter01_week1_slides.html` รายวิชา **4091606 คณิตศาสตร์สำหรับคอมพิวเตอร์** มหาวิทยาลัยราชภัฏอุตรดิตถ์

**สไตล์รวม (Logic Blueprint):** flat / vector, editorial-academic, สะอาด ไม่ใช่ 3D ไม่ใช่ภาพถ่าย
ไม่ใช่ AI clip-art ทั่วไป
**พื้นหลัง:** สว่าง / โปร่งใส (เพื่อวางบนกระดาษครีมของสไลด์)
**Palette (ใช้ทุกภาพในชุดนี้ให้สอดคล้องกัน):**

| ความหมาย | สี | Hex |
|---|---|---|
| Navy (ink / โครงหลัก) | น้ำเงินกรมท่า | `#1F3A93` |
| Green = True / สมเหตุสมผล | เขียว | `#2E8B57` |
| Red = False / ข้อบกพร่อง | แดง | `#C0392B` |
| Gold (เน้น / accent) | ทอง | `#B7950B` |
| Light navy (พื้นอ่อน) | ฟ้าอ่อน | `#E7ECF8` |
| Cream (พื้นกระดาษ) | ครีม | `#FFF7DD` |

> **กฎข้อความสำคัญ:** หลีกเลี่ยงข้อความฝังในภาพ "ทุกชนิด" เพื่อกันการสะกดไทย/อังกฤษเพี้ยน
> หากจำเป็นต้องมีสัญลักษณ์ ให้มีได้เฉพาะ glyph ตรรกศาสตร์ `¬ ∧ ∨ → ↔` หรือเลขฐานสอง `0` / `1`
> ที่ถูกต้องเท่านั้น — **ห้าม** มีคำไทย คำอังกฤษ หรือ true/false ในภาพ

---

## 1. `img/ch1_what_is_logic.png`

**ปรากฏที่:** สไลด์ 5 "ตรรกศาสตร์คืออะไร" — คอลัมน์ขวา, caption ใต้ภาพคือ "การให้เหตุผล: สมเหตุสมผล vs มีข้อบกพร่อง" (สัดส่วนภาพในเลย์เอาต์เป็น 4:3)

**แนวคิด:** การให้เหตุผล (reasoning) ที่แยกเป็นสองเส้นทาง — เส้นทางที่สมเหตุสมผล (valid → ติ๊กถูกเขียว)
กับเส้นทางที่มีข้อบกพร่อง (fallacy → กากบาทแดง)

### Positive prompt
```text
A clean flat-vector editorial illustration in an academic "blueprint" style for a
university logic course, on a light transparent background (no frame, no card).
Subject: a stylized human head shown in left-facing profile, drawn as a single
confident deep-navy (#1F3A93) outline with no shading. Inside the head, a small
cluster of two or three interlocking flat gears rendered in navy with thin gold
(#B7950B) accent rims, suggesting structured thinking.

From the front of the head a single glowing reasoning pathway flows outward and
forks into TWO diverging routes, like a decision split:
- The UPPER route is a smooth, confident curved line in green (#2E8B57) that ends
  in a bold green circular badge containing a clean check mark (valid reasoning).
- The LOWER route is a slightly broken / zig-zag line in red (#C0392B) that ends
  in a red circular badge containing a clean cross / X mark (a logical fallacy).

At the fork point, place a small, simple balance-scale motif drawn in flat navy
line art with a thin gold beam, subtly reinforcing the idea of weighing arguments.
The two scale pans tilt very slightly so the green side reads as "balanced/valid".

Overall aesthetic: minimalist flat vector, crisp 2-3pt strokes, generous empty
space, restrained palette of navy / green / red / gold on a light cream-to-white
field, soft and subtle drop shadows only. Distinctive, editorial, professional —
NOT generic clip-art, NOT 3D, NOT a photograph. Balanced, centered composition
suited to a 4:3 frame.
```

### Negative prompt
```text
no text, no words, no letters, no captions, no labels, no Thai script, no English
words, no true/false text, no numbers except none, no garbled glyphs, no random
ASCII, no watermark, no signature; no 3D render, no realistic photo, no photographic
skin, no clay / claymation, no plasticine, no glossy bevels, no heavy gradients, no
neon glow overload, no busy background, no graph-paper or wood texture, no cartoon
mascot, no cute robot, no emoji, no stock-art look, no dark background, no cluttered
wires, no extra check/cross marks beyond the two specified, no anatomical detail in
the face (no eyes/mouth detail), no brain gore.
```

### Aspect ratio & notes
- **Aspect ratio:** `~4:3` (เลย์เอาต์ `.fig` ของสไลด์เป็น `aspect-ratio:4/3`)
- **Notes:** ส่งออกพื้นหลังโปร่งใส (PNG) หรือพื้นขาว/ครีมอ่อนก็ได้ เพราะการ์ดมีขอบ dashed ของตัวเอง
  เขียว = ถูกต้อง/valid เสมอ, แดง = บกพร่อง/fallacy เสมอ (คงความหมายสีให้ตรงทั้งเด็ค)
  หากเครื่องมือใส่ glyph มาเอง ให้คงเฉพาะเครื่องหมายถูก/กากบาทในวงกลม ไม่ต้องมีตัวอักษร

---

## 2. `img/ch1_logic_in_computing.png`

**ปรากฏที่:** สไลด์ 7 "ตรรกศาสตร์กับคอมพิวเตอร์" — คอลัมน์ขวา, caption ใต้ภาพคือ "ลอจิกเกต → วงจรดิจิทัล → เลขฐานสอง" (สัดส่วน 4:3)

**แนวคิด:** ตรรกศาสตร์ → การคำนวณ เป็นการไหลแนวนอน: สัญลักษณ์ลอจิกเกต (รูปทรง ANSI ที่ถูกต้องของ
AND, OR, NOT) ป้อนเข้าสู่ไมโครชิป / แผงวงจร พร้อมเลขฐานสอง 0/1 จาง ๆ และเงา `{ }` ของ if…else แบบบาง

> **ความถูกต้องของทฤษฎี (ANSI gate shapes) — ระบุให้ generator ชัด:**
> - **AND** = ด้านหลังแบน + ด้านหน้าเป็นครึ่งวงกลม (D-shape) ไม่มีจุดกลม (bubble) ที่เอาต์พุต
> - **OR** = ด้านหลังโค้งเว้า + สองด้านโค้งมาบรรจบเป็นปลายแหลม ไม่มี bubble
> - **NOT** = สามเหลี่ยมชี้ไปทางขวา + มีจุดกลมเล็ก (inversion bubble) ที่ปลายเอาต์พุต (จุดกลมนี้ขาดไม่ได้)

### Positive prompt
```text
A clean flat-vector editorial "blueprint" infographic for a university computer
mathematics course, on a light transparent background, arranged as a single
left-to-right horizontal flow.

LEFT third: three classic ANSI/IEEE logic-gate symbols stacked vertically, all
drawn as crisp deep-navy (#1F3A93) line shapes (2.5pt stroke) with very light
navy (#E7ECF8) fills:
- an AND gate (flat back, semicircular front, D-shape, NO bubble),
- an OR gate (concave curved back, two curved sides meeting in a pointed nose,
  NO bubble),
- a NOT/inverter gate (right-pointing triangle WITH a small circular inversion
  bubble at its output tip — the bubble is essential).
Each gate has short clean input/output stubs.

MIDDLE: thin navy connector wires (some with right-angle bends like a schematic)
carry the gate outputs rightward and converge into the next stage.

RIGHT third: a stylized square microchip / IC sitting on a hint of a printed
circuit board — a flat navy chip body with evenly spaced pins on its sides and a
few thin gold (#B7950B) circuit traces fanning out. Inside or beside the chip,
faint light-navy binary digits "0" and "1" float subtly in a monospace style as a
background texture (low opacity, decorative, correctly formed 0 and 1 only). In a
soft, very faint gold tint behind the chip, suggest a pair of curly braces "{ }"
(as in if/else code blocks) — extremely subtle, like a watermark, the only other
glyphs allowed.

A few small green (#2E8B57) and red (#C0392B) signal dots on the wires hint at
true/false states without any text.

Aesthetic: minimalist flat vector, technical-yet-elegant, crisp strokes, plenty of
whitespace, restrained navy / gold / light-navy palette with tiny green & red
accents, soft subtle shadows only. Distinctive editorial-academic look — NOT
generic clip-art, NOT 3D, NOT a photo. Composition balanced for a 4:3 frame.
```

### Negative prompt
```text
no text, no words, no letters, no Thai script, no English words, no gate name
labels, no "AND"/"OR"/"NOT" text, no garbled glyphs, no random ASCII, no digits
other than the decorative binary 0 and 1, no watermark text, no signature; no 3D
render, no realistic photo, no clay / claymation, no glossy plastic, no heavy
gradients, no neon overload, no busy or dark background, no breadboard photo, no
wood or graph-paper texture, no cartoon mascot, no robot character, no emoji, no
incorrect gate shapes, no bubble on the AND or OR gate, no missing bubble on the
NOT gate, no tangled wire spaghetti, no realistic solder/components.
```

### Aspect ratio & notes
- **Aspect ratio:** `~4:3`
- **Notes:** ไหลซ้าย→ขวาให้ตรง caption "ลอจิกเกต → วงจรดิจิทัล → เลขฐานสอง" คงสีฟังก์ชัน
  (เขียว=จริง, แดง=เท็จ) ให้สอดคล้องกับภาพที่ 1 และทั้งเด็ค ตรวจหลัง generate ว่ารูปทรงเกต
  ถูกต้องตาม ANSI โดยเฉพาะ **bubble ของ NOT ต้องมี** และ **AND/OR ต้องไม่มี bubble**

---

## 3. (ตัวเลือก / OPTIONAL) `img/ch1_cover_hero.png`

**ปรากฏที่:** สไลด์ 1 (Cover / Title) — เป็น hero motif แบบบาง ๆ มุมขวาของหน้าปก
ไม่บังหัวเรื่อง "ตรรกศาสตร์ / Mathematical Logic" และแถบสัญลักษณ์ `¬ ∧ ∨ → ↔` ที่มีอยู่แล้ว

**แนวคิด:** ลวดลายตรรกศาสตร์เชิงนามธรรมแบบเบา ๆ ให้ความรู้สึก "พิมพ์เขียว/แปลนวิชาการ"
ใช้เป็นพื้นหลังตกแต่งที่จางพอจะไม่แย่งความสนใจจากตัวอักษร

### Positive prompt
```text
A subtle, elegant flat-vector hero motif for the title slide of a university logic
course, on a transparent / very light background, intended to sit quietly in a
corner behind a headline (must read as decorative, low-contrast, airy).

Compose an abstract "logic blueprint" emblem: a loosely connected node-and-edge
network (small navy #1F3A93 circles joined by thin straight and gently curved navy
lines), evoking a proof tree or a truth-table lattice. A few nodes glow faintly —
some green (#2E8B57), some red (#C0392B) — like true/false truth values lighting up
across the network, without any text. Thread a couple of thin gold (#B7950B) accent
lines through the structure for warmth. Behind it, an extremely faint blueprint grid
of light-navy lines fades out toward the edges (very low opacity).

The whole motif is light, sparse and refined — lots of negative space, suitable as a
quiet corner accent, never busy or saturated.

Aesthetic: minimalist flat vector, editorial-academic, crisp thin strokes, restrained
navy / gold palette with small green & red accent dots, soft subtle glow only. NOT
3D, NOT a photo, NOT clip-art, NOT a dense diagram. Designed to occupy one corner of
a wide layout while leaving generous empty space for a title.
```

### Negative prompt
```text
no text, no words, no letters, no Thai or English script, no numbers, no logic-symbol
text labels, no garbled glyphs, no watermark, no signature; no 3D render, no
photograph, no clay, no glossy plastic, no heavy gradients, no neon, no dark or busy
background, no full-bleed dense pattern, no high contrast that competes with a
headline, no cartoon mascot, no robot, no emoji, no graph-paper or wood texture,
no clutter.
```

### Aspect ratio & notes
- **Aspect ratio:** `~16:9` หรือกว้างกว่านั้น (เป็น hero ของหน้าปกแนวนอน) — หรือ crop เป็นสี่เหลี่ยม
  มุมขวาบนได้ตามต้องการ
- **Notes:** **ตัวเลือกเสริม** — เด็คปัจจุบันมีลวดลายพื้นหลัง/แถบสัญลักษณ์อยู่แล้ว ใช้ภาพนี้เฉพาะกรณี
  ต้องการ accent เพิ่ม ต้องคุมความจาง (opacity ต่ำ) ไม่ให้แย่งความเด่นของหัวเรื่อง

---

### หมายเหตุการนำไปใช้ (ทั้งชุด)
- ส่งออกเป็น **PNG พื้นหลังโปร่งใส** เพื่อให้กลมกลืนกับพื้นครีมของสไลด์ (`#FFF7DD` / `#FCFAF3`)
- หลัง generate ทุกภาพ ให้ตรวจ: (1) ไม่มีข้อความ/ตัวอักษรหลงเหลือ (2) glyph ที่มี (`¬ ∧ ∨ → ↔`,
  `0/1`, ติ๊ก/กากบาท) ถูกต้องคมชัด (3) สีตรง palette และความหมายสี (เขียว=จริง, แดง=เท็จ) สอดคล้องทั้งเด็ค
- บันทึกไฟล์ผลลัพธ์ตามชื่อเป้าหมายในหัวข้อแต่ละภาพ แล้ววางไว้ในโฟลเดอร์ `slides/img/`
