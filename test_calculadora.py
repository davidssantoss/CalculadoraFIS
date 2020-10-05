import unittest
import calculadora;

class TestCalculadora (unittest.TestCase):

    def test_sum(self):
        self.assertEqual(calculadora.suma(5, 7), 12)

    def test_resta(self):
      self.assertEqual(calculadora.resta(4,3), 1)
  
    def test_multiplicacion(self):
      self.assertEqual(calculadora.multiplicacion(4,4), 16)
  
    def test_divide(self):
      self.assertEqual(calculadora.division(2,1), 2)
        
if __name__ == "__main__":
    unittest.main()
