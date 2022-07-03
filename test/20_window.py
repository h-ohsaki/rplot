#!/usr/bin/env python3

from test_more import ok, eq
import rplot

rp = rplot.Plot()
rp.init_screen()
ok(rp.width == 800)
ok(rp.height == 600)
