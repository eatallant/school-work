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
"""

import os
import re
import sys


# create a new file that is an exact copy of textFile
def make_lib_file(textFile, newLibName):
    # validate file
    if not os.path.isfile(textFile):
        sys.exit('File or directory does not exist')

    # open file
    textContent = open(textFile)

    # create new file and copy contents of textFile
    newLib = open(newLibName, 'w')
    newLib.write(textContent.read())
    newLib.close


# make a list of libs that need answers from file
def madLibber(textFile):

    libContent = open(textFile)
    content = libContent.read()
    libContent.close()
    # make a list of words that need filled in
    libsWanted = re.findall('ADJECTIVE|ADVERB|NOUN|VERB', content)

    # make a list of the users choice for the words
    userLibs = []
    for word in libsWanted:
        userLibs.append(input('enter ' + word.lower() + ': '))

    # for each word user picked, replace the place holder in the text file with the word
    for word in userLibs:
        content = re.sub('ADJECTIVE|ADVERB|NOUN|VERB', word, content, 1)

    # overwrite textFile with content
    libContent = open(textFile, 'w')
    libContent.write(content)
    libContent.close()


# This is the main program. Get path from user and have them name a new file
print('Welcome to Mad Lib')

libFile = str(input('Enter the path of your file: '))
newLib = str(input('Make a new name for this mad lib: ') + '.txt')

make_lib_file(libFile, newLib)
madLibber(newLib)

# print newly edited text file
newLibText = open(newLib)
print(newLibText.read())
newLibText.close()


