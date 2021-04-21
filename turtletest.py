#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Apr 19 00:20:49 2021

@author: sarahnorthover
"""

import turtle
import PIL
from PIL import ImageGrab
import tkinter as tk
import math
import numpy as np
import random

def dump_gui():
    """
    takes a png screenshot of a tkinter window, and saves it on in cwd
    """
    print('...dumping gui window to png')

    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    x1 = x0 + 2*root.winfo_width()
    y1 = y0 + 2*root.winfo_height()
    ImageGrab.grab().crop((x0, y0, x1, y1)).save("gui_image_grabbed1.png")

def draw_sierpinski(length, depth):
    if depth == 0:
        for i in range(0, 3):
            t.fd(length)
            t.left(120)
    else:
        draw_sierpinski(length / 2, depth - 1)
        t.fd(length / 2)
        draw_sierpinski(length / 2, depth - 1)
        t.bk(length / 2)
        t.left(60)
        t.fd(length / 2)
        t.right(60)
        draw_sierpinski(length / 2, depth - 1)
        t.left(60)
        t.bk(length / 2)
        t.right(60)

def quadrilateral(length, width, rotation=0):
    t.right(rotation)
    t.fd(length)
    t.left(90)
    t.fd(width)
    t.left(90)
    t.fd(length)
    t.left(90)
    t.fd(width)
    t.left(90)

def triangle(a, b, c):
    """
    constructs a triangle given three sides. 
    """
    if ((a + b > c) and (a + c > b) and (b + c > a)):
        angle1 = math.acos((b**2 + c**2 - a**2)/(2*b*c))
        angle2 = math.acos((a**2 + c**2 - b**2)/(2*a*c))
        t.forward(b)
        t.left(180 - math.degrees(angle1))
        t.forward(c)
        t.left(180 - math.degrees(angle2))
        t.forward(a)
    else:
        t.forward(0)

def frame(length, width, start_x=-150, start_y=-175):
    t.speed(0)
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    quadrilateral(length, width)

def r_triangle(base, height):
    t.forward(base)
    t.left(90)
    t.forward(height)
    hypotenuse = ((base**2)+(height**2))**0.5
    t.left(180-math.degrees(math.atan(base/height)))
    t.forward(hypotenuse)

def xframepoint(width, start_x):
    x_cor = random.randint(start_x, start_x + length)
    return x_cor

def yframepoint(width, start_y):
    y_cor = random.randint(start_y, start_y + width)
    return y_cor

def rand_size(end):
    return random.randint(20,end)

def change_location():
    t.penup()
    t.goto(xframepoint(length, start_x), yframepoint(width, start_y))
    t.pendown()

def rand_angle():
    return random.randint(0,360)

def rand_rotate():
    guess = random.randint(0,2)
    
    if (guess == 1):
        t.left(rand_angle())
    else:
        t.right(rand_angle())

def concept1():
    for i in range(0, 3):
        change_location()
        rand_rotate()
        r_triangle(rand_size(300), rand_size(200))
        change_location()
        rand_rotate()
        quadrilateral(rand_size(200), rand_size(200))

def concept2():
    t.penup()
    t.goto(-150 + 300/2, -175 + 400/2)
    t.pendown()
    for i in range(0,6):
        t.circle(70)
        t.left(60)

def concept3():
    t.penup()
    t.goto(-150 + 300/2, -175 + 400/2)
    t.pendown()
    for i in range(0, 6):
        quadrilateral(80,80)
        t.left(60)

def concept4():
    for i in range(0, 3):
        change_location()
        rand_rotate()
        triangle(rand_size(300), rand_size(300), rand_size(300))
        change_location()
        rand_rotate()
        quadrilateral(rand_size(200), rand_size(200))

if __name__ == "__main__":
    length = 300 #x
    width = 400 #y
    start_x = -150
    start_y = -175

    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()
    t = turtle.RawTurtle(canvas)
    frame(length,width)  
  
    #draw_sierpinski(400, 6)

    #different ideas: uncomment at will to check them out. 
    # You can experiment with trying more than one concept at a time.

    #concept1()
    #concept2()
    #concept3()
    concept4()
    

    #print(t.pos())
    #triangle(80,70,70)

    t.hideturtle()


    dump_gui()

    root.mainloop()



