import unittest
from salarios import calcular_salario

class TestSalarios(unittest.TestCase):
    def test_sin_extras(self):
        self.assertEqual(calcular_salario(40, 1), 40 * 12000)
    def test_con_extras(self):
        self.assertEqual(calcular_salario(45, 2), 40 * 17000 + 5 * 17000 * 1.25)
    def test_error_horas(self):
        with self.assertRaises(ValueError):
            calcular_salario(-1, 1)
    def test_error_categoria(self):
        with self.assertRaises(ValueError):
            calcular_salario(20, 9)

if __name__ == "__main__":
    unittest.main()
