import random
number = random.randint(1,50)
guess = int(input("Guess a number between 1 and 50"))
while guess != number:
    if guess < number:
	print ("\nGuess a higher number. Try again")
 	guess = int(input("Guess a number between 1 and 50"))
    else: 
 	print ("\nGuess a lower number. Try again")
  	guess = int(input("Guess a number between 1 and 50"))
  	
print ("\nYou guessed the number correctly")
