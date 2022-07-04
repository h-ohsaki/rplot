#!/usr/bin/env python3

from test_more import ok, eq
import rplot

sc = rplot.Screen(curses=True)
for n in range(sc.height):
    sc.draw_text(n, n, f'#{n}: The quick brown fox jumps over the lazy dog.', color=n)
sc.update()
