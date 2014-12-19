import random

class room():

    
    def __init__(self, name, desc):
        self.exits = [None, None, None, None, None, None]
        self.name = name
        self.desc = desc

#setup
directions = ['Up', 'Down', 'North', 'South', 'East', 'West']

keywords = ['Red','Living','Reading','Study','Guest','Bed']

rooms = [room(keywords[random.randint(0,len(keywords)-1)] + " Room", "This room is appropriately themed.") for i in range(0,1)]

for i in range (0, 20):
    #create room
    c = keywords[random.randint(0,len(keywords) - 1)]
    temp_room = room(c + " Room", "This room is " + c + " themed")
    #choose exit
    e = random.randint(0,5)
    while temp_room.exits[e] is not None:
        e = random.randint(0,5)
    #choose room it is linked to
    d = random.randint(0,len(rooms) -1)
    temp_room.exits[e] = rooms[d]
    if e % 2 == 0:
        rooms[d].exits[e + 1] = temp_room
    else:
        rooms[d].exits[e - 1] = temp_room
    rooms.remove(rooms[d])
    rooms.append(temp_room)

current  = rooms[0]

while True:
    print current.name
    command = raw_input("? ")
    if command == "look":
        print current.desc
        for i in range(0,6):
            if current.exits[i] is not None:
                print "[" + directions[i] + "] " + current.exits[i].name
    elif command in "udnsew" and len(command) == 1:
        e = "udnsew".index(command)
        if current.exits[e] is not None:
            print "You move " + command + "."
            current = current.exits[e]
        else:
            print "You can't go that way."
