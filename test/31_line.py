#!/usr/bin/env python3

from test_more import ok, eq
import rplot

rp = rplot.Plot(curses=True)
rp.init_screen()
rp.draw_line(0, 0, 40, 40)
rp.draw_line(0, 10, 40, 30)
rp.draw_line(10, 0, 20, 30)
rp.update()
