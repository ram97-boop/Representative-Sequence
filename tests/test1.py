# -*- coding: utf-8 -*- 

def readFile(f):
    textFile = open(f, 'r')
    line = textFile.readline()
    while line != '\n':
        print(line)
        line = textFile.readline()    
    textFile.close()

def main():
    f = 'gene.fa'
    readFile(f)

if __name__ == '__main__':
    main()
