from visual import *
from visual.controls import *
g = []
bl  = []
for i in xrange(3):
  d = display(x = 0+i*520, y = 0, width=520, height=1080)
  g.append(d)
texdat = materials.loadTGA("testtext")
tex = materials.texture(data = texdat, mapping = "rectangular", interpolate = False)
for i in xrange(3):
  redbox=box(pos=vector(0,-2,0),
           size=(2,2,2),display = g[i], color=color.green, material = tex)
  print g[i].forward

def keyInput(evt):
    if evt.event == 'click':
        for i in xrange (3):
            print "Display #" + str(i)
            print g[i].forward
            print g[i].fov
for i in xrange(3):
    g[i].bind('click', keyInput)
