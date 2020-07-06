from math import *
class point:
    def __init__ (self,a,b):
        self.x = a
        self.y = b
    def __str__(self):
        return('('+(self.x)+ ',' +(self.y)+')')
    def translate(self,deltax,deltay):
        self.x += deltax
        self.y += deltay
