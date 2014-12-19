import string
import random
import time

Goal = [" GGG    OOO    AAA   L    ",
        "G   G  O   O  A   A  L    ",
        "G      O   O  AAAAA  L    ",
        "G  GG  O   O  A   A  L    ",
        " GGG    OOO   A   A  LLLLL"]

Start = ["","","","",""]

letters = string.ascii_letters + " "

for i in range(0,5):
    for j in range(0,len(Goal[0])):
        Start[i] += random.choice(letters)
    print Start[i]

while Start != Goal:
    rCol = random.randint(0, len(Goal[0]) - 1)
    rRow = random.randint(0,4)
    print ""
    if Start[rRow][rCol] != Goal[rRow][rCol]:
        Start[rRow] = Start[rRow][0:rCol] + random.choice(letters) + Start[rRow][rCol + 1:]

    for i in range(0,5):
        print Start[i]
