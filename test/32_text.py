#!/usr/bin/env python3

from test_more import ok, eq
import rplot

sc = rplot.Screen(curses=True)
sc.draw_text(10, 10, 'Hello, World!')
sc.update()
