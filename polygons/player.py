__author__ = 'littlegustv'

import globals
from polygon import *
from pyglet.window import mouse

class player(polygon):

    def __init__(self):
        self.angle = 0
        self.radius = int(globals.window_width / 25)
        self.x = self.radius + 200
        self.y = globals.window_height / 2
        self.velX = 0
        self.velY = 0
        self.acelX = 0
        self.acelY = 0
        self.alive = True
        self.vertices = []
        self.indexes = []
        self.morphing = 0.0
        self.sides = 6
        self.setVertices()
        self.colors = (30,60,70,255) + (30,45,55,255)*self.sides
        #print self.colors
        self.mouse = (0,0)
        self.target = (0,0)
        self.drawTarget = False

    def setTarget(self):
        x, y = globals.mousePosition
        '''
        a1 = math.atan2(float(y - self.y), float(x - self.x))
        side = 0
        closest = 3.1415
        for n in range(1, self.sides + 1):
            vx = self.vertices[2*n]
            vy = self.vertices[2*n + 1]
            a2 = math.atan2((vy - self.y), (vx - self.x))
            if abs(a2 - a1) < closest:
                side = n
                closest = abs(a2 - a1)
        print "yo"
        self.target = (10 * (self.vertices[side * 2] - self.x), 10 *(self.vertices[side * 2 + 1] - self.y))
        '''
        self.target = (x, y)


    def draw(self):
        graphics.draw_indexed(self.sides + 1, gl.GL_TRIANGLES,
                                  self.indexes,
                      ('v2f', tuple(self.vertices)),
                      ('c4B', self.colors))
        if self.drawTarget:
            pass
            '''
            xfragment = (self.target[0] - self.x) / 100
            yfragment = (self.target[1] - self.x) / 100
            for i in range (5, 100):
                graphics.draw(2, gl.GL_LINES,
                ('v2f', (self.x + xfragment * i + xfragment / 2, self.y + yfragment * i + yfragment / 2, self.x + xfragment * (i + 1), self.y + yfragment * (i + 1))),
                    ('c4B', 2*(150,0,0,255)))
            '''

    def addSide(self, x, y, color):
        self.sides += 1
        self.morphing = 0.5
        self.vertices += [x,y]
        self.indexes.pop()
        self.indexes += [self.sides, 0, self.sides, 1]
        self.colors += color

    def handleCollision(self):
        self.removeSide(1)

    def removeSide(self, side):
        #print "V: ", self.vertices, self.vertices[-1:],self.vertices[len(self.vertices) + 2:]
        self.morphing = 0.5
        if side == 1:
            vtx = self.vertices[2 * self.sides:] + self.vertices[2:6]
        elif side == self.sides:
            vtx = self.vertices[2* self.sides - 2:] + self.vertices[2:4]
        else:
            vtx = self.vertices[2 * side - 2: 2 * side + 4]
        self.vertices = self.vertices[:side * 2] + self.vertices[side * 2 + 2:]     #should be OK
        self.indexes = self.indexes[:len(self.indexes) - 4]
        self.indexes.append(1)
        clr = self.colors[side * 4: side * 4 + 4]
        self.colors = self.colors[:side * 4] + self.colors[side * 4 + 4:]
        self.sides -= 1
        #print "ZOMG", side, vtx, clr
        return vtx, clr