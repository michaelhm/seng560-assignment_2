# A simple math application built by reusing a Pytnon library
# Library: https://github.com/zroberts/seng560-python-math
# Forked repository to build app and reuse library

import sys
sys.path.insert(0, '../lib')

import math560

a = 4
b = 4

def calculation(operationName):
    switch={
        'add': math560.addition(a, b),
        'subtract': math560.subtract(a, b),
        'multiply': math560.multiply(a, b),
        'divide': math560.divide(a, b),
        'sqrt': math560.squareRoot(a),
        'exponent': math560.exponent(a, b)
    }
    return switch.get(operationName, 'Invalid operation')

def print_result(operationName):
    result = calculation(operationName)
    if (operationName == 'sqrt'):
        print(f'{operationName} of {a} is {result}')
    elif (operationName == 'exponent'):
        print(f'{a} with an {operationName} of {b} is {result}')
    else:
        print(f'{operationName} {a} and {b} is {result}')


print_result('add')
print_result('subtract')
print_result('multiply')
print_result('divide')
print_result('sqrt')
print_result('exponent')