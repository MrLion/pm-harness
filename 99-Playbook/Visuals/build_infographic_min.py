# Playbook infographic v8 — matched to the reference: two token rows -> one gate -> three outcomes, footer strip
import os

W, H = 1640, 900
NAVY = "#1e3a5f"; INK = "#24425c"; GRAY = "#6b7280"; BG = "#faf6f0"
COPPER = "#c05621"; TEAL = "#0f766e"
F = "Helvetica,Arial"

def token(x, y, w, h, label, color, filled=False, fs=22):
    if filled:
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{color}"/>'
                f'<text x="{x+w/2}" y="{y+h/2+8}" font-size="{fs}" font-weight="800" fill="#fff" text-anchor="middle" font-family="{F}">{label}</text>')
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="#fff" stroke="{color}" stroke-width="2.2"/>'
            f'<text x="{x+w/2}" y="{y+h/2+8}" font-size="{fs}" font-weight="800" fill="{INK}" text-anchor="middle" font-family="{F}">{label}</text>')

def harrow(x1, y, x2, color):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="3" marker-end="url(#a{color[1:]})"/>')

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     f'<rect width="{W}" height="{H}" fill="{BG}"/>',
     f'<defs>'
     f'<marker id="a{COPPER[1:]}" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><polygon points="0,0 10,5 0,10" fill="{COPPER}"/></marker>'
     f'<marker id="a{TEAL[1:]}" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><polygon points="0,0 10,5 0,10" fill="{TEAL}"/></marker>'
     f'<marker id="aN" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><polygon points="0,0 10,5 0,10" fill="{NAVY}"/></marker>'
     '</defs>',
     # header
     f'<text x="80" y="66" font-size="42" font-weight="800" fill="{NAVY}" font-family="{F}">The Product Playbook</text>',
     f'<text x="80" y="112" font-size="30" font-weight="800" fill="{COPPER}" font-family="{F}">An AI harness for product management</text>',
     f'<text x="82" y="148" font-size="20" fill="{GRAY}" font-family="{F}">What are you changing? &#183; How is work governed?</text>',
     ]

# ===== Row 1 : Vision-led (copper)
y1 = 200
s.append(f'<rect x="100" y="{y1}" width="1290" height="80" rx="40" fill="none" stroke="{COPPER}" stroke-width="2.5"/>')
s.append(token(112, y1+5, 330, 70, "Vision-led 0&#8594;1", COPPER, filled=True, fs=27))
s.append(token(560, y1+9, 210, 62, "Vision", COPPER))
s.append(harrow(778, y1+40, 838, COPPER))
s.append(token(846, y1+9, 210, 62, "Thesis", COPPER))
s.append(harrow(1064, y1+40, 1124, COPPER))
s.append(token(1132, y1+9, 246, 62, "Concept test", COPPER))
# ===== Row 2 : Outcome-led (teal)
y2 = 318
s.append(f'<rect x="100" y="{y2}" width="1290" height="80" rx="40" fill="none" stroke="{TEAL}" stroke-width="2.5"/>')
s.append(token(112, y2+5, 330, 70, "Outcome-led 1&#8594;N", TEAL, filled=True, fs=27))
s.append(token(560, y2+9, 210, 62, "Signal", TEAL))
s.append(harrow(778, y2+40, 838, TEAL))
s.append(token(846, y2+9, 260, 62, "Problem &amp; evidence", TEAL))
s.append(harrow(1114, y2+40, 1174, TEAL))
s.append(token(1182, y2+9, 196, 62, "Challenge", TEAL))

# ===== connectors into the gate (right side, stacked)
s.append(f'<path d="M 1394,240 H 1470 V 482 H 1108" fill="none" stroke="{COPPER}" stroke-width="3" marker-end="url(#a{COPPER[1:]})"/>')
s.append(f'<path d="M 1394,358 H 1520 V 527 H 1108" fill="none" stroke="{TEAL}" stroke-width="3" marker-end="url(#a{TEAL[1:]})"/>')

# ===== Evidence gate
s.append(f'<rect x="540" y="455" width="560" height="100" rx="26" fill="{NAVY}"/>')
s.append(f'<text x="820" y="500" font-size="30" font-weight="800" fill="#fff" text-anchor="middle" font-family="{F}">Evidence gate</text>')
s.append(f'<text x="820" y="532" font-size="20" fill="#cdd9e5" text-anchor="middle" font-family="{F}" font-style="italic">Do we know enough to commit?</text>')

# ===== fan-out to outcomes
s.append(f'<path d="M 820,555 V 610 H 380 V 648" fill="none" stroke="{NAVY}" stroke-width="2.5" marker-end="url(#aN)"/>')
s.append(f'<line x1="820" y1="610" x2="1260" y2="610" stroke="{NAVY}" stroke-width="2.5"/>')
s.append(f'<path d="M 820,610 V 648" fill="none" stroke="{NAVY}" stroke-width="2.5" marker-end="url(#aN)"/>')
s.append(f'<path d="M 1260,610 V 648" fill="none" stroke="{NAVY}" stroke-width="2.5" marker-end="url(#aN)"/>')
outs = [(170, "Uncertain", "Run the next test"), (610, "Proceed", "Deliver &#8594; Review"), (1050, "No-go", "Defer or stop")]
for x, t, sub in outs:
    s.append(f'<rect x="{x}" y="652" width="420" height="106" rx="20" fill="#fff" stroke="{NAVY}" stroke-width="2.5"/>'
             f'<text x="{x+210}" y="698" font-size="27" font-weight="800" fill="{NAVY}" text-anchor="middle" font-family="{F}">{t}</text>'
             f'<text x="{x+210}" y="732" font-size="19" fill="{GRAY}" text-anchor="middle" font-family="{F}">{sub}</text>')

# ===== footer
s.append(f'<line x1="80" y1="806" x2="1560" y2="806" stroke="#c9c4bb" stroke-width="2"/>')
s.append(f'<text x="80" y="842" font-size="19" font-weight="800" fill="{NAVY}" font-family="{F}">Operating model</text>'
         f'<text x="300" y="842" font-size="17" fill="{GRAY}" font-family="{F}">|&#160;&#160;&#160;Digital transformation &#183; Capabilities and value streams&#160;&#160;&#160;&#160;&#160;Project-to-product &#183; Funding, teams and governance</text>')
s.append(f'<text x="80" y="876" font-size="17" font-family="{F}" font-style="italic" fill="{INK}">'
         f'Obsidian &#183; Evidence<tspan fill="{GRAY}">&#160;&#160;&#160;&#160;&#160;</tspan><tspan fill="{COPPER}" font-weight="800">/pm</tspan><tspan fill="{GRAY}"> &#183; Reasoning</tspan><tspan> &#160;&#160;&#160;&#160;&#160;Git &#183; Audit trail</tspan></text>')
s.append('</svg>')

out = os.path.expanduser('~/flux-klein/playbook_min.svg')
open(out, 'w').write('\n'.join(s))
print('SVG_OK', os.path.getsize(out), out)
