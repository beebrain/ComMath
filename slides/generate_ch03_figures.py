#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_ch03_figures.py
สร้างภาพกราฟและแผนภาพสำหรับ Chapter 3 Week 8 Slides ด้วย Python Matplotlib
ตามมาตรฐาน thai-textbook-figure-design
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

# ตั้งค่าฟอนต์และสไตล์ตามมาตรฐาน
plt.rcParams['font.sans-serif'] = ['TH Sarabun New', 'Sarabun', 'DejaVu Sans']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.unicode_minus'] = False

# Palette สีธีมสไลด์
NAVY = '#1F3A93'
NAVY_DARK = '#132660'
NAVY_LIGHT = '#EBF0FF'
GOLD = '#B45309'
GOLD_LIGHT = '#FEF3C7'
GREEN = '#16A34A'
GREEN_DARK = '#15803D'
GREEN_LIGHT = '#DCFCE7'
RED = '#DC2626'
RED_DARK = '#B91C1C'
RED_LIGHT = '#FEE2E2'
GRAY_LINE = '#E2E8F0'
GRAY_TEXT = '#64748B'
DARK_TEXT = '#1E293B'

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ==============================================================================
# Figure 1: Vertical Line Test (Slide 9)
# พาราโบลา y = x^2 (ฟังก์ชัน) vs วงกลม x^2 + y^2 = 4 (ไม่เป็นฟังก์ชัน)
# ==============================================================================
def make_vertical_line_test():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 2.7), dpi=300)
    fig.patch.set_facecolor('#ffffff')

    # --- แผงซ้าย: พาราโบลา y = x^2 ---
    ax1.set_facecolor('#fafafa')
    x = np.linspace(-2.2, 2.2, 300)
    y = x**2
    ax1.plot(x, y, color=NAVY, linewidth=2.6, label=r'$y = x^2$')
    
    # เส้นตรงแนวตั้ง x = 1.1
    c = 1.1
    ax1.axvline(x=c, color=GREEN, linewidth=2.2, linestyle='--', label=f'เส้นแนวตั้ง $x = {c}$')
    ax1.plot(c, c**2, 'o', color=GREEN_DARK, markersize=8, zorder=5)
    
    ax1.axhline(0, color='#94a3b8', linewidth=0.9)
    ax1.axvline(0, color='#94a3b8', linewidth=0.9)
    ax1.grid(True, linestyle=':', color=GRAY_LINE, alpha=0.8)
    ax1.set_xlim(-2.5, 2.5)
    ax1.set_ylim(-0.8, 4.8)
    ax1.set_title('พาราโบลา $y = x^2$\nตัดเพียง 1 จุด [เป็นฟังก์ชัน]', 
                  fontsize=13, fontweight='bold', color=GREEN_DARK, pad=6)
    ax1.annotate(f'ตัด 1 จุด ({c}, {c**2:.2f})', xy=(c, c**2), xytext=(c - 1.7, c**2 + 1.2),
                 fontsize=11.5, fontweight='bold', color=GREEN_DARK,
                 arrowprops=dict(arrowstyle='->', color=GREEN_DARK, lw=1.5))
    ax1.set_xlabel('x', fontsize=12, color=DARK_TEXT, loc='right')
    ax1.set_ylabel('y', fontsize=12, color=DARK_TEXT, loc='top', rotation=0)

    # --- แผงขวา: วงกลม x^2 + y^2 = 4 ---
    ax2.set_facecolor('#fafafa')
    theta = np.linspace(0, 2*np.pi, 300)
    r = 2.0
    ax2.plot(r*np.cos(theta), r*np.sin(theta), color=NAVY, linewidth=2.6, label=r'$x^2 + y^2 = 4$')
    
    # เส้นตรงแนวตั้ง x = 1.0
    cx = 1.0
    cy = np.sqrt(r**2 - cx**2)
    ax2.axvline(x=cx, color=RED, linewidth=2.2, linestyle='--', label=f'เส้นแนวตั้ง $x = {cx}$')
    ax2.plot([cx, cx], [cy, -cy], 'o', color=RED_DARK, markersize=8, zorder=5)
    
    ax2.axhline(0, color='#94a3b8', linewidth=0.9)
    ax2.axvline(0, color='#94a3b8', linewidth=0.9)
    ax2.grid(True, linestyle=':', color=GRAY_LINE, alpha=0.8)
    ax2.set_xlim(-2.8, 2.8)
    ax2.set_ylim(-2.8, 2.8)
    ax2.set_aspect('equal')
    ax2.set_title('วงกลม $x^2 + y^2 = 4$\nตัด 2 จุด [ไม่เป็นฟังก์ชัน]', 
                  fontsize=13, fontweight='bold', color=RED_DARK, pad=6)
    ax2.annotate(f'จุดที่ 1 ({cx}, {cy:.2f})', xy=(cx, cy), xytext=(cx - 2.3, cy + 0.45),
                 fontsize=10.5, fontweight='bold', color=RED_DARK,
                 arrowprops=dict(arrowstyle='->', color=RED_DARK, lw=1.4))
    ax2.annotate(f'จุดที่ 2 ({cx}, {-cy:.2f})', xy=(cx, -cy), xytext=(cx - 2.3, -cy - 0.55),
                 fontsize=10.5, fontweight='bold', color=RED_DARK,
                 arrowprops=dict(arrowstyle='->', color=RED_DARK, lw=1.4))
    ax2.set_xlabel('x', fontsize=12, color=DARK_TEXT, loc='right')
    ax2.set_ylabel('y', fontsize=12, color=DARK_TEXT, loc='top', rotation=0)

    for ax in (ax1, ax2):
        for spine in ax.spines.values():
            spine.set_edgecolor('#cbd5e1')

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, 'ch03_w08_vertical_line_test.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f'Generated: {out_path}')


# ==============================================================================
# Figure 2: Parabola Domain & Range (Slide 14)
# g(x) = x^2 - 4x + 7 = (x - 2)^2 + 3
# ==============================================================================
def make_parabola_domain_range():
    fig, ax = plt.subplots(figsize=(5.2, 3.2), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#fafafa')

    x = np.linspace(-0.6, 4.6, 300)
    y = (x - 2)**2 + 3
    ax.plot(x, y, color=NAVY, linewidth=2.7, label=r'$g(x) = (x-2)^2 + 3$')

    # จุดต่ำสุด (Vertex)
    vx, vy = 2.0, 3.0
    ax.plot(vx, vy, 'o', color=GOLD, markersize=9, zorder=6)
    ax.annotate('จุดต่ำสุด (2, 3)', xy=(vx, vy), xytext=(vx + 0.35, vy - 0.8),
                fontsize=12, fontweight='bold', color=GOLD,
                bbox=dict(boxstyle='round,pad=0.25', facecolor=GOLD_LIGHT, edgecolor=GOLD, lw=0.9),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

    # แกนสมมาตร x = 2
    ax.axvline(vx, color=GOLD, linestyle=':', linewidth=1.5, alpha=0.8)

    # ไฮไลต์ Range บนแกน Y: [3, inf) วางเยื้องขวาไม่ทับเส้น
    ax.plot([0, 0], [3, 9.5], color=GREEN, linewidth=4.8, solid_capstyle='round', zorder=4)
    ax.plot(0, 3, 'o', color=GREEN_DARK, markersize=7, zorder=5)
    ax.annotate(r'$\operatorname{Ran}(g) = [3, \infty)$', xy=(0, 6.0), xytext=(0.28, 6.0),
                fontsize=12, fontweight='bold', color=GREEN_DARK, va='center',
                bbox=dict(boxstyle='round,pad=0.25', facecolor=GREEN_LIGHT, edgecolor=GREEN, lw=0.9))

    # ไฮไลต์ Domain บนแกน X: R
    ax.plot([-0.6, 4.6], [0, 0], color=NAVY, linewidth=3.8, zorder=4)
    ax.text(2.0, -0.68, r'$\operatorname{Dom}(g) = \mathbb{R}$' + ' (ทุกจำนวนจริง)',
            fontsize=11.5, fontweight='bold', color=NAVY, ha='center')

    ax.axhline(0, color='#94a3b8', linewidth=0.9)
    ax.axvline(0, color='#94a3b8', linewidth=0.9)
    ax.grid(True, linestyle=':', color=GRAY_LINE, alpha=0.8)
    ax.set_xlim(-0.8, 4.8)
    ax.set_ylim(-0.9, 9.8)
    ax.set_title(r'พาราโบลา $g(x) = x^2 - 4x + 7$', fontsize=13.5, fontweight='bold', color=NAVY, pad=6)
    ax.set_xlabel('x', fontsize=12, color=DARK_TEXT, loc='right')
    ax.set_ylabel('y', fontsize=12, color=DARK_TEXT, loc='top', rotation=0)

    for spine in ax.spines.values():
        spine.set_edgecolor('#cbd5e1')

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, 'ch03_w08_parabola_domain_range.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f'Generated: {out_path}')


# ==============================================================================
# Figure 3: Horizontal Line Test (Slide 17)
# เส้นตรง (Injective 1-1) vs พาราโบลา (Many-to-1)
# ==============================================================================
def make_horizontal_line_test():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 2.7), dpi=300)
    fig.patch.set_facecolor('#ffffff')

    # --- แผงซ้าย: เส้นตรง y = 0.8x + 1 (Injective) ---
    ax1.set_facecolor('#fafafa')
    x = np.linspace(-2.2, 2.2, 200)
    y = 0.8 * x + 1.0
    ax1.plot(x, y, color=NAVY, linewidth=2.6, label=r'$y = 0.8x + 1$')
    
    # เส้นตรงแนวนอน y = 1.8
    k1 = 1.8
    x_cut1 = (k1 - 1.0) / 0.8
    ax1.axhline(y=k1, color=GREEN, linewidth=2.2, linestyle='--', label=f'เส้นแนวนอน $y = {k1}$')
    ax1.plot(x_cut1, k1, 'o', color=GREEN_DARK, markersize=8, zorder=5)
    
    ax1.axhline(0, color='#94a3b8', linewidth=0.9)
    ax1.axvline(0, color='#94a3b8', linewidth=0.9)
    ax1.grid(True, linestyle=':', color=GRAY_LINE, alpha=0.8)
    ax1.set_xlim(-2.5, 2.5)
    ax1.set_ylim(-1.2, 3.5)
    ax1.set_title('ฟังก์ชันเส้นตรง (Linear)\nตัดเพียง 1 จุด [Injective: 1-to-1]', 
                  fontsize=12.5, fontweight='bold', color=GREEN_DARK, pad=6)
    ax1.annotate(f'ตัด 1 จุด ({x_cut1:.2f}, {k1})', xy=(x_cut1, k1), xytext=(x_cut1 - 1.8, k1 + 0.65),
                 fontsize=11, fontweight='bold', color=GREEN_DARK,
                 arrowprops=dict(arrowstyle='->', color=GREEN_DARK, lw=1.4))
    ax1.set_xlabel('x', fontsize=12, color=DARK_TEXT, loc='right')
    ax1.set_ylabel('y', fontsize=12, color=DARK_TEXT, loc='top', rotation=0)

    # --- แผงขวา: พาราโบลา y = x^2 (Many-to-1) ---
    ax2.set_facecolor('#fafafa')
    x = np.linspace(-2.2, 2.2, 300)
    y = x**2
    ax2.plot(x, y, color=NAVY, linewidth=2.6, label=r'$y = x^2$')
    
    # เส้นตรงแนวนอน y = 2.0
    k2 = 2.0
    x_cuts = [-np.sqrt(k2), np.sqrt(k2)]
    ax2.axhline(y=k2, color=RED, linewidth=2.2, linestyle='--', label=f'เส้นแนวนอน $y = {k2}$')
    ax2.plot(x_cuts, [k2, k2], 'o', color=RED_DARK, markersize=8, zorder=5)
    
    ax2.axhline(0, color='#94a3b8', linewidth=0.9)
    ax2.axvline(0, color='#94a3b8', linewidth=0.9)
    ax2.grid(True, linestyle=':', color=GRAY_LINE, alpha=0.8)
    ax2.set_xlim(-2.5, 2.5)
    ax2.set_ylim(-0.8, 4.5)
    ax2.set_title('พาราโบลา $y = x^2$\nตัด 2 จุด [Many-to-1: ไม่ 1-1]', 
                  fontsize=12.5, fontweight='bold', color=RED_DARK, pad=6)
    ax2.annotate(f'จุดที่ 1 ({-np.sqrt(k2):.2f}, {k2})', xy=(x_cuts[0], k2), xytext=(x_cuts[0] - 0.75, k2 + 1.2),
                 fontsize=10.5, fontweight='bold', color=RED_DARK,
                 arrowprops=dict(arrowstyle='->', color=RED_DARK, lw=1.3))
    ax2.annotate(f'จุดที่ 2 ({np.sqrt(k2):.2f}, {k2})', xy=(x_cuts[1], k2), xytext=(x_cuts[1] - 0.35, k2 + 1.2),
                 fontsize=10.5, fontweight='bold', color=RED_DARK,
                 arrowprops=dict(arrowstyle='->', color=RED_DARK, lw=1.3))
    ax2.set_xlabel('x', fontsize=12, color=DARK_TEXT, loc='right')
    ax2.set_ylabel('y', fontsize=12, color=DARK_TEXT, loc='top', rotation=0)

    for ax in (ax1, ax2):
        for spine in ax.spines.values():
            spine.set_edgecolor('#cbd5e1')

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, 'ch03_w08_horizontal_line_test.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f'Generated: {out_path}')


# ==============================================================================
# Figure 4: Pigeonhole Principle (Slide 23)
# นกพิราบ 4 ตัว บินลง 3 รัง (เกิดการชนกันเสมอ)
# ==============================================================================
def make_pigeonhole_diagram():
    fig, ax = plt.subplots(figsize=(5.6, 3.2), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#fafafa')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # หัวข้อบนแผนภาพ
    ax.text(5.0, 5.65, 'นกพิราบ $N = 4$ ตัว บินลงรัง $k = 3$ รัง', 
            fontsize=13.5, fontweight='bold', color=NAVY, ha='center')

    # ตำแหน่งนกพิราบ 4 ตัว (แถวบน y = 4.4)
    p_x = [1.5, 3.8, 6.2, 8.5]
    p_labels = [r'$p_1$', r'$p_2$', r'$p_3$', r'$p_4$']
    p_colors = [NAVY_LIGHT, RED_LIGHT, RED_LIGHT, NAVY_LIGHT]
    p_strokes = [NAVY, RED, RED, NAVY]

    for px, plab, pcol, pstrk in zip(p_x, p_labels, p_colors, p_strokes):
        # วาดวงกลมนก
        circle = Circle((px, 4.35), 0.52, facecolor=pcol, edgecolor=pstrk, linewidth=2.0, zorder=4)
        ax.add_patch(circle)
        ax.text(px, 4.35, plab, fontsize=13, fontweight='bold', color=pstrk, ha='center', va='center', zorder=5)

    # ตำแหน่งรังนก 3 รัง (แถวล่าง y = 1.3)
    # รัง 1 (x=0.5..2.5)
    box1 = FancyBboxPatch((0.5, 1.1), 2.0, 1.3, boxstyle="round,pad=0.1,rounding_size=0.2",
                          facecolor=NAVY_LIGHT, edgecolor=NAVY, linewidth=1.8, zorder=3)
    ax.add_patch(box1)
    ax.text(1.5, 1.95, 'รังที่ 1', fontsize=12.5, fontweight='bold', color=NAVY, ha='center')
    ax.plot(1.5, 1.48, 'o', color=NAVY, markersize=9)

    # รัง 2 (ชน!) (x=3.5..6.5)
    box2 = FancyBboxPatch((3.4, 0.95), 3.2, 1.6, boxstyle="round,pad=0.1,rounding_size=0.2",
                          facecolor=RED_LIGHT, edgecolor=RED, linewidth=2.4, zorder=3)
    ax.add_patch(box2)
    ax.text(5.0, 2.05, 'รังที่ 2 (เกิดการชนกัน!)', fontsize=13, fontweight='bold', color=RED_DARK, ha='center')
    ax.plot([4.4, 5.6], [1.5, 1.5], 'o', color=RED, markersize=9)
    ax.text(5.0, 1.15, 'บรรจุ 2 ตัว (ขั้นต่ำ)', fontsize=11, fontweight='bold', color=RED_DARK, ha='center')

    # รัง 3 (x=7.5..9.5)
    box3 = FancyBboxPatch((7.5, 1.1), 2.0, 1.3, boxstyle="round,pad=0.1,rounding_size=0.2",
                          facecolor=NAVY_LIGHT, edgecolor=NAVY, linewidth=1.8, zorder=3)
    ax.add_patch(box3)
    ax.text(8.5, 1.95, 'รังที่ 3', fontsize=12.5, fontweight='bold', color=NAVY, ha='center')
    ax.plot(8.5, 1.48, 'o', color=NAVY, markersize=9)

    # ลูกศรชี้ลง (Zero Crossing)
    # p1 -> รัง 1
    arrow1 = FancyArrowPatch((1.5, 3.8), (1.5, 2.45), arrowstyle='->,head_width=4.5,head_length=7',
                             color=NAVY, linewidth=2.0, zorder=3)
    ax.add_patch(arrow1)

    # p2 -> รัง 2 ซ้าย
    arrow2 = FancyArrowPatch((3.8, 3.8), (4.4, 2.6), arrowstyle='->,head_width=4.5,head_length=7',
                             color=RED, linewidth=2.2, zorder=3)
    ax.add_patch(arrow2)

    # p3 -> รัง 2 ขวา
    arrow3 = FancyArrowPatch((6.2, 3.8), (5.6, 2.6), arrowstyle='->,head_width=4.5,head_length=7',
                             color=RED, linewidth=2.2, zorder=3)
    ax.add_patch(arrow3)

    # p4 -> รัง 3
    arrow4 = FancyArrowPatch((8.5, 3.8), (8.5, 2.45), arrowstyle='->,head_width=4.5,head_length=7',
                             color=NAVY, linewidth=2.0, zorder=3)
    ax.add_patch(arrow4)

    # กล่องข้อสรุปด้านล่าง
    ax.text(5.0, 0.35, r'$\lceil N / k \rceil = \lceil 4 / 3 \rceil = \mathbf{2}$' + ' ตัวในหนึ่งรังเสมอ',
            fontsize=13, fontweight='bold', color=NAVY, ha='center',
            bbox=dict(boxstyle='round,pad=0.28', facecolor='#ffffff', edgecolor=NAVY, lw=1.3))

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, 'ch03_w08_pigeonhole.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f'Generated: {out_path}')


# ==============================================================================
# Figure 5: Hash Collision PHP in CS (Slide 24)
# คีย์ N = 4 ลงตารางแฮช M = 3 ช่อง (การชนกัน)
# ==============================================================================
def make_hash_collision_diagram():
    fig, ax = plt.subplots(figsize=(8.8, 2.7), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#fafafa')
    ax.set_xlim(0, 16.5)
    ax.set_ylim(0, 5.2)
    ax.axis('off')

    # หัวข้อคอลัมน์ 1: คีย์ข้อมูล (N = 4)
    ax.text(1.5, 4.85, 'คีย์ข้อมูล (N = 4)', fontsize=13.5, fontweight='bold', color=NAVY, ha='center')
    
    # 4 คีย์ในแนวตั้ง ปรับระดับ y ให้ตรงกับเป้าหมายเป๊ะๆ (100% Horizontal)
    k_y = [3.44, 2.84, 1.77, 0.67]
    k_labels = [r'$k_1$', r'$k_2$', r'$k_3$', r'$k_4$']
    k_colors = [RED_LIGHT, RED_LIGHT, NAVY_LIGHT, NAVY_LIGHT]
    k_strokes = [RED, RED, NAVY, NAVY]

    for ky, klab, kcol, kstrk in zip(k_y, k_labels, k_colors, k_strokes):
        circ = Circle((1.5, ky), 0.40, facecolor=kcol, edgecolor=kstrk, linewidth=2.0, zorder=4)
        ax.add_patch(circ)
        ax.text(1.5, ky, klab, fontsize=12.5, fontweight='bold', color=kstrk, ha='center', va='center', zorder=5)

    ax.text(3.7, 4.55, 'ฟังก์ชันแฮช ' + r'$h(k)$', fontsize=11.5, color=GRAY_TEXT, ha='center')

    # หัวข้อคอลัมน์ 2: ตารางแฮช (M = 3 ช่อง)
    ax.text(7.2, 4.85, 'ตารางแฮช (M = 3 ช่อง)', fontsize=13.5, fontweight='bold', color=NAVY, ha='center')

    # ช่อง 0: Collision Bucket
    slot0 = FancyBboxPatch((5.5, 2.4), 3.4, 1.8, boxstyle="round,pad=0.08,rounding_size=0.15",
                           facecolor=RED_LIGHT, edgecolor=RED, linewidth=2.2, zorder=3)
    ax.add_patch(slot0)
    ax.text(7.2, 3.88, '[ช่อง 0] เกิดการชนกัน!', fontsize=11.5, fontweight='bold', color=RED_DARK, ha='center')
    
    # แถวย่อย k1 และ k2
    sub1 = FancyBboxPatch((5.7, 3.2), 3.0, 0.48, boxstyle="round,pad=0.04", facecolor='#fff', edgecolor=RED, lw=1.0)
    sub2 = FancyBboxPatch((5.7, 2.6), 3.0, 0.48, boxstyle="round,pad=0.04", facecolor='#fff', edgecolor=RED, lw=1.0)
    ax.add_patch(sub1)
    ax.add_patch(sub2)
    ax.text(7.2, 3.44, r'$k_1$' + ' (บันทึกสำเร็จ)', fontsize=10.5, fontweight='bold', color=RED_DARK, ha='center', va='center')
    ax.text(7.2, 2.84, r'$k_2$' + ' (ชนกับ ' + r'$k_1$' + '!)', fontsize=10.5, fontweight='bold', color=RED_DARK, ha='center', va='center')

    # ช่อง 1
    slot1 = FancyBboxPatch((5.5, 1.45), 3.4, 0.65, boxstyle="round,pad=0.08,rounding_size=0.12",
                           facecolor='#fff', edgecolor=NAVY, linewidth=1.6, zorder=3)
    ax.add_patch(slot1)
    ax.text(7.2, 1.77, r'[ช่อง 1]  $k_3$' + ' (สำเร็จ)', fontsize=11.5, fontweight='bold', color=NAVY, ha='center', va='center')

    # ช่อง 2
    slot2 = FancyBboxPatch((5.5, 0.35), 3.4, 0.65, boxstyle="round,pad=0.08,rounding_size=0.12",
                           facecolor='#fff', edgecolor=NAVY, linewidth=1.6, zorder=3)
    ax.add_patch(slot2)
    ax.text(7.2, 0.67, r'[ช่อง 2]  $k_4$' + ' (สำเร็จ)', fontsize=11.5, fontweight='bold', color=NAVY, ha='center', va='center')

    # ลูกศรแนวนอน 100% ขนานกัน ไม่มีการตัดกันเด็ดขาด
    arrow_k1 = FancyArrowPatch((1.98, 3.44), (5.4, 3.44), arrowstyle='->,head_width=4.5,head_length=7',
                               color=RED, linewidth=2.0, zorder=4)
    arrow_k2 = FancyArrowPatch((1.98, 2.84), (5.4, 2.84), arrowstyle='->,head_width=4.5,head_length=7',
                               color=RED, linewidth=2.0, zorder=4)
    arrow_k3 = FancyArrowPatch((1.98, 1.77), (5.4, 1.77), arrowstyle='->,head_width=4.5,head_length=7',
                               color=NAVY, linewidth=1.8, zorder=4)
    arrow_k4 = FancyArrowPatch((1.98, 0.67), (5.4, 0.67), arrowstyle='->,head_width=4.5,head_length=7',
                               color=NAVY, linewidth=1.8, zorder=4)
    for arr in [arrow_k1, arrow_k2, arrow_k3, arrow_k4]:
        ax.add_patch(arr)

    # คอลัมน์ 3: การ์ดคำอธิบายทฤษฎี PHP
    card = FancyBboxPatch((9.6, 0.35), 6.6, 4.3, boxstyle="round,pad=0.1,rounding_size=0.2",
                          facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.3, zorder=2)
    ax.add_patch(card)
    ax.text(9.9, 4.22, 'การชนกันของแฮช (Hash Collision)', fontsize=13, fontweight='bold', color=RED_DARK)
    ax.plot([9.9, 15.9], [3.92, 3.92], color='#e2e8f0', lw=1.2)
    ax.text(9.9, 3.48, '• คีย์ ' + r'$k_1$' + ' และ ' + r'$k_2$' + ' ถูกแฮชลง [ช่อง 0] ซ้ำกัน', fontsize=11.5, color=DARK_TEXT)
    ax.text(9.9, 2.92, '• จำนวนคีย์ ' + r'$N=4$' + ' มากกว่าจำนวนช่อง ' + r'$M=3$', fontsize=11.5, color=DARK_TEXT)
    ax.text(9.9, 2.36, '• แม้ฟังก์ชันจะสุ่มดีแค่ไหน ก็ต้องมีการชนกันเสมอ', fontsize=11.5, color=DARK_TEXT)

    # กล่องสูตรการันตี
    f_box = FancyBboxPatch((9.9, 0.65), 6.0, 1.35, boxstyle="round,pad=0.08,rounding_size=0.12",
                           facecolor=RED_LIGHT, edgecolor=RED, linewidth=1.3, zorder=3)
    ax.add_patch(f_box)
    ax.text(12.9, 1.45, r'$\lceil N / M \rceil = \lceil 4 / 3 \rceil = \mathbf{2}$' + ' คีย์/ช่อง',
            fontsize=13, fontweight='bold', color=RED_DARK, ha='center')
    ax.text(12.9, 0.95, 'การันตีตาม Pigeonhole Principle', fontsize=11, color=GRAY_TEXT, ha='center')

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, 'ch03_w08_hash_collision.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f'Generated: {out_path}')


# ==============================================================================
# Figure 6: Inverse Function Symmetry (Slide 32)
# f(x) = (2x+1)/(x-3) และ f^-1(x) = (3x+1)/(x-2) สะท้อนข้ามเส้นตรง y = x
# ==============================================================================
def make_inverse_symmetry():
    fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#fafafa')

    # แกนพิกัด x และ y
    ax.axhline(0, color='#94a3b8', linewidth=1.0)
    ax.axvline(0, color='#94a3b8', linewidth=1.0)
    ax.grid(True, linestyle=':', color=GRAY_LINE, alpha=0.8)

    # 1. เส้นสมมาตร y = x
    line_x = np.linspace(-5, 8.5, 200)
    ax.plot(line_x, line_x, color=GOLD, linestyle='--', linewidth=2.0, label='เส้นสมมาตร y = x')

    # 2. กราฟฟังก์ชัน f(x) = (2x + 1) / (x - 3)
    # กิ่งซ้าย: x in [-5, 2.5]
    x_f1 = np.linspace(-5, 2.5, 300)
    y_f1 = (2 * x_f1 + 1) / (x_f1 - 3)
    # กิ่งขวา: x in [3.5, 8.5]
    x_f2 = np.linspace(3.5, 8.5, 300)
    y_f2 = (2 * x_f2 + 1) / (x_f2 - 3)
    ax.plot(x_f1, y_f1, color=NAVY, linewidth=2.4, label=r'$f(x) = \frac{2x+1}{x-3}$')
    ax.plot(x_f2, y_f2, color=NAVY, linewidth=2.4)

    # 3. กราฟฟังก์ชันผกผัน f^-1(x) = (3x + 1) / (x - 2)
    # กิ่งซ้าย: x in [-5, 1.5]
    x_inv1 = np.linspace(-5, 1.5, 300)
    y_inv1 = (3 * x_inv1 + 1) / (x_inv1 - 2)
    # กิ่งขวา: x in [2.5, 8.5]
    x_inv2 = np.linspace(2.5, 8.5, 300)
    y_inv2 = (3 * x_inv2 + 1) / (x_inv2 - 2)
    ax.plot(x_inv1, y_inv1, color=GREEN_DARK, linewidth=2.4, label=r'$f^{-1}(x) = \frac{3x+1}{x-2}$')
    ax.plot(x_inv2, y_inv2, color=GREEN_DARK, linewidth=2.4)

    # 4. จุดสมมาตรคู่ที่ 1: A(5, 5.5) บน f และ A'(5.5, 5) บน f^-1
    pt1_f = (5.0, 5.5)
    pt1_inv = (5.5, 5.0)
    ax.plot([pt1_f[0], pt1_inv[0]], [pt1_f[1], pt1_inv[1]], color='#64748b', linestyle=':', linewidth=1.5, zorder=5)
    ax.plot(pt1_f[0], pt1_f[1], 'o', color=NAVY, markersize=7.5, zorder=6)
    ax.plot(pt1_inv[0], pt1_inv[1], 'o', color=GREEN_DARK, markersize=7.5, zorder=6)
    
    ax.annotate('(5, 5.5) บน f', xy=pt1_f, xytext=(pt1_f[0] - 2.8, pt1_f[1] + 1.1),
                fontsize=11.5, fontweight='bold', color=NAVY,
                bbox=dict(boxstyle='round,pad=0.2', facecolor=NAVY_LIGHT, edgecolor=NAVY, alpha=0.9),
                arrowprops=dict(arrowstyle='->', color=NAVY, lw=1.2))
    ax.annotate('(5.5, 5) บน ' + r'$f^{-1}$', xy=pt1_inv, xytext=(pt1_inv[0] + 0.3, pt1_inv[1] - 1.5),
                fontsize=11.5, fontweight='bold', color=GREEN_DARK,
                bbox=dict(boxstyle='round,pad=0.2', facecolor=GREEN_LIGHT, edgecolor=GREEN_DARK, alpha=0.9),
                arrowprops=dict(arrowstyle='->', color=GREEN_DARK, lw=1.2))

    # 5. จุดสมมาตรคู่ที่ 2: B(1, -1.5) บน f และ B'(-1.5, 1) บน f^-1
    pt2_f = (1.0, -1.5)
    pt2_inv = (-1.5, 1.0)
    ax.plot([pt2_f[0], pt2_inv[0]], [pt2_f[1], pt2_inv[1]], color='#64748b', linestyle=':', linewidth=1.5, zorder=5)
    ax.plot(pt2_f[0], pt2_f[1], 'o', color=NAVY, markersize=7.5, zorder=6)
    ax.plot(pt2_inv[0], pt2_inv[1], 'o', color=GREEN_DARK, markersize=7.5, zorder=6)
    
    ax.annotate('(1, -1.5)', xy=pt2_f, xytext=(pt2_f[0] - 2.8, pt2_f[1] - 1.6),
                fontsize=11.5, fontweight='bold', color=NAVY,
                bbox=dict(boxstyle='round,pad=0.15', facecolor='#ffffff', edgecolor='#cbd5e1', alpha=0.9),
                arrowprops=dict(arrowstyle='->', color=NAVY, lw=1.1))
    ax.annotate('(-1.5, 1)', xy=pt2_inv, xytext=(-4.2, 1.8),
                fontsize=11.5, fontweight='bold', color=GREEN_DARK,
                bbox=dict(boxstyle='round,pad=0.15', facecolor='#ffffff', edgecolor='#cbd5e1', alpha=0.9),
                arrowprops=dict(arrowstyle='->', color=GREEN_DARK, lw=1.1))

    # ป้ายข้อความ y = x
    ax.text(7.2, 6.4, r'$y = x$', fontsize=12.5, fontweight='bold', color=GOLD, rotation=45, va='bottom')

    # ขอบเขตแกน
    ax.set_xlim(-5, 8.5)
    ax.set_ylim(-5, 8.5)
    ax.set_aspect('equal')
    ax.set_xlabel('x', fontsize=12, loc='right', labelpad=-2)
    ax.set_ylabel('y', fontsize=12, loc='top', labelpad=-4, rotation=0)

    # Title & Legend (Lower Right: บริเวณ x > 2.5, y < 0 ว่างเปล่า 100% ไม่มีเส้นกราฟ)
    ax.set_title('สมมาตรของฟังก์ชันผกผันข้ามเส้นตรง ' + r'$y = x$' + '\nจุด ' + r'$(a, b)$' + ' บน ' + r'$f$' + ' สะท้อนเป็น ' + r'$(b, a)$' + ' บน ' + r'$f^{-1}$' + ' เสมอ',
                 fontsize=12.5, fontweight='bold', color=NAVY_DARK, pad=8)
    ax.legend(loc='lower right', fontsize=11.5, framealpha=0.95, edgecolor='#cbd5e1')

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, 'ch03_w08_inverse_symmetry.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f'Generated: {out_path}')


if __name__ == '__main__':
    print('Starting Python figure generation for Chapter 3 Week 8 Slides...')
    make_vertical_line_test()
    make_parabola_domain_range()
    make_horizontal_line_test()
    make_pigeonhole_diagram()
    make_hash_collision_diagram()
    make_inverse_symmetry()
    print('All 6 figures generated successfully!')

