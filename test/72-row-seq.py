#!/usr/bin/env python3

import math

from test_more import ok, eq
import rplot

nseries = 4

sc = rplot.Screen(curses=False)
h = sc.height // nseries
rps = [None] * 4
for n in range(nseries):
    rps[n] = rplot.Plot(sc, height=h, offset=(0, h*n), start_color=n)

for x in range(sc.width):
    sc.clear()
    for n, rp in enumerate(rps):
        sr = rp.series(0)
        v = math.sin((1 + n) * 2 * math.pi * x / rp.width)
        sr.append(v)
        rp.draw_series()
    sc.update()
sc.wait()
