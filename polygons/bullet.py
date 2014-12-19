__author__ = 'littlegustv'

from pyglet import *
from polygon import *
import math

class bullet(polygon):

    def __init__(self, angle, vtx, color = (255,255,255,255)):
        self.x = vtx[2]
        self.y = vtx[3]
        self.angle = angle
        self.velX = math.cos(angle) * 10
        self.velY = math.sin(angle) * 10
        self.alive = True
        self.color = color
        self.vertices = [self.x, self.y] + vtx
        self.indexes = [0,1,2]
        self.sides = 3
        self.radius = 15

    def draw(self):
        graphics.draw(3, gl.GL_TRIANGLES,
                      ('v2f', tuple(self.vertices[2:])),
                      ('c4B', 3 * self.color))

    def update(self, dt):
        ox = self.x
        oy = self.y
        self.x += self.velX
        self.y += self.velY
        for n in range (0, len(self.vertices)):
            if n % 2 == 0:
                self.vertices[n] += (self.x - ox)
                self.vertices[n + 1] += (self.y - oy)

    #def draw(self):
    #    graphics.draw(3, gl.GL_TRIANGLES, ('v2f', tuple(self.vtx)))
        #graphics.draw(2, gl.GL_LINES, ('v2f', (self.x - 15 * math.cos(self.angle), self.y - 15 * math.sin(self.angle),
        #                                       self.x + 15 * math.cos(self.angle), self.y + 15 * math.sin(self.angle))), ('c4B', self.color * 2))

    def handleCollision(self):
        self.alive = False
