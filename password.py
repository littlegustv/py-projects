import timeit
import string
import random

global hidden_word
hidden_word = "Swordfish"

letter_set = string.ascii_letters

global guess
global i

guess = "123456789"
i = 0

print guess

while guess != hidden_word and i< 2:
    max_time = 0
    picked_letter = ''
    for l in letter_set:
        lower = max(0, i-1)
        stmt = "'" + guess[0:i] + l + guess[i+1:] + "' == '" + hidden_word + "'"
        t = timeit.timeit(stmt, number=100000)
        print t, l, stmt
        if t > max_time:
            #print t, max_time, l, stmt
            picked_letter = l
            max_time = t
    g_list = list(guess)
    print i
    g_list[i] = picked_letter
    guess = "".join(g_list)
    print guess
    i += 1
