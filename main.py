from gamedata import data
import random
from art import logo, vs






finish = True

point = 0

first = random.choice(data)
print(logo)



while finish != False:
    second = random.choice(data)
    print(first['follower_count'])
    print(second['follower_count'])
    print("*****************")
    print("Compera A: "+first['name']+","+first['description'])
    print(vs)
    print("Compare B: "+second['name']+","+second['description'])
    a = input("make a chocie")

    if a == "A":
        if first['follower_count'] > second['follower_count']:
            point += 1
            first = second
        else:
            finish=False
            print(f"You lost your point is {point}")
    else:
        if second['follower_count'] > first['follower_count']:
            point += 1
            first = second
        else:
            finish=False
            print( f"You lost your point is {point}")
