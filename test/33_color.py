#!/usr/bin/env python3

import math

from test_more import ok, eq
import rplot

rp = rplot.Plot(curses=True)
rp.init_screen()
for n in range(rp.height):
    rp.draw_text(n, n, f'#{n}: The quick brown fox jumps over the lazy dog.', color=n)
rp.update()

