import time
num = 23897543974039820438

factors = []

lower = 2
upper = num
number = num

while True:
    if number <= 1:
        break
    elif upper <= lower:
        factors.append(number)
        break
    elif number % lower == 0:
        print lower
        factors.append(lower)
        upper = number / lower
        number = number / lower
    else:
        lower += 1
        upper = number / lower
