#This basic algorithm finds the square root of any nonnegative number

#The user enter a number
x = int(input("Enter a number: "))
#We don't know the square root so we say it is 1
guess = 1
#We want to check if our guess is right by calculating how close it is
while abs(x - guess**2) >= 0.00001:
  #The guess wasn't close enough so we average the guess and x/guess until it's close
  guess = (guess + (x/guess))/2
print("The square root of", x, "is aproximately", guess)
