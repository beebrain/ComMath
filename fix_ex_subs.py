import os
import glob

for filename in glob.glob('chapters/*.tex'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('\\subsection{ส่วนที่', '\\subsection*{ส่วนที่')
    new_content = new_content.replace('\\subsection{เฉลยส่วนที่', '\\subsection*{เฉลยส่วนที่')
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
print("Done.")
