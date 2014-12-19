from pyglet import *
import random

window = window.Window(640,480)

class gameobject():

    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.velX = 0
        self.velY = 0
        self.color = (255,255,255,255)

    def draw(self):
        graphics.draw_indexed(4, gl.GL_TRIANGLES,
                              [0,1,2,0,2,3],
                              ('v2f', (self.x, self.y,
                                       self.x + self.w, self.y,
                                       self.x + self.w, self.y + self.h,
                                       self.x, self.y + self.h)),
                              ('c4B', self.color*4))

    def update(self, dt):
        self.x += self.velX
        self.y += self.velY

    def moveup(self):
        self.velY = 5

    def movedown(self):
        self.velY = -5

    def stop(self):
        self.velY = 0
        
player1 = gameobject(0,240,16,80)
player2 = gameobject(window.width - 16, 240, 16, 80)

ball = gameobject(285,235,16,16)
ball.velX = -8
ball.velY = 8
ball.color = (180,180,180,255)

middle = gameobject(315,0,10,480)

alert = text.Label("", font_size=45, x=10, y=420)
p1 = text.Label("", font_size=45, x=40, y=420)
p2 = text.Label("", font_size=45, x=350, y=420)

time = 0.0
state = 'play'

scores = [0,0]

@window.event
def on_draw():
    window.clear()
    if state == 'play':
        middle.draw()
        ball.draw()
        player1.draw()
        player2.draw()
        p1.draw()
        p2.draw()
    alert.draw()

def update(dt):
    global time, state
    if state == 'play':

        if scores[0] >= 11 and scores[0] - scores[1] >= 2:
            alert.text = "Player 1 Wins."
            state = "end"
            return
        elif scores[1] >= 11 and scores[1] - scores[0] >= 2:
            alert.text = "Player 2 Wins."
            state = "end"
            return
        
        if ball.y > window.height - ball.h:
            ball.y = window.height - ball.h
            ball.velY *= -1
        elif ball.y < 0:
            ball.y = 0
            ball.velY *= -1

        if ball.x > window.width - ball.w:
            scores[0] += 1
            ball.x = 290
        elif ball.x < 0:
            scores[1] += 1
            ball.x = 350

        p1.text = "P1: " + str(scores[0])
        p2.text = "P2: " + str(scores[1])

        player1.update(dt)
        player2.update(dt)
        ball.update(dt)
        
        #check if collides with player
        for p in [player1, player2]:
            if ball.x < p.x + p.w and ball.x + ball.w > p.x:
                if ball.y < p.y + p.h and ball.y + ball.h > p.y:
                    cx = p.x + p.w / 2
                    cy = p.y + p.h / 2

                    bcx = ball.x + ball.w / 2
                    bcy = ball.y + ball.h / 2

                    if abs(bcx -cx) / float(p.w) > abs(bcy - cy) / float(p.h):
                        ball.velX *= -1
                        if ball.x < p.x:
                            ball.x = p.x - ball.w
                        else:
                            ball.x = p.x + p.w
                    else:
                        ball.velY *= -1
                        if ball.y < p.y:
                            ball.y = p.y - ball.h
                        else:
                            ball.y = p.y + p.h

        #player1
        if ball.velX < 0:
            if ball.y > player1.y + player1.h and player1.y < window.height - player1.h:
                player1.moveup()
            elif ball.y < player1.y and player1.y > 0:
                player1.movedown()
            elif ball.y > player1.y + player1.h / 4 and ball.y < player1.y + 3 * player1.h /4:
                player1.stop()
        else:
            player1.stop()
        
        if ball.velX > 0:
            if ball.y > player2.y + player2.h and player2.y < window.height - player2.h:
                player2.moveup()
            elif ball.y < player2.y and player2.y > 0:
                player2.movedown()
            elif ball.y > player2.y + player2.h / 4 and ball.y < player2.y + 3 * player2.h /4:
                player2.stop()
        else:
            player2.stop()
        """
        if ball.velX > 0:
            step = abs(ball.x - window.width) / abs(ball.velX)
            prediction = ball.y + ball.velY * step
            if prediction > window.height:
                prediction = prediction - (prediction - window.height)
            if prediction < 0:
                prediction = -1 * prediction
            if prediction > player2.y + player2.h:
                player2.moveup()
            elif prediction < player2.y:
                player2.movedown()
            elif prediction > player2.y + player2.h / 4 and prediction < player2.y + 3 * player2.h /4:
                player2.stop()
        else:
            player2.stop()
        """
         

clock.schedule_interval(update, 0.02)

app.run()

