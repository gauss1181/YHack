# vPython

import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

from visual import *

scene1 = display(title="Just a Sphere",
                 x=0, y=0, width=800, height=800,
                 center=(0,0,0), background=(0,0,0))

sphere(color=color.red)

scene2 = display(title="Second Scene",
                 x=0, y=0, width=400, height=400,
                 center=(0,0,0), background=(0,1,0))

sphere()

scene3 = display(title="Ball In Box Animation",
                 x=0, y=0, width=600, height=600,
                 center=(0,0,0), background=(0,0,1))

ball = sphere(pos=(-5,0,0), radius=0.5, color=color.cyan)
wallR = box(pos=(6,0,0), size=(0.2,12,12), color=color.blue)
wallL = box(pos=(-16,0,0), size=(0.2,12,12), color=color.blue)
wallU = box(pos=(-5,6,0), size=(22,0.2,12), color=color.green)
wallD = box(pos=(-5,-6,0), size=(22,0.2,12), color=color.green)
wallB = box(pos=(-5,0,-6), size=(22,12,0.2), color=color.red)
ball.velocity = vector(25,5,15)
deltat = 0.005
t = 0
vscale = 0.1
scene3.autoscale = False
ball.trail = curve(color=ball.color)
while t < 10:
    rate(100)
    if (ball.pos.x > wallR.pos.x or ball.pos.x < wallL.pos.x):
        ball.velocity.x = -ball.velocity.x
    if (ball.pos.z > wallU.pos.z or ball.pos.z < wallD.pos.z):
        ball.velocity.z = -ball.velocity.z
    if (ball.pos.y < wallB.pos.y):
        ball.velocity.y = -ball.velocity.y
    ball.pos = ball.pos + ball.velocity*deltat
    ball.trail.append(pos=ball.pos)
    t += deltat
