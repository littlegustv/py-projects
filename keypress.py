import thread
import time

number = 1

def update():
    global number
    number += 1
    time.sleep(0.1)
    update()

def user_input():
    global number
    print number
    x = raw_input("Do it? ")
    if x == 'y' or x == 'Y':
        number -= 10
    user_input()
    
thread.start_new_thread(update, ())
thread.start_new_thread(user_input, ())
