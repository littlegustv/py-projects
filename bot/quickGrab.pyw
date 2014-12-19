"""

Screen Resolution: 1600x900
Chrome 'docked' on left side of screen
    - Bookmarks Toolbar enabled.
    - Scrolled to top of screen

"""

import ImageGrab
import os
import time

# Globals
# *******

x_pad = 37
y_pad = 257

def screenGrab():
    box = (x_pad + 1,y_pad + 1,x_pad + 640, y_pad + 480)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    
def main():
    screenGrab()

if __name__ == '__main__':
    main()

#38, 258
#678, #738
