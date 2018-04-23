#Import the random library
import random

#roll variable
roll_again = True

#main while loop
while roll_again:
	print("You rolled:",randint(1,6))
	print("Do you wanna play again?")
	roll_again = ("y" or "yes") in input().lower()