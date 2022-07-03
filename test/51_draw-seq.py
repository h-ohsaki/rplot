#!/usr/bin/env python3

import math

from test_more import ok, eq
import rplot

rp = rplot.Plot()
rp.init_screen()
sr = rp.series(0)

for n, x in enumerate(range(1000)):
    sr.append(math.sqrt(1 + n) * math.sin(x))
    rp.clear()
    rp.draw_series()
    rp.update()
rp.wait()
