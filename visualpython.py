import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

from visual import *
g = []
for i in xrange(3):
    g.append(display(x = 0+i*520, y = 0, width=520, height=1080))
for i in xrange(3):
    redbox=box(pos=vector(0,0,0),
               size=(8,4,6),display = g[i], color=color.red)
    # rotate the cube when twisting hand over leap motion
