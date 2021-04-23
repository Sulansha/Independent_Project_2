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
    it will prompt with 'save as?'
    type after the prompt on the terminal then press enter
    it will use the input to customize the file name.
    """
    save = input("save file?")
    if (save == 'y'):
        print('...dumping gui window to png')
        x0 = root.winfo_rootx()
        y0 = root.winfo_rooty()
        x1 = x0 + 2*root.winfo_width()
        y1 = y0 + 2*root.winfo_height()
        figurename = input("save as?")
        ImageGrab.grab().crop((x0, y0, x1, y1)).save(
            "gui_image_grabbed_" + figurename + ".png")


    
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
    """
    constructs a square/rectangle if given length and width
    """
    t.right(rotation)
    t.fd(length)
    t.left(90)
    t.fd(width)
    t.left(90)
    t.fd(length)
    t.left(90)
    t.fd(width)
    t.left(90)

def kite(a1, a2, b):
    """
    constructs kite when given diagonals
    a1 and a2 - the lengths of each part of main diagonal
    b1 - the lengths of each half of cross diagonal
    """
    side1 = math.sqrt(a1**2 + b**2)
    side2 = math.sqrt(a2**2 + b**2)

    angle1 = math.degrees(math.atan(a1/b)) + math.degrees(math.atan(a2/b))
    angle2 = 2*math.degrees(math.atan(b/a2))

    t.forward(side1)
    t.left(180-angle1)
    t.forward(side2)
    t.left(180-angle2)
    t.forward(side2)
    t.left(180-angle1)
    t.forward(side1)
    t.left(180-angle2)

def hexagon(side):
    """
    constructs a hexagon if given side length
    """
    for i in range(0,5):
        t.forward(side)
        t.left(60)
    
    t.forward(side)

def triangle(a, b, c):
    """
    constructs a triangle given three sides. 
    If the side lengths given cannot construct a triangle, does nothing.
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
    """
    creates the rectangular frame for the piece.

    length - x

    width - y

    start_x - x-coordinate of bottom left of frame

    start_y - y-coordinate of bottom left of frame
    """
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    quadrilateral(length, width)

def r_triangle(base, height):
    """
    draws a right-angled triangle if given base and height
    """
    t.forward(base)
    t.left(90)
    t.forward(height)
    hypotenuse = ((base**2)+(height**2))**0.5
    t.left(180-math.degrees(math.atan(base/height)))
    t.forward(hypotenuse)

def xframepoint(width, start_x):
    """
    gives an x-coordinate inside the frame window
    """
    x_cor = random.randint(start_x + 10, start_x + length -10)
    return x_cor

def yframepoint(width, start_y):
    """
    gives an y-coordinate inside the frame window
    """
    y_cor = random.randint(start_y + 10, start_y + width - 10)
    return y_cor

def rand_size(end):
    """
    gives a random integer from 20 to the specified endpoint
    """
    return random.randint(20,end)

def change_location():
    """
    randomly changes the location of the pointer inside the frame
    """
    t.penup()
    t.goto(xframepoint(length, start_x), yframepoint(width, start_y))
    t.pendown()

def rand_angle():
    """
    returns an integer from 1 to 360 (inclusive)
    """
    return random.randint(0,360)

def rand_rotate():
    """
    rotates the pointer in either the left or right direction a random degree.
    """
    guess = random.randint(0,2)
    
    if (guess == 1):
        t.left(rand_angle())
    else:
        t.right(rand_angle())

def center():
    """
    moves the turtle pointer to the center of the frame
    """
    t.penup()
    t.goto(start_x + length/2, start_y + width/2)
    t.pendown()

def concept1(repeat=4):
    """
    draws randomly created right-triangles and rectangles 

    repeat- number of times the code will loop
            creating a triangle and rectangle each time
    """
    for i in range(0, repeat):
        change_location()
        rand_rotate()
        r_triangle(rand_size(300), rand_size(200))
        change_location()
        rand_rotate()
        quadrilateral(rand_size(200), rand_size(200))

def concept2(rotation_amt = 60,radius = 70, c=1):
    """
    draws rotating circles at the center of the frame

    radius - center of circle

    rotation_amt - the degree the pointer will rotate before drawing the next polygon
    
    c - setting as 1 automatically centers the drawing 
    setting as any other number will not center the drawing
    """
    center()
    for i in range(0,360, rotation_amt):
        t.circle(radius)
        t.left(rotation_amt)


def concept3(rotation_amt=60, length=80, width=80):
    """
    draws rotating quadrilaterals at the center of the frame

    you can select any rotation amt, but it is more pleasing
    to the eye to select one that is divisible by 360.
    """
    center()
    for i in range(0, 360, rotation_amt):
        quadrilateral(length, width)
        t.left(rotation_amt)

def concept4(repeat=4):
    """
    draws randomly created triangles and rectangles
    """
    for i in range(0, repeat):
        change_location()
        rand_rotate()
        triangle(rand_size(300), rand_size(300), rand_size(300))
        change_location()
        rand_rotate()
        quadrilateral(rand_size(200), rand_size(200))

def concept5(radius=100, number=10, color1= 'black', c=1):
    """
    creates the stated concentric number of circles.

    number - distance between consecutive circles

    radius - radius of largest circle

    since it creates circles by filling in with bucket tool, 
    if you would like to use this 
    with other concepts,
    use this one FIRST (it should be the first concept run).
    """
    if (c==1):
        center()
    for diameter in range(radius * 2, 0, -2*number):
        t.dot(diameter, color1)
        t.dot(diameter - 2, 'white')

def concept6(a1, a2, b, rotation_amt=60, times = 5, c=1):
    """
    draws rotating kites at the center of the frame

    times - number of rotations made by the pointer

    c -  setting as 1 centers the piece each time

    rotation_amt - the degree the pointer will rotate
    before drawing the next polygon

    you can select any rotation amt, but it is more pleasing
    to the eye to select one that is divisible by 360.
    """
    if (c==1):
        center()
    for i in range(0, times*rotation_amt, rotation_amt):
        kite(a1, a2, b)
        t.left(rotation_amt)


def concept7(a, b, c, rotation_amt=60, cen=1):
    """
    draws rotating triangles at the center of the frame
    setting center as 1 centers the piece each time

    cen - setting as 1 centers the piece each time
    """
    if (c == 1):
        center()
    for i in range(0, 360, rotation_amt):
        triangle(a,b,c)
        t.left(rotation_amt)

def concept8(side, rotation_amt=180, c=1, times=3):
    """
    draws rotating hexagons at the center of the frame
    setting center as 1 centers the piece each time
    """
    if (c == 1):
        center()
    for i in range(0, times*rotation_amt, rotation_amt):
        hexagon(side)
        t.left(rotation_amt)


if __name__ == "__main__":
    length = 300 #x
    width = 400 #y
    start_x = -150
    start_y = -175

    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()
    t = turtle.RawTurtle(canvas)
    t.speed(0)

    frame(length,width)  

  
    #draw_sierpinski(400, 6)

    # different ideas: uncomment at will to check them out. 
    # You can experiment with trying more than one concept at a time.

    #concept5(number=20)
    #concept1()
    concept2(rotation_amt=30, radius=130)
    concept3(rotation_amt=20, length= 160, width=150)
    concept8(60,80,30, times= 19)
    #concept4()
    for i in range(0,7):
        change_location()
        concept7(50,50,50,rotation_amt=30, cen=0)
    #concept3(rotation_amt=90)
    
    concept8(120)

    #print(t.pos())

    t.hideturtle()

    # uncomment the line below this if you'd like to save the figure
    # you must uncomment it before running the code.
    dump_gui()

    root.mainloop()



