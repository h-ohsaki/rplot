#!/usr/bin/env python3

from test_more import ok, eq
import rplot

rp = rplot.Plot()
rp.init_screen()
rp.draw_line(0, 0, 800, 600)
rp.update()
rp.wait()