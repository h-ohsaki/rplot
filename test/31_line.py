#!/usr/bin/env python3

from test_more import ok, eq
import rplot

sc = rplot.Screen(curses=True)
sc.draw_line(0, 0, 40, 40)
sc.draw_line(0, 10, 40, 30, 1)
sc.draw_line(10, 0, 20, 30, 2)
sc.update()
