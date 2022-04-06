import string
import os
import time


def clearConsole():
    time.sleep(.5)
    os.system('cls')


def generator():
    chars = string.ascii_uppercase
    numbers = string.digits
    #           0   1   2   3   4   5   6
    license = ['', '', '', '-', '', '', '']

    print(numbers)
    print(chars)

    for i in range(len(chars)):
        for j in range(len(chars)):
            for k in range(len(chars)):
                license[0] = chars[i]
                license[1] = chars[j]
                license[2] = chars[k]
                try:
                    license[4] = numbers[i]
                except IndexError:
                    pass
                try:
                    license[5] = numbers[j]
                except IndexError:
                    pass
                try:
                    license[6] = numbers[k]
                except IndexError:
                    pass
                print(''.join(license))
                clearConsole()
