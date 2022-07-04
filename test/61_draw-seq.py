#!/usr/bin/env python3

import math

from test_more import ok, eq
import rplot

sc = rplot.Screen(curses=True)
rp = rplot.Plot(sc)
sr = rp.series(0)

for n, x in enumerate(range(1000)):
    sr.append(math.sqrt(1 + n) * math.sin(x))
    sc.clear()
    rp.draw_series()
    sc.update()
sc.wait()
