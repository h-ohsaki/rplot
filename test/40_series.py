#!/usr/bin/env python3

from test_more import ok, eq
import rplot

rp = rplot.Plot()
sr = rp.series(0)
ok(len(sr) == 0)
sr.append(1)
sr.append(2)
sr.append(3)
ok(len(sr) == 3)
