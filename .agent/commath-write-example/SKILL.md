---
name: commath-write-example
description: Guide for writing mathematical examples, solutions, and step-by-step equations using the custom mathstyle.sty for the Computer Math textbook.
---

# Writing Computer Math Examples

When the user asks you to write, format, or generate an example (ตัวอย่าง) and its solution (วิธีทำ) for the Computer Mathematics textbook, you MUST strictly follow these guidelines.

## 1. Core Environments
Always use the `ex` environment for the problem statement and the `solution` environment for the answer. These are defined in `mathstyle.sty`.

```latex
\begin{ex}[ชื่อตัวอย่าง หรือ หัวข้อ]
จงหาค่าของ ...
\end{ex}

\begin{solution}
% เนื้อหาวิธีทำ
\end{solution}
```

## 2. Step-by-Step Solutions (`solsteps`)
For calculations, proofs, or logical deductions that require multiple steps, use the `solsteps` environment inside the `solution` block. 
- It has been custom-styled to have **no bullet points** and **reduced line spacing** for a clean, modern look.
- Use `\item` for each new step.

```latex
\begin{solution}
\begin{solsteps}
    \item จากสมการ $2x + 5 = 15$
    \item นำ $5$ ไปลบทั้งสองข้าง: $2x = 15 - 5$
    \item จะได้ $2x = 10$
\end{solsteps}
\end{solution}
```

## 3. Highlighting the Final Answer (`\mathoval`)
Always wrap the final result equation in the custom `\mathoval{...}` command. This will draw a clean oval border around the final answer without relying on complex TikZ code.

```latex
    \item ดังนั้นคำตอบคือ \mathoval{x = 5}
```

## 4. CRITICAL: Thai Text in Math Mode
**NEVER** type Thai characters directly inside math mode (e.g., `$ทด1$` or `$x_{พจน์}$`). This will cause a "Missing character" font error during XeLaTeX compilation.
**ALWAYS** wrap Thai text inside math mode with `\text{...}`.

* **Incorrect:** $x_{รวม} = 10$
* **Correct:** $x_{\text{รวม}} = 10$

## 5. End of Solution Formatting
The `solution` environment automatically inserts a subtle horizontal gray line and a blank line spacing at the end. You **do not** need to manually add `\hrule`, `\rule`, or `\vspace` after the `\end{solution}`.

## Full Example Template

```latex
\begin{ex}[การแก้สมการเชิงเส้น]
จงหาค่าของ $x$ จากสมการ $2x + 5 = 15$
\end{ex}

\begin{solution}
\begin{solsteps}
    \item จากสมการ $2x + 5 = 15$
    \item นำ $5$ ไปลบทั้งสองข้าง: $2x = 15 - 5$
    \item จะได้ $2x = 10$
    \item นำ $2$ ไปหารทั้งสองข้าง: $x = \frac{10}{2}$
    \item ดังนั้นคำตอบคือ \mathoval{x = 5}
\end{solsteps}
\end{solution}
```
