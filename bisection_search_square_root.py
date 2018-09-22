#This program calculates the square root using a bisection search method

x = int(input("Enter a number: "))
epsilon = 0.0001
numGuesses = 0
low = 0.0
high = max(1.0, x)
answer = (high + low)/2.0
while abs(answer**2 - x) >= epsilon:
	print('low =', low, 'high =', high, 'answer =', answer)
	numGuesses += 1
	if answer**2 < x:
		low = answer
	else:
		high = answer
	answer = (high + low)/2.0

print('numGuesses = ', numGuesses)
print(answer, 'is close to square root of', x)
