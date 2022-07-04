#!/usr/bin/env python3

from test_more import ok, eq
import rplot

sc = rplot.Screen()
sc.draw_line(0, 0, 800, 600)
sc.update()
sc.wait()