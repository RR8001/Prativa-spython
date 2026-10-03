
#creating a random number guessing game through python using while loop..
import random
"""import random loads python built-in module that helps us to
 functions that generate random number,import tells python to find 
 a module then run that module under a name for which you can use"""
num = random.randint(1,8)
#here we have tell to generate random numbers from 1 to 8 only
print(num)
# I have cheated here.
guess = int(input("hey!! can  you guess a number"))
if guess == num:
    print("you guess is right brooo")
else:
    print("you guessed is wrong")

   