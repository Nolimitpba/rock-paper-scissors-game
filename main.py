import random

user = input('rock, paper, or scissors?')
computer = random.choice(['rock', 'paper', 'scissors'])

if user == computer:
    print("it's a tie")
elif user == 'rock':
    if computer == 'paper':
        print('You lose!')
    else:
        print('You win')
elif user == 'paper':
    if computer == 'scissors':
        print('You lose!')
    else:
        print('You win')
elif user == 'scissors':
    if computer == 'rock':
        print('You lose')
    else:
        print('You win')                
    
