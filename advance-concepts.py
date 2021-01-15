import os
import sys
#from MyModule import include foo, bar, foobar

def my_function(one, two,
                three, four,
                five, six):
    print("Hello..!!")

# 2 white lines between 2 different function
def second_function():
    print("Second function")


my_list = [1, 2,
           3, 4,
           5, 6]
#print(my_list[2])

#usage of white space
x = 3*52 + 7*2

check = True

#if check is True:
#    print("This is true")

import random

playerhp = 260
enemyattacklow = 60
enemtattackhigh = 80

# usage for breaking while loop
while playerhp > 0:
    dmg = random.randrange(enemyattacklow, enemtattackhigh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30
        break

    # for empty lock of code use pass
    #if playerhp <= 30:
        #pass

    print("Enemy strikes for ", dmg, "points of damage. Current HP is", playerhp)

    if playerhp == 30:
        print("You have low health...!!")

    # usage of continue
    if playerhp > 30:
        continue




