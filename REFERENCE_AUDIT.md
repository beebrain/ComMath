# รายงานตรวจสอบบรรณานุกรม

วันที่ตรวจสอบ: 8 สิงหาคม 2569

## เกณฑ์

- รายการหนังสือต้องมี ISBN-13 ที่ตรวจ checksum ได้ และต้องสอดคล้องกับชื่อเรื่อง/ฉบับพิมพ์
- รายการบทความต้องมี DOI ที่แก้ไขได้
- ห้ามเติม ISBN หรือ DOI จากการคาดเดา

## ผลตรวจและการแก้ไข

- รายการหนังสือที่คงไว้ใน `references.bib`: 23 รายการ ทุกเล่มมี ISBN-13
- รายการบทความที่คงไว้: `codd1970relational` มี DOI `10.1145/362384.362685`
- แก้ `mendelson2015introduction` จาก ISBN `9781482237726` เป็น `9781482237788` ตามข้อมูลบรรณานุกรมของ Google Books สำหรับ *Introduction to Mathematical Logic*, 6th edition, CRC Press, 2015
- ISBN ที่คงไว้ทุกหมายเลขผ่านการตรวจเลขตรวจสอบ ISBN-13 แล้ว แต่การผ่าน checksum เพียงอย่างเดียวไม่ใช่หลักฐานว่าหนังสือมีอยู่จริง จึงต้องใช้ร่วมกับระเบียนสำนักพิมพ์/ห้องสมุดหรือผู้จำหน่าย

## รายการที่นำออกจากบรรณานุกรมใช้งาน

นำออกเพราะข้อมูลในโครงการยังไม่มี ISBN หรือ DOI ที่ตรวจยืนยันได้:

- `boole1854investigation`
- `frege1879begriffsschrift`
- `russell1910principia`
- `aristotle_organon`
- `saovon2556compmath`
- `saovon2553compmath`
- `limtrakul2538commath`

การนำออกไม่ได้แปลว่าเอกสารเหล่านี้ไม่มีอยู่จริง แต่ยังไม่ผ่านเกณฑ์ “ต้องมี DOI หรือ ISBN จริง” ของรอบตรวจนี้ จึงไม่ควรแสดงเป็นรายการอ้างอิงที่ยืนยันแล้วจนกว่าจะมีภาพหน้าลิขสิทธิ์หรือระเบียน ISBN/DOI จริง

## แหล่งตรวจตัวอย่างที่ใช้ยืนยัน

- Rosen, 8th ed.: ISBN-13 `9781259676512` — [Stewart Library catalog](https://libcat.weber.edu/cgi-bin/koha/opac-detail.pl?biblionumber=1198909)
- Grimaldi, 5th ed.: ISBN-13 `9780201726343` — [Rose-Hulman faculty publications](https://scholar.rose-hulman.edu/math_fac/285/)
- Hurley and Watson, 14th ed.: ISBN-13 `9780357798683` — [VitalSource bibliographic record](https://www.vitalsource.com/products/a-concise-introduction-to-logic-patrick-j-hurley-v9798214155425)
- Strang, 6th ed.: ISBN-13 `9781733146678` — [library catalog record](https://wowlic.sookmyung.ac.kr/search/detail/CAT000000888597)
- Mendelson, 6th ed.: [Google Books record](https://books.google.com/books/about/Introduction_to_Mathematical_Logic.html?id=FS-sCQAAQBAJ)

`ComMath_references_zotero.bib` ถูกปรับให้ไม่เก็บรายการที่ไม่มี identifier ชุดเดียวกัน แต่ยังคงรายการผลงานผู้เขียนที่อยู่ในไฟล์ Zotero เดิมไว้ เพราะเป็นคนละกลุ่มข้อมูลกับบรรณานุกรมหลัก
