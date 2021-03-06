'''
Created on Aug 3, 2016

@author: Rykath
Package: Main.Data

Usage: class for single patterns
'''

import Utilities.map
import Main.settings
import Main.Engine.basic

class Pattern():
    type = "simple-pattern"
    scope = "internal"
    
    def __init__(self,ID):
        self.id = ID
        self.name = None
        self.computeLvl = 0
        
        # layers
        self.mapL = Utilities.map.Layers()    # dead,living | 0,1
        self.mapC = Utilities.map.Layers()    # cell count  | 0-8
        self.rep = None     # point of repetition | end of pattern = state no REP
    
    def input(self,name=None,array=None):
        if name != None:
            self.name = name
        if array != None:
            self.mapL.addLayer(Utilities.map.Map2D(array=array,default=Main.settings.MapLdef,valid=Main.settings.MapLval).shrink(False)[1])
    
    def compute(self):
        iteration = 0
        done = False
        while not done and iteration < Main.settings.CmptMaxIter:
            # add next generation
            o = Main.Engine.basic.getNxtGen(self.mapL.getLayer(-1,mutate=False).expand(four=1,mutate=False)).shrink(False)
            d = [1-i for i in o[0][0]]
            for i in range(self.mapL.size):
                if o[1].array == self.mapL.getLayer(i).array:
                    self.rep = i
            if self.rep == None:
                self.mapL.addLayer(o[1],off=d)
            iteration += 1

'''
class Pattern_old():
    type = "simple-pattern"
    scope = "internal"
    
    def __init__(self,ID):
        self.id = ID
        self.name = None
        self.computeLvl = 0
        
        self.mapL = None    # dead,living | 0,1
        self.mapC = None    # cell count  | 0-8
    
    def input(self,name=None,array=[[]]):
        if name != None:
            self.name = name
        if array != [[]]:
            self.mapL = Utils.Map(dimension=3,size=[1,len(array[0]),len(array)],default=0,valid=[0,1])
            for y in range(len(array)):
                for x in range(len(array[0])):
                    if array[y][x] == 1:
                        self.mapL.set([x,y],1)
    
    def compute(self):
        if self.computeLvl == 0 and self.mapL != None:
            pass    # compute pattern-type and next generations
        if self.mapL != None:
            self.mapC = Utils.Map(dimension=self.mapL.dimension,size=self.mapL.size,default=0,valid=list(range(9)))
            # assuming dimension = 3 (t,x,y)
            for p in range(len(self.mapC.size[0])):
                for x in range(len(self.mapC.size[1])):
                    for y in range(len(self.mapC.size[2])):
                        v = 0
                        for X in range(-1,2):
                            for Y in range(-1,2):
                                a = self.mapL.get([p,x+X,y+Y])
                                if a != None and (X,Y) != (0,0):
                                    v += a
                        self.mapC.set([p,x,y],v)
'''
