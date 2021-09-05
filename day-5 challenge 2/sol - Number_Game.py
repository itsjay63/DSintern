# Interactive Guess the Number Game 

"""

    The computer will think of a random number from 1 to 10 as 
    secret number.
    Then ask you ( Player ) to guess the number and store as 
    guess number.

    Compare the guess number with the secret number.
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""

import random 
#dir(random)
#help(randint)
#--------------v-1-----------------
num1=int(random.random()*10) #it will include only [1,10)
num2=int(input("Guess a number between 1 and 10:"))

if(num1==num2):
    print("Player wins and computer loses")
else:
    print("Player loses and computer wins")
    
#---------------v-2----------------------
num1=random.randint(1, 10) #it will include [1,10]
num2=int(input("Guess a number between 1 and 10:"))

if(num1==num2):
    print("Player wins and computer loses")
else:
    print("Player loses and computer wins")
    

