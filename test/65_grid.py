#!/usr/bin/env python3

import math

from test_more import ok, eq
import rplot

rp = rplot.Plot(curses=True, grid=100, subgrid=10)
rp.init_screen()
sr = rp.series(0)

for x in range(rp.width):
    sr.append(220 * math.sin(2 * math.pi * x / rp.width))
rp.draw_series()
rp.update()

