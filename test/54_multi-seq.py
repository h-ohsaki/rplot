#!/usr/bin/env python3

import math

from test_more import ok, eq
import rplot

nseries = 5

rp = rplot.Plot()
rp.init_screen()

for x in range(rp.width):
    rp.clear()
    for n in range(nseries):
        sr = rp.series(n)
        v = math.sin((1 + n) * 2 * math.pi * x / rp.width)
        sr.append(v)
    rp.draw_series()
    rp.update()
rp.wait()
