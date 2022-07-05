#!/usr/bin/env python3

import math

from test_more import ok, eq
import rplot

sc = rplot.Screen(curses=True)
rp = rplot.Plot(sc, offset=(10, 10), width=60, height=30)
sr = rp.series(0)

for x in range(rp.width):
    sr.append(math.sin(2 * math.pi * x / rp.width))
rp.draw_series()
sc.update()
sc.wait()
