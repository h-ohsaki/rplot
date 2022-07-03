#!/usr/bin/env python3

import math

from test_more import ok, eq
import rplot

nseries = 5

rp = rplot.Plot(curses=True)
rp.init_screen()

for n in range(nseries):
    sr = rp.series(n)
    for x in range(rp.width):
        v = math.sin((1 + n) * 2 * math.pi * x / rp.width)
        sr.append(v)
    sr.label = f'{n}-th series'

rp.draw_series()
rp.update()
rp.wait()
