print('Enter the encrypted message(Ceasar cipher) to be hacked:')
message=input('> ')

SYMBOLS1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SYMBOLS1+='abcdefghijklmnopqrstuvwxyz'

for key in range(len(SYMBOLS1)):
    translated=''
    for symbol in message:
        if symbol in SYMBOLS1:
            num=SYMBOLS1.find(symbol)
            num-=key

            if num<0:
                num+=len(SYMBOLS1)
                
            translated+=SYMBOLS1[num]
        else:
            translated+=symbol
            
    print(f'Key #{key}: {translated}')