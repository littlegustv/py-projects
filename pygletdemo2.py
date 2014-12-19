from pyglet import *
import math

window = window.Window(640,480)

def draw_box(x,y,w,h,color=(255,255,255,255), border=0):
    graphics.draw_indexed(4, gl.GL_TRIANGLES,
                          [0,1,2,0,2,3],
                          ('v2i', (x, y,
                            x + w, y,
                           x + w, y + h,
                           x, y + h)),
                          ('c4B', color*4))
    if border > 0:
        graphics.draw_indexed(4, gl.GL_TRIANGLES,
                          [0,1,2,0,2,3],
                          ('v2i', (x + border, y + border,
                            x + w - border, y + border,
                           x + w - border, y + h - border,
                           x + border, y + h - border)),
                          ('c4B', (0,0,0,255)*4))

@window.event
def on_draw():
    draw_box(200,200,50,150,(200,150,200,255),4)

app.run()
