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


def dump_gui():
    """
    takes a png screenshot of a tkinter window, and saves it on in cwd
    """
    print('...dumping gui window to png')

    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    x1 = x0 + root.winfo_width()
    y1 = y0 + root.winfo_height()
    ImageGrab.grab().crop((x0, y0, x1, y1)).save("gui_image_grabbed.png")


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

def quadrilateral(length, width, rotation):
    t.right(rotation)
    t.fd(length)
    t.left(90)
    t.fd(width)
    t.left(90)
    t.fd(length)
    t.left(90)
    t.fd(width)

def r_triangle(base, height):
    t.forward(base)
    t.left(90)
    t.forward(height)
    hypotenuse = ((base**2)+(height**2))**0.5
    t.left(180-math.degrees(math.atan(base/height)))
    t.forward(hypotenuse)

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    t = turtle.RawTurtle(canvas)
    t.speed(0)
    t.penup()
    t.goto(-200, -175)
    t.pendown()
    #draw_sierpinski(400, 6)
    r_triangle(300,200)
    t.hideturtle()

    dump_gui()

    root.mainloop()



