from visual import *
import sympy
from sympy import *
import ttk
from Tkinter import *
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

def show_formula():
    print(formula.get())
    Str_equation = formula.get()
    eq = sympify(Str_equation)
    tup = []
    for i in xrange (0, 10):
        temp = []
        for j in xrange(0,10):
            eq2 = eq.subs(x,i)
            eq3 = eq2.subs(y,j)
            temp.append ((i, j, eq3.evalf()))
        tup.append(temp)
    for lists in tup:
        c= curve(pos = lists, radius=0.05)
        
    

master = Tk()
Label(master, text="Enter Formula Here").grid(row = 0)

formula = Entry(master)
formula.grid(row = 0, column = 1)

Button(master, text = 'GRAPH IT!', command = show_formula).grid(row = 2, column = 0)
def main():
    outside = box(color = color.cyan, opacity = 0.0, pos = (0,0,0))
    
    
mainloop()
