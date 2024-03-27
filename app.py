import random

stop = False

while not stop:
    number = input("Guess a number 0 to 10 , insert 'q' to quit:\n")
    if number =='':
        print('Please insert a number')
    else:
        if number  != 'q':
             randNum = random.randint(0,10)
             if int(number) == randNum:
                print('You have guessed the correct number!')
                print(f'Your guess:{number}')
                print(f'The Number:{randNum}')
             else:
                print('Sorry, that was not the number')
                print(f'Your guess:{number}')
                print(f'The Number:{randNum}') 
        else:
             stop = True         
