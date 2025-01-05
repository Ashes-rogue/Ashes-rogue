import random

n1=int(input('lower limit  '))
n2=int(input('upper limit  '))
r=random.randint(n1,n2)
t=0

while True:
    g=int(input('Guess  '))
    t+=1
    if g==r:
        print('correct answer')
        break
    elif g>r:
        print('too high, try again')
    else:
        print('too low, try again')

print('Total number of guess: ',t)

    
