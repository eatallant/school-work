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


# this program is a number guessing robot that isn't always great at it's job

import random, time

randVal = random.randint(2, 8)

print("Hello, enter a number between 1 and 10 and I will guess it (hint, I'll know if you pick 5): ")
number = int(input())

# user needs to stay in range
while number < 1 or number > 10:
  print("Follow the rules and try again: ")
  number = int(input())

print('Thinking...')
for i in range(randVal,0, -1):
  print(i)
  time.sleep(1)

low = 1
high = 10
answer = 'N'

while answer == 'N': 

  

  guessRange = range(low,high + 1)

  if number == 5: 
    print('I give up. try another number: ')
    number = int(input())
    continue
  elif number > 5 and number < 10: 
    print('Is it ' + str(low) + '? (y/n): ')
    answer = input().upper()
    low = low + 1
  elif number < 5 and number > 1:
    print('Is it ' + str(high) + '? (y/n)')
    answer = input().upper()
    high = high - 1   
  else:
    print('You broke it')
    break 

if answer == 'Y':
  print('I\'m so smart!!')
