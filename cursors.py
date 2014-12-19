import pyglet
import shader
from pyglet.gl import *

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

window = pyglet.window.Window()
image = pyglet.resource.image('seamlessleaft.jpg')
sprite = pyglet.sprite.Sprite(img=image, x=0, y=0)
shader = shader.Shader(vert = ['''

    /* passthrough vertex stage */
    void main()
    {
       gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    }

'''], frag=['''

    /* passthrough fragment stage */
    void main()
    {
       gl_FragColor = gl_Color;
    }
    
'''])



text = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=10, y=10)

@window.event
def on_draw():
    window.clear()
    text.draw()
    shader.bind()
    #shader.uniformf('pixel', 1.0, 1.0)
    sprite.draw()
    shader.unbind()

def update(dt):
    print "yeha."

pyglet.clock.schedule_interval(update, 1/20)
pyglet.app.run()
