#!/usr/bin/env python3

import math

from test_more import ok, eq
import rplot

rp = rplot.Plot(curses=True)
rp.init_screen()
sr1 = rp.series(0)
sr2 = rp.series(1)

for x in range(rp.width):
    sr1.append(math.sin(2 * math.pi * x / rp.width))
    sr2.append(math.cos(8 * math.pi * x / rp.width))
rp.draw_series()
rp.update()
rp.wait()
