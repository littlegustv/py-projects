from pyglet import *

w = window.Window(640,400)

l[0] = text.Label("Hi", x=10,y=10)

@w.event
def on_draw():
    w.clear()
    l[0].draw()

def update(dt):
    txt = l[0].text + "_"
    l[0] = text.Label(txt, x=10, y=10)
    print "what."

clock.schedule_interval(update, 0.1)

app.run()
