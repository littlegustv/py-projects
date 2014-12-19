"""

Screen Resolution: 1600x900
Chrome 'docked' on left side of screen
    - Bookmarks Toolbar enabled.
    - Scrolled to top of screen

"""

import ImageGrab
import os
import time
import win32api, win32con
import ImageOps
from numpy import *

# Globals
# *******

x_pad = 37
y_pad = 257

foodOnHand = {
'shrimp':5,
'rice':10,
'nori':10,
'roe':10,
'salmon':5,
'unagi':5
    }

sushiTypes = {
3000: 'gunkan',
3073: 'onigiri',
3330: 'caliroll'
    }

class Blank:
    seat1 = 5970
    seat2 = 5180
    seat3 = 9855
    seat4 = 9642
    seat5 = 5527
    seat6 = 7655

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
    print "Click."

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.1)
    print "Left Down."

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
    time.sleep(0.1)
    print "Left Up."

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x, y

def grab():
    box = (x_pad + 1,y_pad + 1,x_pad + 640, y_pad + 480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    return a

def screenGrab():
    box = (x_pad + 1,y_pad + 1,x_pad + 640, y_pad + 480)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def startGame():
    #Play
    mousePos((316,190))
    leftClick()
    time.sleep(0.1)

    #Continue
    mousePos((376,390))
    leftClick()
    time.sleep(0.1)

    #Skip
    mousePos((565,461))
    leftClick()
    time.sleep(0.1)

    #Skip
    mousePos((345,385))
    leftClick()
    time.sleep(0.1)

# 25,63 : 64x11
#126,63
#227,63
#328,63
#429,63
#530,63

def getSeatOne():
    box = (x_pad + 25,y_pad + 63,x_pad + 25+64,y_pad + 63+11)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')    
    return a
            
def getSeatTwo():
    box = (x_pad + 126,y_pad + 63,x_pad + 126+64,y_pad + 63+11)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')    
    return a
            
def getSeatThree():
    box = (x_pad + 227,y_pad + 63,x_pad + 227+64,y_pad + 63+11)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def getSeatFour():
    box = (x_pad + 328,y_pad + 63,x_pad + 328+64,y_pad + 63+11)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def getSeatFive():
    box = (x_pad + 429,y_pad + 63,x_pad + 429+64,y_pad + 63+11)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def getSeatSix():
    box = (x_pad + 530,y_pad + 63,x_pad + 530+64,y_pad + 63+11)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def getAllSeats():
    getSeatOne()
    getSeatTwo()
    getSeatThree()
    getSeatFour()
    getSeatFive()
    getSeatSix()

class Cord:

    f_shrimp = (41,337)
    f_rice = (97,331)
    f_nori = (46,392)
    f_roe = (87,393)
    f_salmon = (25,442)
    f_unagi = (100,444)

    phone = (573,358)

    menu_rice = (545,294)
    buy_rice = (542,290)

    menu_toppings = (558,277)

    t_shrimp = (499,227)
    t_unagi = (575,227)
    t_nori = (509,270)
    t_roe = (564,276)
    t_salmon = (502,329)
    t_exit = (597, 339)

    delivery_norm = (488,301)

"""

Plate Cords:

88 213
177 210
278 217
384 210
494 216
592 212

"""

def clearTables():
    mousePos((88,213))
    leftClick()

    mousePos((177,219))
    leftClick()

    mousePos((278,217))
    leftClick()

    mousePos((384,210))
    leftClick()

    mousePos((494,216))
    leftClick()

    mousePos((592,212))
    leftClick()
    time.sleep(1)

def makeFood(food):
    if food == 'onigiri':
        print "making onigiri"
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(0.1)
        foldMat()
        time.sleep(1.5)
    if food == 'caliroll':
        print "making caliroll"
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(0.1)
        foldMat()
        time.sleep(1.5)
    if food == 'gunkan':
        print "making gunkan"
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        foodOnHand['roe'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(0.1)
        foldMat()
        time.sleep(1.5)

def foldMat():
    mousePos((Cord.f_rice[0] + 40, Cord.f_rice[1]))
    leftClick()
    time.sleep(.1)

def buyFood(food):

    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.1)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (127,127,127):
            print "Rice Available"
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            foodOnHand['rice'] += 10
            time.sleep(3.5)
        else:
            print "Rice NOT Available"
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    elif food == 'shrimp':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_shrimp) != (127,127,127):
            print "Shrimp Available"
            mousePos(Cord.t_shrimp)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            foodOnHand['shrimp'] += 5
            time.sleep(3.5)
        else:
            print "Shrimp NOT Available"
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    elif food == 'unagi':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_unagi) != (94,49,8):
            print "Unagi Available"
            mousePos(Cord.t_unagi)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            foodOnHand['unagi'] += 5
            time.sleep(3.5)
        else:
            print "Unagi NOT Available"
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
            
    elif food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_nori) != (33,30,11):
            print "Nori Available"
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            foodOnHand['nori'] += 10
            time.sleep(3.5)
        else:
            print "Nori NOT Available"
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    elif food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_roe) != (109,123,127):
            print "Roe Available"
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            foodOnHand['roe'] += 10
            time.sleep(3.5)
        else:
            print "Roe NOT Available"
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    elif food == 'salmon':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_unagi) != (127,71,47):
            print "Salmon Available"
            mousePos(Cord.t_unagi)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            foodOnHand['salmon'] += 5
            time.sleep(3.5)
        else:
            print "Salmon NOT Available"
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
            
#    mousePos(Cord.t_shrimp)
#    mousePos(Cord.t_nori)
#    mousePos(Cord.t_roe)
#    mousePos(Cord.t_salmon)
#    mousePos(Cord.t_unagi)
#    mousePos(Cord.t_exit)
    
#    mousePos(Cord.menu_rice)
#    mousePos(Cord.buy_rice)

#    mousePos(Cord.d_normal)

def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print i + " is low and needs restock..."
                buyFood(i)
        else:
            if j <= 2:
                print i + "is low and needs return the ranks..."
                buyFood(i)

def checkBubbles():

    checkFood()
    s = getSeatOne()
    if s != Blank.seat1:
        if sushiTypes.has_key(s):
            print 'seat 1 occupied and needs ' + sushiTypes[s]
            makeFood(sushiTypes[s])
        else:
            print "sushi unknown of type: " + str(s)

    clearTables()
    checkFood()
    s = getSeatTwo()
    if s != Blank.seat2:
        if sushiTypes.has_key(s):
            print 'seat 1 occupied and needs ' + sushiTypes[s]
            makeFood(sushiTypes[s])
        else:
            print "sushi unknown of type: " + str(s)

    clearTables()
    checkFood()
    s = getSeatThree()
    if s != Blank.seat3:
        if sushiTypes.has_key(s):
            print 'seat 1 occupied and needs ' + sushiTypes[s]
            makeFood(sushiTypes[s])
        else:
            print "sushi unknown of type: " + str(s)

    clearTables()
    checkFood()
    s = getSeatFour()
    if s != Blank.seat4:
        if sushiTypes.has_key(s):
            print 'seat 1 occupied and needs ' + sushiTypes[s]
            makeFood(sushiTypes[s])
        else:
            print "sushi unknown of type: " + str(s)

    clearTables()   
    checkFood()
    s = getSeatFive()
    if s != Blank.seat5:
        if sushiTypes.has_key(s):
            print 'seat 1 occupied and needs ' + sushiTypes[s]
            makeFood(sushiTypes[s])
        else:
            print "sushi unknown of type: " + str(s)

    clearTables()
    checkFood()
    s = getSeatSix()
    if s != Blank.seat6:
        if sushiTypes.has_key(s):
            print 'seat 1 occupied and needs ' + sushiTypes[s]
            makeFood(sushiTypes[s])
        else:
            print "sushi unknown of type: " + str(s)

    clearTables()  
def main():
    #screenGrab()
    startGame()
    while True:
        checkBubbles()
    print "main"
    
if __name__ == '__main__':
    main()

#38, 258
#678, #738
