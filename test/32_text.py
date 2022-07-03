#!/usr/bin/env python3

import time

from test_more import ok, eq
import rplot

rp = rplot.Plot(curses=True)
rp.init_screen()
rp.draw_text(10, 10, 'Hello, World!')
rp.update()
