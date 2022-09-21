import unittest
import calc 

class test_calc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,6), 16)
        self.assertEqual(calc.add(1,-4), -3)
        self.assertEqual(calc.add(-10,6), -4)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,6),60)
        self.assertEqual(calc.multiply(-10,6),-60)
        self.assertEqual(calc.multiply(-10,-6),60)

    def test_divide(self):
        self.assertEqual(calc.divide(40,10),4)
        self.assertEqual(calc.divide(-10,-40), 1/4)

        self.assertRaises(ValueError, calc.divide, 10,0)
        #context manager instead
        with self.assertRaises(ValueError):
            calc.divide(10,0)



if __name__ == '__main__':
    unittest.main()