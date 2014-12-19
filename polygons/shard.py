__author__ = 'littlegustv'

from pyglet import *
from polygon import *

class shard(polygon):

    def __init__(self, vtx, color):
        self.x = (vtx[0] + vtx[2] + vtx[4])/3
        self.y = (vtx[1] + vtx[3] + vtx[5])/3
        self.velX = 0
        self.velY = 0
        #self.vtx = tuple(vtx)
        self.alive = True
        self.color = color
        self.sides = 3
        self.angle = 0.0
        self.indexes = [0,1,2,0]
        self.vertices = vtx + [self.x, self.y]
        self.vtx = vtx
        self.radius = 15

    def update(self,dt):
        for n in range(0, len(self.vtx)):
            #even, therefore an X vertex
            if n % 2 == 0:
                xn = self.vtx[n] - self.x
                yn = self.vtx[n + 1] - self.y
                xp = xn * math.cos(self.angle) - yn * math.sin(self.angle) + self.x
                yp = xn * math.sin(self.angle) + yn * math.cos(self.angle) + self.y
                self.vertices[n] = xp
                self.vertices[n+1] = yp

        self.angle -= dt

    def handleCollision(self):
        self.alive = False