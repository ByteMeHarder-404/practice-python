# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 17:29:32 2025

@author: Akshat Bhalani
"""

import random,sys,time

ALLCLOSED="""

+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+"""

FIRSTCLOSED="""

+------+  +------+  +------+
|      |  |      |  |      |
| GOAT |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+ """

SECONDCLOSED="""

+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  | GOAT |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+ """

THIRDCLOSED="""

+------+  +------+  +------+
|      |  |      |  |      |
| 1    |  |   2  |  | GOAT |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+ """

WINNING=["""

+------+  +------+  +------+
|      |  |      |  |      |
| CAR  |  | GOAT |  | GOAT |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+ """,
"""
+------+  +------+  +------+
|      |  |      |  |      |
| GOAT |  | CAR  |  | GOAT |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+ """,
"""
+------+  +------+  +------+
|      |  |      |  |      |
| GOAT |  | GOAT |  | CAR  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+ """]

print("Let's Make a DEAL")
swapwins=0
swaplosses=0
staywins=0
staylosses=0
while True:
    swap=0
    stay=0
    carDoor=random.randint(1,3)
    print(ALLCLOSED)
    while True:
        print('Pick a door 1,2,3 or quit:')
        response=input('>').upper()
        if response[0]=='Q':
            sys.exit()
        if int(response)==1 or int(response)==2 or int(response)==3:
            break
    doorPick=int(response)
    
    while True:
        goatDoor=random.randint(1,3)
        if goatDoor!=doorPick and goatDoor!=carDoor:
            break
    print('The door with goat is:')
    if goatDoor==1:
        print(FIRSTCLOSED)
    elif goatDoor==2:
        print(SECONDCLOSED)
    else:
        print(THIRDCLOSED)
    
    choice=input('Do you want to change your choice(Y/N):')
    if choice[0].upper()=='Y':
        while True:
            response1=int(input("Enter new choice:"))
            if response1 !=goatDoor and response1 != response:
                response=response1
                swap+=1
                break
            else:
                stay+=1
    print('The winning door is:')
    print(WINNING[carDoor-1])
    if response==carDoor:
        print('YOU WIN')
    else:
        print("SORRY YOU LOST")
    
    if swap==1 and response==carDoor:
        swapwins+=1
    elif swap==1:
        swaplosses+=1
    elif stay==1 and response==carDoor:
        staywins+=1
    else:
        staylosses+=1
    print("\nGame Summary So Far:")
    print(f"Swapped: {swapwins} wins, {swaplosses} losses")
    print(f"Stayed : {staywins} wins, {staylosses} losses\n")
    time.sleep(2)
    print('Press Enter to continue:')
    input()
    