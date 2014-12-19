from pyglet import *
from pyglet.window import key

def drawbox(x,y,width,height,color=(255,255,255,255)):
     graphics.draw_indexed(4, gl.GL_TRIANGLES,
                      [0,1,2,0,2,3],
                      ('v2f', (x,y,
                               x + width, y,
                               x + width, y + height,
                               x, y + height)),
                              ('c4B', color * 4))  

keys = {
    "Up": False,
    "Down": False
}

px = 10
py = 100

bx = 360
by = 200

velX = -5
velY = 5

wx = 315
wy = 200

window = window.Window(640,480)

def reset():
    global px, py, bx, by, velX, velY
    px = 10
    py = 100

    bx = 300
    by = 200

    velX = 5
    velY = 5

@window.event
def on_draw():
    window.clear()
    drawbox(px,py,10,100)
    drawbox(bx,by,10,10)
    drawbox(wx,wy,10,80)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        keys['Up'] = True
    elif symbol == key.DOWN:
        keys['Down'] = True

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.UP:
        keys['Up'] = False
    elif symbol == key.DOWN:
        keys['Down'] = False

def update(dt):
    global px,py,bx,by,velX,velY
    bx += velX
    by += velY
    #ball collisions
    if by > window.height - 10 or by < 0:
        velY *= -1
    if bx > window.width - 10:
        velX *= -1
    #collide with paddle
    if bx > 10 and bx < 20 and by > py and by < py + 100:
        velX *= -1
    elif bx < 0:
        reset()
    #collide with wall
    if bx + 10 > wx and bx < wx + 10 and by + 10 > wy and by < wy + 80:
        velX *= -1
        velY *= -1
        
    if keys['Up']:
        py += 5
    elif keys['Down']:
        py -= 5
        
clock.schedule_interval(update, 0.01)

app.run()
