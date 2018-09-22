#This program uses exahustive enumeration to find an aproximation of the square root of any given number larger than 1.
x = int(input("Enter a number: "))
epsilon = 0.01
step = epsilon**2
numGuesses = 0
answer = 0.0
while abs(answer**2 - x) >= epsilon and answer <= x:
	answer += step
	numGuesses += 1

print('numGuesses = ', numGuesses)
if abs(answer**2 - x) >= epsilon:
	print('Failed on square root of ', x)
else:
	print(answer, 'is close to square root of', x)
