import numpy as np
import turtle as t

class quadrilateral:
    def __init__(self, length, width):
        self.length = length #x-coordinate
        self.width = width #y-coordinate
        self.position =  np.array([[t.pos(), t.pos()+ length],[t.pos(), t.pos() + width]])

    def draw(self):
        t.fd(self.length)
        t.left(90)
        t.fd(self.width)
        t.left(90)
        t.fd(self.ength)
        t.left(90)
        t.fd(self.width)
        t.left(90)
    
    def inside(self, x_cor, y_cor):
        if ((self.position[0][0] < x_cor < self.position[0][1]) and ((self.position[1][0] < y_cor < self.position[1][1]))):
            return True
        return False
