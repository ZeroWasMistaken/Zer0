#Zer0 OS Alpha module

#[MODULES]

import math
import platform
import os

#[FUNCTIONS]

defaultInput = '> '

#Function helpMessage()

helpMSG = '''[Zer0 OS Alpha]
help : Displays this message
calculator : Opens a calculator
clear : Clears the screen
exit : Exits Zer0'''

def helpMessage():
    print(helpMSG)

#Function welcomeMessage()

welcomeText = '''Welcome to Zer0 OS Alpha!
Type help for more information\n'''

def welcomeMessage():
    print(welcomeText)

#Function calculatorClient()

calculatorInput = 'calculator' + defaultInput

operation_select = '''Select an operation:
1. Add
2. Substract
3. Multiply
4. Divide
5. Exponent
6. Square root'''

def addValue(x, y):
    return x + y

def substractValue(x, y):
    return x - y

def multiplyValue(x, y):
    return x * y

def divideValue(x, y):
    return x / y

def exponentValue(x, y):
    return x ** y

def squareRootValue(x):
    return math.sqrt(x)

def calculatorClient():
    print(operation_select)

    while True:
        operationSelect = input(calculatorInput)

        if operationSelect in('1','2','3','4'):
            num1 = float(input('Insert first number: '))
            num2 = float(input('Insert second number: '))

            operationSwitcher = {
                '1': addValue(num1, num2),
                '2': substractValue(num1, num2),
                '3': multiplyValue(num1, num2),
                '4': divideValue(num1, num2)
            }

            print(operationSwitcher.get(operationSelect, 'Invalid Operation'))

        elif operationSelect == '5':
            exp_num = float(input('Select number: '))
            exp = float(input('Select exponent: '))

            exponentValue(exp_num, exp)

        elif operationSelect == '6':
            sqrt_num = float(input('Select number: '))

            squareRootValue(sqrt_num)

        elif operationSelect == 'exit':
            break

#Function username()

def username():
    usernameFile = open('username.txt', 'r')

    if usernameFile == '~':
        usernameSelect = input('Please select an username: ')
        usernameWrite = open('username.txt', 'w')
        usernameWrite.write(usernameSelect)

    usernameFile.close()

#Function screenClear()

name = platform.system()

def screenClear():
    if name != "Windows":
        os.system("clear")
    else:
        os.system("cls")

#Function OSInterface()

def OSInterface():
    while True:
        cmd = input(defaultInput)

        if cmd == 'help':
            helpMessage()

        elif cmd == 'clear':
            screenClear()

        elif cmd == 'calculator':
            calculatorClient()

        elif cmd == 'exit':
            break

        else:
            print('Invalid Command!')