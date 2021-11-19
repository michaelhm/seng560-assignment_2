from math import atan
import unittest
import math560

class TestAdditionMethos (unittest.TestCase):
    items = [1,2,3,4,5,6,7,8,9,0]
    def test_add(self):
        print(f"Testing addition functions\n")
        print(f"Adding {self.items[0]} and {self.items[1]}")
        self.assertEqual(math560.addition(self.items[0],self.items[1]), 3)

        print(f"Adding the full list: {self.items}")
        self.assertEqual(math560.sumList(self.items), 45)

        print(f"Testing that an exception is raised if single value is passed into sumList")
        with self.assertRaises(Exception):
            math560.sumList(self.items[0])

    def test_subtract(self):
        print(f"\n\nTesting Subtraction functions\n")
        
        print(f"Subtracting {self.items[-2]} from {self.items[1]}")
        self.assertEqual(math560.subtract(self.items[-2], self.items[1]), 7)
        print(f"Subtracting the full list: {self.items}")
        self.assertEqual(math560.subtractList(self.items), -43)

        print(f"Testing that an exception is raised if single value is passed into subtractList")
        with self.assertRaises(Exception):
            math560.subtractList(self.items[1])
    
    def test_multiplication(self):

        print(f"\n\nTesting Multiplication Functsion\n")

        print(f"Multiplying items: {self.items[0]} * {self.items[-2]}")
        self.assertEqual(math560.multiply(self.items[0], self.items[-2]), self.items[-2])

        print(f"Multiplying items: {self.items[1]} * {self.items[-2]}")
        self.assertEqual(math560.multiply(self.items[1], self.items[-2]), math560.addition(self.items[-2], self.items[-2]))

        print(f"Multiply List: {self.items}")
        self.assertEqual(math560.multiplyList(self.items), self.items[-1])
        
        print(f"Multiplying List, minus the zero: {self.items[:-1]}")
        self.assertEqual(math560.multiplyList(self.items[:-1]), 362880)
        
        print(f"passing a single int into the multiply list")
        with self.assertRaises(Exception):
            math560.multiplyList(self.items[1])
    
    def test_division(self):
        print(f"\n\nTesting Division Functions\n")

        print(f"Dividing Items: {self.items[-2]} \ {self.items[2]}")
        self.assertEqual(math560.divide(self.items[-2], self.items[2]), self.items[2])

        print (f"Dividing Items: {self.items[0]} \ {self.items[1]}")
        self.assertEqual(math560.divide(self.items[0], self.items[1]), .5)

    def test_square_root(self):
        print(f"\n\nTesting the Square Root\n")

        print(f"Square Root of {self.items[-2]}")
        self.assertEqual(math560.squareRoot(self.items[-2]), 3)

        print(f"Square Root of 70.5")
        self.assertEqual(math560.squareRoot(70.5), 8.396427811873332)
    
    def test_exponent(self):
        print(f"\n\nTesting Exponent\n")

        print(f"Exponential items: 2^2")
        self.assertEqual(math560.exponent(2,2), 4)

        print(f"Expontial test: 2^3")
        self.assertEqual(math560.exponent(2,3), 8)

        print(f"Exponential test: 2^10")
        self.assertEqual(math560.exponent(2,10), 1024)
    
    def test_binaryConversion(self):
        print(f"\n\nTesting Conversion to Binary")
        print(f"Convert 25 to Binary")
        self.assertEqual(math560.convertToBinary(25), "11001")

        print(f"pass in non-int")
        with self.assertRaises(Exception):
            math560.convertToBinary("s")

    
    def test_hexConversion(self):
        print(f"\n\nTesting conversion to Hexadecimal\n")
        print(f"Convert 123 to Hex")
        self.assertEqual(math560.convertToHex(123),"7B")

        print(f"pass in non-int")
        with self.assertRaises(Exception):
            math560.convertToHex("a")
    
    def test_octalConversion(self):
        print(f"\n\nTesting conversion to Octal\n")
        print(f"Convert 25 to Octal")
        self.assertEqual(math560.convertToOct(25), "31")

        print(f"pass in non-int")
        with self.assertRaises(Exception):
            math560.convertToOct("b")


if __name__ == '__main__':
    unittest.main()