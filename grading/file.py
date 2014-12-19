import time

Name = raw_input ("what is your name? ")
Food = raw_input ("what is tyour favorite food? ")
Game = raw_input ("what is your favorite game to play? ")
Music = raw_input ("what is your favorite song? ")


rooms = [
    [0,1,2,],
    [3,4,5,],
    [6,7,8,]
    ]

myList = [

     {
        "Name": "gaming room",
        "Description": "its has a triple monitor gaming setup with the most powerful pc in the world",
        "Items" :["mouse","keyboard","call of duty","gaming laptop"],
        "Locked": True,
        "Key": "MC",
        },
    {
        "Name": "watermalon room",
        "Description": "This room is made out of watermalon the walls are made out of water malon and there are coolers full of watermalon",
        "Items": ["watermalon"],
        "Locked" :True,
        "key": "red",
        },
    {
        "Name": "poutine room",
        "Description": "this room looks like a normal dining room put the table is full of poutine and all the coberts are filled with poutines",
        "Items": ["poutine"],
        "Locked": False,
        "Key": "chesse",
        },
    {
        "Name": "koolaid room",
        "Description": "this room hsa pools full of koolaid",
        "Items": ["koolaid"],
        "Locked": False,
        "Key": "red2",
        },
    {
        "Name": "music room",
        "Description": "this room has the best sterio system in the world with speakers 9 foot tall and an unlimited collection of music",
        "Items" :["speakers sterio"],
        "locked": True,
        "Key": "black",
        },
    {
        "Name": "pizza",
        "Description" :"this room has pizza covered walls with pizza boxes everywhere",
        "Items" :["pizza"],
        "Locked" :True,
        "Key": "peparoni",
        },
    {
        "Name": "KFC",
        "Description": "this room is the resterunt KFC in a room",
        "Items" :["Chicken"],
        "Locked": False,
        "Key": "Brown",
        },
    {
        "Name": "pepsi",
        "Description": "this room is has pools full of pepsi",
        "Items" :["pepsi"],
        "Locked" :True,
        "Key": "pop",
        },
    {
        "Name": "Movie room",
        "Description" :"this room is a theator i a room",
        "Items" :["soda"],
        "Locked" :True,
        "Key": "screen",
        }
        ]

cRow = 0
cColumn = 0
current = 0

done = False

inventory = []

def prompt ():
    x = raw_input()
    return False

def CheckLocked (roomNumber):
    if myList[roomNumbe]["Locked"]:
        if myList[roomNumber]["Key"] is inventory:
            return False
        else:
            return True

endRoom = 8

inventory = []

current = 0

while not done:
    command = raw_input("Command: ")
    if command == "look":
        print rooms [current]["Name"]
        print rooms[current]["Description"]
        print "Items:"
        for i in rooms[current]["Items:"]:
            print i
    elif command == "inventory":
        for i in inventory:
            print i
    elif command[:3] == "get":
        arg = command [4:]
        if arg in rooms[current]["items:"]:
            rooms[current]["items:"].remove (arg)
            inventory.append(arg)
    elif command[:4] == "drop":
        arg = command [5:]
        if arg in inventory:
            inventory.remove (arg)
            rooms[current]["items:"].append(arg)
    elif command == "say":
        say = raw_input("Say:")
        print "you say " + say
    elif command == "forward":
        if rooms[current+1]["locked"]:
            key = rooms[current+1]["key"]
            if key in inventory:
                print "run run run "
                current += 1
            else:
                print "da key is close"
        else:
                cRow += 1
    elif current == 8:
        print "u going to KFC gg"
        print "get dat chicken..."
        done = True
    elif command == "help":
        print " Do : forward, feed, grab [item name], see, and, inventory get going"
    elif command[3:] == "eat":
        arg = command [:4]
        if arg in inventory:
            if arg == "MC":
                print "red!"
            elif arg == "chesse":
                print "red"
            elif arg == "MC":
                print "red"
            elif arg == "peparoni":
                print "red"
            elif arg == "chesse":
                print "soda"
            elif arg == "Red":
                print "red"
            elif arg == "brown":
                print "MC"
            elif arg == "black":
                print "pop"
            elif arg == "soda":
                print " gg"
            else:
                "gg bud!"
        

        
