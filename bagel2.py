import random

NUM_DIGITS=3
CHANCES = 10

def secret_num():
    numbers=[1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)
    sec_num=''
    for i in range(0,NUM_DIGITS):
        sec_num+=numbers[i]
    return sec_num
def get_clues()