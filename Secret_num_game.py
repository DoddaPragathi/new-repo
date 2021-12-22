#A Python program using "while" loop that guess a secret number game
"""
Program No.    :General Practice
Progaram Name  :Practice19.py
Author         :Pragathi
Topics         :Decision Control Statements
                 Loop/iterative control statements
                 for,while loop control statements
                 Nested control statements
"""
import random
#Create a secret number
secret= random.randrange(0,100)
guess=0
numofTries=0
win=False
while(win==False):
    guess=int(input("Enter the number to be guessed:"))
    numofTries+=1
    if(guess==secret):
        win=True
    elif(guess>secret):
        print("It is too high")
    else:
        print("It is too low")

print("You win!!!!")
print("You have trails of {0}".format(numofTries))
print("Thank You!!!")
