__author__ = 'littlegustv'

from pyglet import *
import globals
import random
import math

class polygon():

    def __init__(self,sides,collisionFunction):
        self.sides = sides
        self.velX = random.randint(-4,-2)
        self.velY = 0
        self.radius = -(globals.window_width / 90) * self.velX
        self.x = globals.window_width - self.radius / 2
        self.y = random.randint(self.radius / 2, globals.window_height - self.radius / 2)
        #self.acelX = -1
        #self.acelY = -1
        self.vertices = []
        self.indexes = []
        self.morphing = 0.0
        self.alive = True
        self.angle = 0.0
        self.setVertices()
        self.color = (random.randint(50,255), random.randint(50,255), random.randint(50,255), 150)
        self.collisionFunction = collisionFunction

    def setVertices(self):
        self.vertices = [self.x, self.y]
        self.indexes = []
        for n in range(0, self.sides):
            xn = self.radius * math.sin(2 * math.pi * n / self.sides) #+ self.x
            yn = self.radius * math.cos(2 * math.pi * n / self.sides) #+ self.y
            xp =  xn * math.cos(self.angle) - yn  * math.sin(self.angle) + self.x
            yp = xn * math.sin(self.angle) + yn * math.cos(self.angle) + self.y

            self.vertices.append(xp)
            self.vertices.append(yp)
            if n < self.sides - 1:
                self.indexes.append(0)
                self.indexes.append(n+1)
                self.indexes.append(n+2)
        self.indexes.append(0)
        self.indexes.append(self.sides)
        self.indexes.append(1)

    def draw(self):
        if self.sides > 2:
            graphics.draw_indexed(self.sides + 1, gl.GL_TRIANGLES,
                                  self.indexes,
                      ('v2f', tuple(self.vertices)),
                      ('c4B', tuple([int(0.85 * x) for x in self.color]) + self.sides * self.color))


    def update(self, dt):
        self.x += self.velX
        self.y += self.velY

        if abs(self.velX) > 0:
            self.angle += dt * -1 * self.velX / 2
        elif abs(self.velY) > 0:
            self.angle += dt * self.velY / 2

        #self.velX += self.acelX
        #self.velY += self.acelY
        if self.morphing >= 0:
            temp_vtx = self.vertices
            self.setVertices()
            for n in range(0,len(temp_vtx)):
                temp_vtx[n] = (temp_vtx[n] + self.vertices[n]) / 2
            self.vertices = temp_vtx
            self.morphing -= dt
        else:
            self.setVertices()
        if self.sides <= 2:
            self.alive = False

    def handleCollision(self):
        self.sides -= 1
        self.morphing = 3.0
        shard_vtx = self.vertices[len(self.vertices) - 4:] + self.vertices[2:4]
        self.collisionFunction(shard_vtx, self.color)
        self.vertices = self.vertices[:len(self.vertices) - 2]
        self.indexes = self.indexes[:len(self.indexes) - 4]
        self.indexes.append(1)