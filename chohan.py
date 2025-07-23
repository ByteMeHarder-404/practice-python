import random,sys

JAPANESE_NUMBERS={1:'ICHI',2:'NI',3:'SAN',4:'SHI',5:'GO',6:'ROKU'}

print('Cho Han')

purse =5000

while True:
    print('You have', purse,' mon. How much do you bet? (or QUIT)')
    while True:
        pot=input("> ")
        if pot.upper()=='QUIT':
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number:')
        elif int(pot)>purse:
            print('You do not have enough to make that bet.')
        else:
            pot=int(pot)
            break
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print('The cup has been swirled.tell your prediction:')
    print('CHO(even) or HAN(odd):')
    while True:
        bet=input('> ').upper()
        if bet!='CHO' and bet!='HAN':
            print('Please enter either "CHO" or "HAN"')
            continue
        else:
            break
    
    print('The dice result:')
    print(f'  {JAPANESE_NUMBERS[dice1]} - {JAPANESE_NUMBERS[dice2]}')
    print(f'     {dice1} - {dice2}')

    rollIsEven=(dice1+dice2)%2==0
    if rollIsEven:
        correctbet='CHO'
    else:
        correctbet='HAN'
    
    playerWon=bet==correctbet

    if playerWon:
        print(f'You won! You take {pot} mon')
        purse+=pot
        print(f'The house collects a {pot//10} mon fee')
        purse-=(pot//10)
    else:
        purse-=pot
        print('You lost')
    
    if purse==0:
        print('You have run out of money! Hahaha')
        sys.exit()