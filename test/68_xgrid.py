#!/usr/bin/env python3

import math

from test_more import ok, eq
import rplot

sc = rplot.Screen(curses=True)
rp = rplot.Plot(sc, xgrid=1)
sr = rp.series(0)

for x in range(rp.width):
    sr.append(1.2 * x / 100)
rp.draw_series()
sc.update()
sc.wait()
