import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData
# Output:
# [['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'],
# ['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'],
# ['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'],
# ['4/10/2015 2:40', 'Strawberries', '98']]

exampleData[0][0]
# Output: '4/5/2015 13:34'
exampleData[0][1]
# Output: 'Apples'
exampleData[0][2]
# Output: '73'
exampleData[1][1]
# Output: 'Cherries'
exampleData[6][1]
# Output: 'Strawberries'

for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

# Output:
# Row #1 ['4/5/2015 13:34', 'Apples', '73']
# Row #2 ['4/5/2015 3:41', 'Cherries', '85']
# Row #3 ['4/6/2015 12:46', 'Pears', '14']
# etc.

# Writing csv
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
# Output: 21
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
# Output: 32
outputWriter.writerow([1, 2, 3.141592, 4])
# Output: 16

outputFile.close()

