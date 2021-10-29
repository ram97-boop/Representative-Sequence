# -*- coding: utf-8 -*- 

def addTwoNum(a, b):
    return a + b

def main():
    s = input('\nEnter two integers: \n')
    numList = s.split()
    print(addTwoNum(int(numList[0]), int(numList[1])))

if __name__ == '__main__':
    main()
