#!/usr/bin/env python3
"""Generate the "Put ka pravom kvantnom računaru" progress-tracker SVGs, one per
lecture on the path to running a single-qubit calculation on real hardware
(finale = poglavlje2/07-using_quantum_computer.md).

Output: images/progress/progress-00.svg ... progress-07.svg
Each SVG is a self-contained vertical roadmap with the current step highlighted,
in the book's GitHub-light + teal palette. No JavaScript, print-safe.

Usage:  python generate_progress.py
"""
import os

# --- the 8 milestones on the path to the goal (order = TOC order) -----------
STEPS = [
    ("00", "Zašto kvantni računari?"),
    ("01", "Ko ih gradi?"),
    ("02", "Šta je kubit?"),
    ("03", "Kvantne kapije"),
    ("04", "Kvantna kola"),
    ("05", "Kvantno merenje"),
    ("06", "Uticaj šuma"),
    ("07", "Račun na pravom hardveru"),   # <-- the goal
]

# palette (matches styles/site.css)
TEAL   = "#0d9488"
TEAL2  = "#0ea5a4"
INK    = "#24292f"
MUTED  = "#6e7781"
LINE   = "#d0d7de"
LABEL  = "#3d444d"

# layout constants (SVG user units; viewBox width 250)
W        = 250
PAD_TOP  = 84          # y where the step list begins
ROW_DY   = 32
DOT_CX   = 24
DOT_R    = 7
LABEL_X  = 44
H        = PAD_TOP + len(STEPS) * ROW_DY + 14


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def dot_center_y(i):
    return PAD_TOP + i * ROW_DY + 6


def make_svg(current):
    n = len(STEPS)
    reached_goal = (current == n - 1)
    frac = max(0, current + 1) / n          # current = -1 -> "not started", 0/8
    fill_w = 218 * frac

    if reached_goal:
        meta = "Cilj dostignut · 100%"
        meta_fill = TEAL
        meta_weight = "700"
    else:
        meta = f"Korak {current + 1} od {n} · {round(frac * 100)}%"
        meta_fill = MUTED
        meta_weight = "400"

    p = []
    p.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" font-family="-apple-system,BlinkMacSystemFont,'
        f'Segoe UI,Helvetica,Arial,sans-serif" role="img" '
        f'aria-label="Napredak kursa: korak {current+1} od {n}">'
    )
    # card
    p.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" '
             f'fill="#ffffff" stroke="{LINE}"/>')

    # header icon: a small "chip"
    p.append(f'<g stroke="{TEAL}" stroke-width="1.6" fill="none">')
    p.append(f'<rect x="16" y="12" width="15" height="15" rx="3" fill="{TEAL}" stroke="none"/>')
    for dx in (5, 10):  # top/bottom pins
        p.append(f'<line x1="{16+dx}" y1="9" x2="{16+dx}" y2="12"/>')
        p.append(f'<line x1="{16+dx}" y1="27" x2="{16+dx}" y2="30"/>')
    for dy in (5, 10):  # left/right pins
        p.append(f'<line x1="13" y1="{12+dy}" x2="16" y2="{12+dy}"/>')
        p.append(f'<line x1="31" y1="{12+dy}" x2="34" y2="{12+dy}"/>')
    p.append('</g>')
    p.append(f'<circle cx="23.5" cy="19.5" r="3" fill="#ffffff"/>')

    # title (two lines)
    p.append(f'<text x="44" y="16" font-size="12.5" font-weight="700" fill="{INK}">Put ka pravom</text>')
    p.append(f'<text x="44" y="30" font-size="12.5" font-weight="700" fill="{INK}">kvantnom računaru</text>')

    # meta
    p.append(f'<text x="16" y="52" font-size="11.5" font-weight="{meta_weight}" fill="{meta_fill}">{esc(meta)}</text>')

    # progress bar
    p.append(f'<rect x="16" y="58" width="218" height="7" rx="3.5" fill="#eef0f2"/>')
    p.append(f'<rect x="16" y="58" width="{fill_w:.1f}" height="7" rx="3.5" fill="{TEAL}"/>')

    # connector lines
    y0 = dot_center_y(0)
    y_last = dot_center_y(n - 1)
    p.append(f'<line x1="{DOT_CX}" y1="{y0}" x2="{DOT_CX}" y2="{y_last}" stroke="{LINE}" stroke-width="2"/>')
    if current > 0:
        p.append(f'<line x1="{DOT_CX}" y1="{y0}" x2="{DOT_CX}" y2="{dot_center_y(current)}" '
                 f'stroke="{TEAL}" stroke-width="2"/>')

    # steps
    for i, (num, label) in enumerate(STEPS):
        cy = dot_center_y(i)
        is_goal = (i == n - 1)
        done = i < current or (reached_goal and is_goal)
        current_step = (i == current)

        # marker
        if is_goal:
            # target-square marker
            filled = done or current_step
            bg = TEAL if filled else "#ffffff"
            ring = "#ffffff" if filled else TEAL
            p.append(f'<rect x="{DOT_CX-8}" y="{cy-8}" width="16" height="16" rx="4" '
                     f'fill="{bg}" stroke="{TEAL}" stroke-width="2"/>')
            p.append(f'<circle cx="{DOT_CX}" cy="{cy}" r="3.4" fill="none" stroke="{ring}" stroke-width="1.6"/>')
            p.append(f'<circle cx="{DOT_CX}" cy="{cy}" r="0.9" fill="{ring}"/>')
        elif done:
            p.append(f'<circle cx="{DOT_CX}" cy="{cy}" r="{DOT_R}" fill="{TEAL}" stroke="{TEAL}" stroke-width="2"/>')
            p.append(f'<path d="M{DOT_CX-3.2} {cy+0.2} L{DOT_CX-1} {cy+2.4} L{DOT_CX+3.3} {cy-2.8}" '
                     f'fill="none" stroke="#ffffff" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>')
        elif current_step:
            p.append(f'<circle cx="{DOT_CX}" cy="{cy}" r="10.5" fill="{TEAL}" opacity="0.16"/>')
            p.append(f'<circle cx="{DOT_CX}" cy="{cy}" r="{DOT_R}" fill="#ffffff" stroke="{TEAL}" stroke-width="2"/>')
            p.append(f'<circle cx="{DOT_CX}" cy="{cy}" r="3" fill="{TEAL}"/>')
        else:
            p.append(f'<circle cx="{DOT_CX}" cy="{cy}" r="{DOT_R}" fill="#ffffff" stroke="{LINE}" stroke-width="2"/>')

        # label
        if current_step:
            lw, lc = "700", INK
        elif done:
            lw, lc = "400", MUTED
        else:
            lw, lc = "400", LABEL
        ty = cy + 4
        p.append(f'<text x="{LABEL_X}" y="{ty}" font-size="11.5" font-weight="{lw}" fill="{lc}">'
                 f'<tspan fill="{MUTED}" font-size="9.5">{num} </tspan>{esc(label)}</text>')

    p.append('</svg>')
    return "\n".join(p)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.join(here, "images", "progress")
    os.makedirs(outdir, exist_ok=True)
    # "not started" version (0/8, nothing filled) — e.g. for the intro page
    start_path = os.path.join(outdir, "progress-start.svg")
    with open(start_path, "w", encoding="utf-8") as f:
        f.write(make_svg(-1))
    print("wrote", start_path)

    for i, (num, _) in enumerate(STEPS):
        svg = make_svg(i)
        path = os.path.join(outdir, f"progress-{num}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        print("wrote", path)


if __name__ == "__main__":
    main()
