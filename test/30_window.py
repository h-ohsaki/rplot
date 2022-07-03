#!/usr/bin/env python3

import os

from test_more import ok, eq
import rplot

rp = rplot.Plot(curses=True)
rp.init_screen()
ok(rp.width >= 80)
ok(rp.height >= 25)
