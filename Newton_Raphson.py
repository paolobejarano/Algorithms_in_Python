#This program is an implementation of the Newton-Raphson algorithm
#The purpose is to find the square root of a number

epsilon = 0.0001
number = float(input("Introduce a number: "))
guess = number/2
numGuesses = 0
print("Initial guess:", guess)
while abs(number - guess*guess) > epsilon:
    numGuesses += 1
    guess = guess - (((guess**2)-k)/(2*guess))
    print("Guess #" + guess)
    print(guess, "could be the square root of", number)
print(guess, "is very close to the square root of", number)
