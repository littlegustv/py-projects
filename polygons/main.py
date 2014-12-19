from pyglet import *
from pyglet.window import key
from pyglet.window import mouse
from polygon import *
from shard import *
from player import *
from bullet import *
import random
import math
from globals import *

gl.glEnable(gl.GL_BLEND)
gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

gameState = "Menu"

def iround(n):
    y = round(n) - 0.5
    return int(y) + (y > 0)

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def offscreen(o):
    if o.__class__.__name__ == 'player':
        return False
    return o.x > window.width or o.x < 0 or o.y > window.height or o.y < 0

keys = {'up': False, 'down': False, 'right': False, 'left': False}

game_objects = []
player1 = player()

font.add_file('TulpenOne-Regular.ttf')

title = text.Label("Taking Sides", font_name="Tulpen One", x=100, y=globals.window_height/2, font_size=85)
subtitle = text.Label("Press 'P' to play...", font_name="Tulpen One", x=106, y = globals.window_height/2 - 100, font_size = 38)

menuPolygon = polygon(5,None)
menuPolygon.x = 600
menuPolygon.y = 2 * globals.window_height / 3
menuPolygon.radius =  -(globals.window_width / 10)
menuPolygon.velY = random.randint(-4,4)
menuPolygon.velX = random.randint(-4,4)
menuPolygon.setVertices()

game_objects.append(player1)

def reset():
    global game_objects, player1
    game_objects = []
    player1 = player()
    game_objects.append(player1)

def spawnShard(vtx, color):
    s = shard(vtx, color)
    #print len(game_objects)
    game_objects.append(s)
    #print "@", len(game_objects)

testP = polygon(4,spawnShard)
game_objects.append(testP)

def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def project(axis, obj):
    vertexList = obj.vertices
    length = obj.sides
    min = dot(axis, (vertexList[0], vertexList[1]))
    max = min
    for i in range(1, length + 1):
        v = (vertexList[2*i], vertexList[2*i+1])
        p = dot(axis, v)
        if p < min:
            min = p
        elif p > max:
            max = p

    return (min, max)

def overlap(p1, p2):
    if p1[0] > p2[0] and p1[0] < p2[1] or p1[1] > p2[0] and p1[1] < p2[1]:
        return True
    else:
        return False

def checkCollision(o, o2):
    l = o.sides
    axes1 = []
    vtx = o.vertices[2:]
    #get axis for first object
    for vn in range(0, l):
        #print o.__class__, vn
        start = [vtx[2*vn], vtx[2*vn + 1]]
        vxy = [start[0] - vtx[(2*vn + 2) % len(vtx)], start[1] - vtx[(2*vn + 3) % len(vtx)]]
        axes1.append([-vxy[1],vxy[0]])
        #print vn, start, vxy
    #and for second...

    l = o2.sides
    axes2 = []
    vtx = o2.vertices[2:]

    for vn in range(0, l):
        start = [vtx[2*vn], vtx[2*vn + 1]]
        vxy = [start[0] - vtx[(2*vn + 2) % len(vtx)], start[1] - vtx[(2*vn + 3) % len(vtx)]]
        axes2.append([-vxy[1],vxy[0]])

    notOverlap = False

    for a in axes1:
        p1 = project(a, o)
        p2 = project(a, o2)

        if not overlap(p1, p2):
            notOverlap = True

    for a in axes2:
        p1 = project(a, o)
        p2 = project(a, o2)

        if not overlap(p1, p2):
            notOverlap = True

    if not notOverlap:
        return True
    else:
        return False


@window.event
def on_key_press(symbol, modifiers):
    global gameState
    if symbol == key.W:
        keys['up'] = True
    elif symbol == key.S:
        keys['down'] = True
    elif symbol == key.A:
        keys['left'] = True
    elif symbol == key.D:
        keys['right'] = True

    if symbol == key.P and gameState == "Menu":
        reset()
        gameState = "Play"

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.W:
        keys['up'] = False
    elif symbol == key.S:
        keys['down'] = False
    elif symbol == key.A:
        keys['left'] = False
    elif symbol == key.D:
        keys['right'] = False

@window.event
def on_mouse_motion(x,y,dx,dy):
    globals.mousePosition = (x,y)

@window.event
def on_mouse_drag(x,y,dx,dy, button, modifiers):
    globals.mousePosition = (x,y)

@window.event
def on_mouse_release(x,y, button, modifiers):
    if button == mouse.MIDDLE:
        player1.drawTarget = False

@window.event
def on_mouse_press(x, y, button, modifiers):
    #print player1.x, player1.y
    #for n in range(0, player1.sides):
        #print n, " ::: ", player1.vertices[2 * n + 2], player1.vertices[2 * n + 3], " : ", player1.colors[4*n + 4:4*n+8]
    if button == mouse.MIDDLE:
        player1.drawTarget = True
    if button == mouse.LEFT and player1.sides > 3:
        a1 = math.atan2(float(y - player1.y), float(x - player1.x))
        side = 0
        closest = 3.1415
        a3 = 100
        for n in range(1, player1.sides + 1):
            vx = player1.vertices[2*n]
            vy = player1.vertices[2*n + 1]
            a2 = math.atan2((vy - player1.y), (vx - player1.x))
            if abs(a2 - a1) < closest:
                side = n
                closest = abs(a2 - a1)
                a3 = a2

        vtx, clr = player1.removeSide(side)
        #player1.x + math.cos(angle) * (player1.radius + 4), player1.y + math.sin(angle) * (player1.radius + 4)

        b = bullet(angle = a1, vtx=vtx, color = clr)
        game_objects.append(b)

@window.event
def on_draw():
    window.clear()
    if gameState == "Menu":
        title.draw()
        subtitle.draw()
        menuPolygon.draw()
    elif gameState == "Play":
        game_objects.sort(key=lambda x: x.velX, reverse=True)
        for o in game_objects:
            o.draw()

def update(dt):
    global gameState
    if gameState == "Menu":
        menuPolygon.update(dt)
        if menuPolygon.x > globals.window_width or menuPolygon.x < 0:
            menuPolygon.velX *= -1
        if menuPolygon.y > globals.window_height or menuPolygon.y < 0:
            menuPolygon.velY *= -1
    elif gameState == "Play":
        #SPAWNING ENEMIES
        if random.randint(0,100) < 5 and len(game_objects) < 20:
            pn = polygon(5, spawnShard)
            game_objects.append(pn)

        for o in game_objects:
            o.update(dt)
        player1.setTarget()

        if keys['up']:
            player1.velY = 9
        elif keys['down']:
            player1.velY = -9
        else:
            player1.velY = 0
        if keys['right']:
            player1.velX = 9
        elif keys['left']:
            player1.velX = -9
        else:
            player1.velX = 0

        #collisions:

        for o in game_objects:
            for o2 in game_objects:
                if o is o2:
                    continue
                elif o.__class__ == o2.__class__:
                    continue
                #elif distance(o.x, o.y, o2.x, o2.y) > 2*(o.radius + o2.radius):
                #    continue
                else:
                    if checkCollision(o, o2):
                        if o.__class__.__name__ == 'bullet' and o2.__class__.__name__ == 'polygon':
                            o.handleCollision()
                            o2.handleCollision()
                        if o.__class__.__name__ == 'shard' and o2.__class__.__name__ == 'player':
                            o.handleCollision()
                            player1.addSide(o.x, o.y, o.color)
                        if o.__class__.__name__ == 'polygon' and o2.__class__.__name__ == 'player':
                            player1.handleCollision()
                            game_objects.remove(o)

        for o in game_objects:
            if o.__class__.__name__ is not "player":
                if o.x > globals.window_width:
                    o.x = 0
                elif o.x < 0:
                    o.x = globals.window_width
                if o.y > globals.window_height:
                    o.y = 0
                elif o.y < 0:
                    o.y = globals.window_height
            if not o.alive:
                game_objects.remove(o)
                del(o)
        if player1.sides < 3:
            gameState = "Menu"
clock.schedule_interval(update, 0.02)
    
app.run()
