#!/usr/bin/env python3

from test_more import ok, eq
import rplot

sc = rplot.Screen()
ok(sc.width == 800)
ok(sc.height == 600)
