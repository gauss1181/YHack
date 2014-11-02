from visual import *
from visual.controls import *
g = []
bl  = []
for i in xrange(3):
  d = display(x = 0+i*520, y = 0, width=520, height=1080)
  d.forward= (0,0,5)
  g.append(d)
texdat = materials.loadTGA("test")
tex = materials.texture(data = texdat, mapping = "spherical", interpolate = False)
for i in xrange(3):
  redbox=box(pos=vector(0,0,0),
           size=(2,2,2),display = g[i], color=color.green, material = tex)
  print g[i].forward

def keyInput(evt):
    if evt.event == 'click':
        for i in xrange (3):
            print "Display #" + str(i)
            print g[i].forward
            print g[i].fov
def rotInput(evt):
    s = evt.key
    if s=='a':
        g[0].forward = g[0].forward.rotate(angle = -.1, axis = (0,0,1))
        g[0].center = 5*norm(g[0].forward)
        
    elif s=='s':
        g[0].forward = g[0].forward.rotate(angle = .1, axis = (0,0,1))
        g[0].center = 5*norm(g[0].forward)
        
    elif s=='d':
        g[1].forward = g[1].forward.rotate(angle = -.1, axis = (0,0,1))
        g[1].center = 5*norm(g[1].forward)

    elif s=='f':
        g[1].forward = g[1].forward.rotate(angle = .1, axis = (0,0,1))
        g[1].center = 5*norm(g[1].forward)

    elif s=='g':
        g[2].forward = g[2].forward.rotate(angle = -.1, axis = (0,0,1))
        g[2].center = 5*norm(g[2].forward)

    elif s == 'h':
        g[2].forward = g[2].forward.rotate(angle = .1, axis = (0,0,1))
        g[2].center = 5*norm(g[2].forward)
        

for i in xrange(3):
        g[i].bind('click', keyInput)
        g[i].bind('keydown', rotInput)
    
