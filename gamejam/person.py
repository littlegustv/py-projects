import gameobject
from pyglet import *
from pyglet import font

class person (gameobject.gameobject):

    def __init__(self, floor, destFloor, name="", faction="Neutral"):
        
        self.floor = floor
        self.destFloor = destFloor
        self.y = (floor + 1)* 50
        self.x = 200
        self.width = 10
        self.height = 20
        self.floorLabel = text.Label('', 
                          font_name='VT323', 
                          font_size=16,
                          x=self.x + self.width/2, y=self.y + self.height,
                          width=10, color=(0,0,0,255), bold=True)
        self.waiting = 0.1
        self.highlight = False
        self.name = name
        self.faction = faction
        if faction == "Opener":
            self.color = (150,220,150,255)
        elif faction == "Closer":
            self.color = (150,150,220,255)
        else:
            self.color = (200,200,200,255)

    def draw(self):
        graphics.draw_indexed(4, gl.GL_TRIANGLES,
                      [0,1,2,0,2,3],
                      ('v2f', (self.x,self.y,
                               self.x + self.width, self.y,
                               self.x + self.width, self.y + self.height,
                               self.x, self.y + self.height)),
                              ('c4B', self.color * 4))
        self.floorLabel.draw()
        if self.highlight > 0:
            graphics.draw(3, gl.GL_TRIANGLES,
                        ('v2f', (self.x + 2, self.y + self.height + 10,
                                 self.x + self.width - 2, self.y + self.height + 10,
                                 self.x + self.width/2, self.y + self.height + 2)),
                        ('c4B', (220,0,0,255)*3))
            '''graphics.draw_indexed(4, gl.GL_LINES,
                          [0,1,1,2,2,3,3,0],
                          ('v2f', (self.x - 4, self.y - 4,
                                   self.x + self.width + 4, self.y - 4,
                                   self.x + self.width + 4, self.y + self.height + 4,
                                   self.x - 4, self.y + self.height + 4)),
                          ('c4B', (255,0,0,255)*4))
            graphics.draw_indexed(4, gl.GL_LINES,
                          [0,1,1,2,2,3,3,0],
                          ('v2f', (self.x - 3, self.y - 3,
                                   self.x + self.width + 3, self.y - 3,
                                   self.x + self.width + 3, self.y + self.height + 3,
                                   self.x - 3, self.y + self.height + 3)),
                          ('c4B', (255,0,0,255)*4))
            '''

    def update(self, dt):
        self.floorLabel.text = str(self.destFloor)
        self.floorLabel.x = self.x
        self.floorLabel.y = self.y + 4
        if not self.floor == self.destFloor:
            self.waiting += dt
        '''
        if self.waiting > 16:
            self.color = (200,50,50,255)
        elif self.waiting > 12:
            self.color = (200,100,100,255)
        elif self.waiting > 6:
            self.color = (200,150,150,255)
        else:
            self.color = (200,200,200,255)
        '''
        if self.highlight >= 0:
            self.highlight -= dt
