# INF360 Programming with Python
# Eric Tallant
# Assignment 1

print('Welcome, user. What can I do for you? ')
response = input()

print('"' + response + '" sounds too difficult.\nHow difficult is it on a scale of 1 - 10? ')
difficultyScale = int(input())

print('Error: "' + response + '" sounds more like ' + str(difficultyScale * 10))
print('Choose something closer to ' + str(difficultyScale - 2) + ' next time.\nGoodbye.')
