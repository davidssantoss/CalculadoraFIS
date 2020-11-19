import math
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "No se puede dividir por cero"
        return a / b

    def potencia(self, a, b):
        return math.pow(a, b)