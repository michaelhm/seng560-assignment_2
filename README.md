# SENG 560 - Programming Assignment 2 - Software Reuse

The purpose of this repository is to perform arithmetic functions using a library built by another classmate.

To prove the reusability of the library, I have created a simple application which passes values of various number types to library functions and prints the results.

The library was very easy to integrate into my application and proved to be *black box* as I did not have to make any modifications to library source code.

### Example of reuse implementation:
``a = 4``

``b = 0o04``

``math560.addition(a, b)``

## How to use this application
### Requirements:
*Python version 3.\*.\**

### Run app:
1. Clone repository
2. Open terminal/shell in cloned project folder
3. Run from terminal/shell: ``cd simple_app && python3 math_app.py`` or ``cd simple_app && python math_app.py``

### Expected output:
> add 4 and 4 is 8
>
> multiply 4 and 4 is 16
>
> divide 4 and 4 is 1.0
>
> sqrt of 4 is 2.0
>
> 4 with an exponent of 4 is 256
>
> subtract 3 and 2 is 1
