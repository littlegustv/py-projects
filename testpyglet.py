import pyglet
import random

window = pyglet.window.Window()
label = pyglet.text.Label('', 
                          font_name='Times New Roman', 
                          font_size=18,
                          x=window.width//2, y=window.height,
                          anchor_x='center', anchor_y='center', width=window.width, multiline=True)


road = "############          ############"

@window.event
def on_draw():
    window.clear()
    label.draw()

def update(dt):
    global road
    r = random.randint(0,10)
    if r > 7:
        road = road[1:] + road[:1]
    elif r < 4:
        road = road[len(road)-1:] + road[:len(road) - 1]
    label.text += "\n" + road

pyglet.clock.schedule_interval(update, (1/5.0))
pyglet.app.run()
