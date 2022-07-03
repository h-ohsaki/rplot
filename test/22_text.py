#!/usr/bin/env python3

from test_more import ok, eq
import rplot

rp = rplot.Plot()
rp.init_screen()
rp.draw_text(10, 10, 'Hello, World!')
rp.update()
rp.wait()
