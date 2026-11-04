# -*- coding: utf-8 -*-
"""Pixelový banner profilu Daliika (styl loga RuGee). pouziti: banner.py <vystup.svg>"""
import random, sys
W, H = 1200, 320
R = random.Random(1104)
PISMENA = {
    'D': ['XXXXXX.', 'XX...XX', 'XX...XX', 'XX...XX', 'XX...XX', 'XX...XX', 'XX...XX', 'XXXXXX.'],
    'A': ['.XXXXX.', 'XX...XX', 'XX...XX', 'XXXXXXX', 'XXXXXXX', 'XX...XX', 'XX...XX', 'XX...XX'],
    'L': ['XX....', 'XX....', 'XX....', 'XX....', 'XX....', 'XX....', 'XXXXXX', 'XXXXXX'],
    'I': ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
    'K': ['XX...XX', 'XX..XX.', 'XX.XX..', 'XXXX...', 'XXXX...', 'XX.XX..', 'XX..XX.', 'XX...XX'],
}
o = []
o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" shape-rendering="crispEdges" role="img" aria-label="Daliik – hlavní developer Arconie">')
o.append('''<defs>
<linearGradient id="nebe" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a0918"/><stop offset=".55" stop-color="#1a1036"/><stop offset="1" stop-color="#2d1748"/></linearGradient>
<linearGradient id="zlato" gradientUnits="userSpaceOnUse" x1="0" y1="58" x2="0" y2="146"><stop offset="0" stop-color="#fff3c4"/><stop offset=".45" stop-color="#f2c14e"/><stop offset="1" stop-color="#c8834a"/></linearGradient>
<linearGradient id="mesic" gradientUnits="userSpaceOnUse" x1="1020" y1="48" x2="1080" y2="108"><stop offset="0" stop-color="#fff7dc"/><stop offset="1" stop-color="#e6d3a0"/></linearGradient>
<filter id="zar" x="-20%" y="-40%" width="140%" height="180%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<style>
.h{animation:blik 3.2s ease-in-out infinite}
.h2{animation:blik 4.7s ease-in-out infinite .8s}
.h3{animation:blik 2.6s ease-in-out infinite 1.6s}
@keyframes blik{0%,100%{opacity:1}50%{opacity:.15}}
.j{animation:stoupa 7s linear infinite}
@keyframes stoupa{0%{transform:translateY(0);opacity:0}10%{opacity:1}80%{opacity:.8}100%{transform:translateY(-190px);opacity:0}}
.okno{animation:plamen 1.8s steps(2) infinite}
@keyframes plamen{0%,100%{fill:#f2c14e}50%{fill:#e07a3a}}
.nadpis{animation:dech 5s ease-in-out infinite}
@keyframes dech{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
@media (prefers-reduced-motion: reduce){.h,.h2,.h3,.j,.okno,.nadpis{animation:none}}
</style>''')
o.append(f'<rect width="{W}" height="{H}" fill="url(#nebe)"/>')
# hvezdy
for i in range(90):
    x, y = R.randrange(0, W), R.randrange(0, 200)
    s = R.choice([2, 2, 2, 3, 4])
    c = R.choice(['#ffffff', '#cfc4ff', '#ffe9a3'])
    k = R.choice(['h', 'h2', 'h3', '', ''])
    o.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{c}"' + (f' class="{k}"' if k else '') + '/>')
# mesic (pixelovy kruh)
cx, cy, r = 1050, 78, 30
for yy in range(-r, r + 1, 4):
    for xx in range(-r, r + 1, 4):
        if xx * xx + yy * yy <= r * r:
            stin = (xx - 10) ** 2 + (yy + 6) ** 2 <= (r - 6) ** 2 and xx > 2
            o.append(f'<rect x="{cx+xx}" y="{cy+yy}" width="4" height="4" fill="{"#d9c58f" if stin else "url(#mesic)"}"/>')
# hory (vzdalene) - schody po 8 px
def hrebeny(baseline, barva, krok, vys, seed):
    rr = random.Random(seed)
    y = baseline - vys // 2
    body = []
    for x in range(0, W + krok, krok):
        y += rr.choice([-krok, 0, krok])
        y = max(baseline - vys, min(baseline - 10, y))
        body.append((x, y))
    d = f'M0 {H} ' + ' '.join(f'L{x} {y} L{x+krok} {y}' for x, y in body) + f' L{W} {H} Z'
    o.append(f'<path d="{d}" fill="{barva}"/>')
hrebeny(250, '#241a4d', 16, 110, 7)
hrebeny(275, '#1b1340', 8, 70, 11)
# hrad / dungeon silueta vpravo
hrad = '#120c2b'
def blok(x, y, w, h, c=hrad):
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>')
for (x, w, top) in [(860, 40, 170), (900, 90, 205), (990, 36, 150), (1026, 80, 200), (1106, 44, 180)]:
    blok(x, top, w, H - top)
    for zx in range(x, x + w, 12):
        blok(zx, top - 8, 6, 8)
for (x, y) in [(872, 190), (1000, 172), (1003, 210), (1118, 200), (930, 225), (1050, 222)]:
    o.append(f'<rect class="okno" x="{x}" y="{y}" width="8" height="12" fill="#f2c14e"/>')
# vlajka
blok(1006, 118, 4, 32, '#120c2b')
o.append('<path d="M1010 118 h22 l-6 6 l6 6 h-22 Z" fill="#c0392b"/>')
# zem
blok(0, 292, W, 28, '#0d0922')
for x in range(0, W, 24):
    blok(x, 288, 12, 4, '#17103a')
# jiskry/zhave uhliky stoupaji
for i in range(26):
    x = R.randrange(40, W - 40)
    y = R.randrange(250, 300)
    d = R.uniform(0, 7)
    c = R.choice(['#f2c14e', '#e07a3a', '#ffe9a3'])
    o.append(f'<rect class="j" x="{x}" y="{y}" width="3" height="3" fill="{c}" style="animation-delay:-{d:.2f}s"/>')
# nadpis DALIIK
S = 11
text = 'DALIIK'
mezera = 2
sirka = sum(len(PISMENA[c][0]) + mezera for c in text) - mezera
x0 = (W - sirka * S) // 2 - 120
y0 = 58
def napis(dx, dy, fill, cls=''):
    rr = []
    x = x0
    for c in text:
        g = PISMENA[c]
        for ry, row in enumerate(g):
            for rx, ch in enumerate(row):
                if ch == 'X':
                    rr.append(f'<rect x="{x + rx*S + dx}" y="{y0 + ry*S + dy}" width="{S}" height="{S}"/>')
        x += (len(g[0]) + mezera) * S
    return f'<g fill="{fill}"{cls}>' + ''.join(rr) + '</g>'
o.append('<g class="nadpis">')
o.append(napis(0, 0, '#f2c14e', ' filter="url(#zar)" opacity=".55"'))
o.append(napis(6, 6, '#07061a'))
o.append(napis(0, 0, 'url(#zlato)'))
# odlesk na hornich pixelech
o.append('</g>')
fx = x0
font = "font-family=\"'Press Start 2P','Courier New',ui-monospace,monospace\""
o.append(f'<text x="{fx}" y="{y0 + 8*S + 46}" {font} font-size="22" font-weight="700" letter-spacing="5" fill="#d8ccff">HLAVNÍ DEVELOPER · ARCONIA</text>')
o.append(f'<text x="{fx}" y="{y0 + 8*S + 78}" {font} font-size="15" letter-spacing="3" fill="#9d8fd6">Java · Paper · MythicMobs · Laravel · React</text>')
o.append('</svg>')
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(o))
print('ok', len('\n'.join(o)))
