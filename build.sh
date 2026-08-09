#!/usr/bin/env bash
# คอมไพล์ตำราแล้วรายงานสุขภาพของ build
#
#   ./build.sh        คอมไพล์ตามปกติ (latexmk ข้ามถ้าไม่มีอะไรเปลี่ยน)
#   ./build.sh -g     บังคับรันใหม่ทุก pass ใช้เมื่อต้องการตัวเลขคำเตือนที่เชื่อถือได้
#
# หมายเหตุ ถ้า latexmk ขึ้นว่า "Nothing to do" แปลว่าไม่ได้คอมไพล์จริง
# ตัวเลขคำเตือนจะมาจาก main.log ของรอบก่อน จึงควรใช้ -g เมื่อจะรายงานผล
set -u
cd "$(dirname "$0")"

# OneDrive ล็อกไฟล์ระหว่าง build ทำให้เกิดไฟล์ -SAVE-ERROR ค้างและ build พัง
rm -f main.bcf-SAVE-ERROR main.bbl-SAVE-ERROR

latexmk ${1:-} -xelatex -interaction=nonstopmode main.tex > /tmp/commath-build.log 2>&1
status=$?

printf '\n=== ผลคอมไพล์ ===\n'
printf 'latexmk exit        %s\n' "$status"
grep -q 'Nothing to do' /tmp/commath-build.log &&
  printf '%s\n' 'หมายเหตุ latexmk ข้ามการคอมไพล์ ตัวเลขข้างล่างมาจากรอบก่อน ใช้ ./build.sh -g เพื่อบังคับรันใหม่'

[ -f main.pdf ] && printf 'จำนวนหน้า          %s\n' "$(pdfinfo main.pdf | awk '/^Pages/{print $2}')"

for pair in "error (!):^! " \
            "undefined ref:Reference.*undefined" \
            "undefined cite:Citation.*undefined" \
            "multiply defined:multiply defined" \
            "missing character:Missing character" \
            "overfull:Overfull" \
            "underfull:Underfull"; do
  label=${pair%%:*}; pattern=${pair#*:}
  printf '%-19s %s\n' "$label" "$(grep -c "$pattern" main.log)"
done

printf '\n=== กฎของโครงการ ===\n'
python3 tools/check_intro.py | grep -E 'รวม|ไม่มีเกริ่นนำ'
python3 tools/term_audit.py | head -1

exit $status
