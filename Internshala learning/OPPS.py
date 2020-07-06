# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:32:59 2020

@author: Gaurav
"""

class person:
    counter = 0
    def __init__(self,a,b):
        self.name = a
        self.gender = b
        person.counter+=1
    def showinfo(self):
        print('name: ',self.name)
        print('gender: ',self.gender)
    @classmethod
    def showcounter(cls):
        print('No of object created so far: ',cls.counter)
        
#geter and seter method
class car:
    def __init__(self,a=40):
        self.speed = a
    def get_speed(self):
        return self._speed
    def set_speed(self,a):
        if a<=0 or a>=160:
            print("speed needs to between 0 to 160")
        else:    
            self._speed=a
        return
    speed = property(get_speed,set_speed)
