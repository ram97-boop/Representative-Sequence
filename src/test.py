inputString = input()
inputFile = open(inputString, 'r')
for line in inputFile:
    print(line)

inputFile.close()
