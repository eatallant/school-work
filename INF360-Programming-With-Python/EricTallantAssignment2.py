# INF360 - Programming in Python
# Eric Tallant
# Assignment 2

#(1 point) - Initial comments*
#(1 points) - Use at least 2 comparison operators.
#(1 points) - Use at least 1 boolean operator (and, or, not).
#(2 points) - Write at least 1 if statement that contains 2 elif statements and 1 else statement.
#(2 points) - Write at least 1 while statement that contains a break and continue.
#(2 points) - Write at least 1 for loop using the range() method.
#(1 point) - Use the import keyword to import the random module. Use the random.randint() function somewhere in your script.



print("Hello, enter a number between 1 and 10 and I will guess it (hint, I'll know if you pick 5): ")
number = int(input())

while number < 1 or number > 10:
  print("Follow the rules and try again: ")
  number = int(input())



while False: # while false, keep guessing

  low = 1
  high = 11

  guessRange = range(low,high)

  if number == 5: # if number is 5, guess 5
    print('You for sure picked 5')
  elif number < 5: # else if number is less than 5, guess the highest remaining number and dec high
    print('I\'m thinking ' + str(low))
# else if number is greater than 5, guess the lowest remaining number and inc low
# else give error and quit
