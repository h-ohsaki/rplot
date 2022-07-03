#!/usr/bin/env python3

from test_more import ok, eq
import rplot

rp = rplot.Plot(curses=True)
sr = rp.series(0)

ok(sr.vmin == 0)
ok(sr.vmax == 0)

sr.append(1)
sr.append(2)
sr.append(3)

ok(sr.vmin == 0)
ok(sr.vmax == 3)

sr.append(-2)

ok(sr.vmin == -2)
ok(sr.vmax == 3)
