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

        self.assertEqual(math560.multiply(self.items[0], self.items[-2]), self.items[-2])

        self.assertEqual(math560.multiply(self.items[1], self.items[-2]), math560.addition(self.items[-2], self.items[-2]))

        self.assertEqual(math560.multiplyList(self.items), self.items[-1])
        
        self.assertEqual(math560.multiplyList(self.items[:-1]), 362880)




if __name__ == '__main__':
    unittest.main()