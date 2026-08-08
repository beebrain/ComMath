import os
import subprocess
import shutil

# Directory paths
base_dir = "/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/URU_Work/BookComputerMath/ComMath"
figures_tikz_dir = os.path.join(base_dir, "Figures/tikz")
figures_dir = os.path.join(base_dir, "Figures")
temp_dir = os.path.join(base_dir, "temp_render")

os.makedirs(temp_dir, exist_ok=True)

ch1_figures = [
    "01-truth-table-basic",
    "02-and-gate-circuit",
    "03-or-gate-circuit",
    "04-implication-truth",
    "07-modus-ponens",
    "08-modus-tollens",
    "09-xor-logic"
]

style_path = os.path.join(figures_tikz_dir, "_styles")

latex_template = r"""\documentclass[border=10pt]{standalone}
\usepackage{fontspec}
\setmainfont[Script=Thai,WordSpace=1]{TH Sarabun New}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{tikz}
\usepackage{circuitikz}
\input{""" + style_path + r"""}
\begin{document}
\input{""" + figures_tikz_dir + r"""/__FIG_NAME__.tex}
\end{document}
"""

generated_files = []

for fig in ch1_figures:
    print(f"Generating {fig}...")
    tex_content = latex_template.replace("__FIG_NAME__", fig)
    tex_filename = os.path.join(temp_dir, f"{fig}_standalone.tex")
    
    with open(tex_filename, "w", encoding="utf-8") as f:
        f.write(tex_content)
        
    # Run xelatex
    cmd_xelatex = ["xelatex", "-interaction=nonstopmode", f"{fig}_standalone.tex"]
    res = subprocess.run(cmd_xelatex, cwd=temp_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    pdf_filename = os.path.join(temp_dir, f"{fig}_standalone.pdf")
    if os.path.exists(pdf_filename):
        # Convert to PNG using pdftoppm (300 DPI)
        output_prefix = os.path.join(temp_dir, fig)
        cmd_pdftoppm = ["pdftoppm", "-png", "-r", "300", pdf_filename, output_prefix]
        subprocess.run(cmd_pdftoppm, check=True)
        
        # pdftoppm appends -1.png or -01.png
        generated_png = output_prefix + "-1.png"
        if not os.path.exists(generated_png):
            generated_png = output_prefix + "-01.png"
            
        target_png = os.path.join(figures_dir, f"{fig}.png")
        target_jpg = os.path.join(figures_dir, f"{fig}.jpg")
        
        if os.path.exists(generated_png):
            shutil.copy(generated_png, target_png)
            print(f"Successfully generated: {target_png}")
            # Also convert to JPG via sips for backward compatibility
            subprocess.run(["sips", "-s", "format", "jpeg", target_png, "--out", target_jpg], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            generated_files.append(target_png)
        else:
            print(f"Error: PNG not found for {fig}")
    else:
        print(f"Compilation failed for {fig}")
        print(res.stdout[-500:])

print("\nAll Chapter 1 PNG figures generated successfully!")
