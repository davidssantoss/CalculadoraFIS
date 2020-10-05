import unittest
import calculadora;

class TestCalculadora (unittest.TestCase):

  def test_sum(self):
        self.assertEqual(calculadora.sum(5, 7), 12)
        
 if __name__ == "__main__":
    unittest.main()
