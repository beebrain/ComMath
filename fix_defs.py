import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all thrm blocks
    pattern = re.compile(r'\\begin\{thrm\}(.*?)\\end\{thrm\}', re.DOTALL)
    
    def repl(match):
        inner = match.group(1)
        # Heuristics for definition:
        # If it contains \textbf{... (English)} or \textbf{...} คือ or \textbf{...} หมายถึง
        # And it does NOT have [Algebraic Laws] or [De Morgan] etc. (unless it's a theorem)
        
        # Check if the block has an optional argument [xxx] at the very beginning
        opt_arg_match = re.match(r'^\s*\[(.*?)\]', inner)
        if opt_arg_match:
            opt_arg = opt_arg_match.group(1)
            # If it's explicitly a theorem or law, keep as thrm
            if 'Law' in opt_arg or 'Theorem' in opt_arg or 'Principle' in opt_arg or 'ทฤษฎี' in opt_arg or 'กฎ' in opt_arg or 'Properties' in opt_arg or 'Cantor' in opt_arg or 'Gate' in opt_arg:
                return match.group(0) # keep as thrm

        # check if it looks like a definition
        # looks for \textbf{...} near the start, or defines something
        if r'\textbf{ทฤษฎีบท' in inner:
            return match.group(0)
            
        if 'คือ' in inner[:200] or 'หมายถึง' in inner[:200] or 'เป็น' in inner[:100] or 'ได้แก่' in inner[:100]:
            if r'\textbf{' in inner[:200]:
                return f'\\begin{{definition}}{inner}\\end{{definition}}'
                
        # If it has \textbf{... (English)}
        if re.search(r'\\textbf\{.*?\([A-Za-z\s-]+\)\}', inner):
            return f'\\begin{{definition}}{inner}\\end{{definition}}'
            
        return match.group(0)

    new_content = pattern.sub(repl, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated definitions in {filepath}")

for filename in os.listdir('chapters'):
    if filename.endswith('.tex'):
        process_file(os.path.join('chapters', filename))
print("Done.")
