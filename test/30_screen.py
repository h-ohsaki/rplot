#!/usr/bin/env python3

from test_more import ok, eq
import rplot

sc = rplot.Screen(curses=True)
ok(sc.width >= 80)
ok(sc.height >= 25)
