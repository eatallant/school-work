# Write a function named printTable() that takes a list of lists of strings
# and displays it in a well-organized table with each column right-justified. 
# Assume that all the inner lists will contain the same number of strings. 
# For example, the value could look like this:


#tableData = [['apples', 'oranges', 'cherries', 'banana'],
#             ['Alice', 'Bob', 'Carol', 'David'],
#             ['dogs', 'cats', 'moose', 'goose']]
#Your printTable() function would print the following:


#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose



def printTable(theList):

  # create a list to hold the char amounts for rjust
  colWidths = [0] * len(theList)

  # populate colWidths with the longest string in each list
  for i in range(len(theList)):
    for j in theList[i]:
      if(len(j) > colWidths[i]):
        colWidths[i] = len(j)


  # print the nth item in each list right justified in each line
  for i in range(len(theList[0])):
    for j in range(len(theList)):
      print(theList[j][i].rjust(colWidths[j]), end=' ')
    print('')



