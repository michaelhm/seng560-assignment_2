
class sengMath: 
    def addition(self, a, b):
        return a + b
        
    def sumList(self, items):
        if(type(items) is not list):
            raise Exception("List not provided")
        total = 0
        for i in items:
            total += i
        return total
    
    def multiply(self, a, b):
        return a * b

    def multiplyList(self, items):
        if(type(items) is not list):
            raise Exception("List not provided")
        total = items[0]
        for i in items[1:]:
            total *= i
        return total

    def divide(self, a, b):
        return a / b

    def squareRoot(self, x):
        if x is 0 or x is 1:
            return x

        i = 1; result = 1
        while result <= x:
            i += 1
            result = i * i
        return i -1

        # TODO - Find the square root
    
    def exponent(self,a,expon):
        # TODO - raise to the power of
        total = a; i = 1
        while i < expon:
            total *= a
        return total

    def convertToBinary(self):
        # TODO - conver to binary
        return ""

    def convertToHex(self):
        # TODO - convert to hex
        return ""

    def convertToInt(self):
        # TODO - conver value to INT
        return "" 
    def converToOct(self):
        # TODO - convert value to Octal
        return ""
    
