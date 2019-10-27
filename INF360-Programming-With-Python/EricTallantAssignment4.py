# INF360 - Programming with Python
# Eric Tallant
# Assignment 4

"""
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The following text file would then be created:

The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.

functions:
1. makeLib(textFile, newLibName)
  create file newLibName.txt. copy contents of textFile. take new file and run it through regex. 
    every time ADJECTIVE, ADVERB, NOUN, or VERB is found in the file, 
    ask user to input that word type. replace that word type with user input. close file at end
  preconditions: textFile exists
  
program steps:
1. get file from user
2. run getLibs
3. print file
"""
import os
import re


# create a new file that is an exact copy of textFile
def make_lib_file(textFile, newLibName):
  # validate file
  if not os.path.isfile(textFile):
    print('File or directory does not exist')
    return

  # open file
  textContent = textFile.open()

  # create new file and copy contents of textFile
  newLib = open(newLibName + '.txt', 'w')
  newLib.write(textContent.read())
  newLib.close


# make a list of libs that need answers from file
def madLibber(textFile):

  libContent = textFile.open()
  # make a list of words that need filled in
  libsWanted = re.findall('ADJECTIVE'|'ADVERB'|'NOUN'|'VERB', libContent)

  # make a list of the users choice for the words
  userLibs = []
  for word in libsWanted:
    userLibs.append(input('enter ' + word.lower() + ': '))

  # for each word user picked, replace the place holder in the text file with the word
  for word in userLibs:
    libContent.write(re.sub('ADJECTIVE'|'ADVERB'|'NOUN'|'VERB', word, libContent))

  libContent.close()

print('Welcome to Mad Lib')
libFile = input('Enter the path of your file: ')
newLib = input('Make a new name for this mad lib: ')

make_lib_file(libFile, newLib)
madLibber(newLib)

newLib.open()
print(newLib.read())





