#!/usr/bin/env python3

import math

from test_more import ok, eq
import rplot

sc = rplot.Screen()
for n in range(50):
    sc.draw_text(n, n, f'#{n}: The quick brown fox jumps over the lazy dog.', color=n)
sc.update()
sc.wait()