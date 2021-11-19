# seng560-python-math

## Using the Application
Import the code-base into your file:
```
import math560
```

## Methods

### Addition 
Addes two numbers together and returns the sumation of those numbers.
```
math560.addition = math560.addition(5,10) # 15 returned
```
### Sumlist
Takes in a list of numbers and sums the entire list. 
```
items = [1,2,3]
math560.sumList(items) # returns 6
```
### subtract
takes the difference between the two provided numbers
```
math560.subtract(5,3) # returns 2
```

### subtractList
Subtracts subsequent items in a list from the first item.
I.e: item[0] - item[1] - item[2] - item[n]
```
items = [6,2,1]
math560.subtractList(items)
```
### multiply
Multiplies two items together
```
math560.multiply(2,3) # returns 6
```
### multiplyList

Multiply the items in a list togther, starting from the first list item
I.e: item[0] * item[1] * item[n]
```
items = [6,2,1]
math560.multiplyList(items) # returns 12
```
### Division
Divides the two numbers together
```
math560.divide(6,2) # returns 3
```
### Square Root
Finds the square root of the number
```
math560.squareRoot(9) # returns 3
```
### Exponent
Raises the first number to the power of the second number. 
```
math560.exponent(2,3) # returns 8
```
### Convert to Binary
Converts an integer to a binary string 
```
math560.convertToBinary(25) # returns "11001"
```
### Convert to Hexadecimal
Converts an integer to a hexadecimal string
```
math560.convertToHex(123) # returns 7B
```
### Convert to Octal 
Converst an integer to Octal string
```
math560.convertToOctal(25) # return "31"
``` 