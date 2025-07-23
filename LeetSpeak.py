# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 17:18:31 2025

@author: Akshat Bhalani
"""

import random
def main():
    print('Enter your message:')
    english=input('>')
    print()
    leetspeak=englishToLeetSpeak(english)
    print(leetspeak)
def englishToLeetSpeak(message):
    charMapping={
        'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
     'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
     'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
     'v': ['\\/']
        }
    leetspeak=''
    for char in message:
        if char.lower() in charMapping and random.random()<=0.70:
            possiblities=charMapping[char.lower()]
            replacement=random.choice(possiblities)
            leetspeak+=replacement
        else:
            leetspeak+=char
    return leetspeak

main()