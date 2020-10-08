from calculadora import *
#Pruebas unitarias de la calculadora usando pytest
def test_suma(a, b):
    assert suma(a, b) > 0 #es un valor positivo
    print(suma(a, b))
def test_resta(a, b):
    assert resta(a, b) > 0  #es un valor positivo
    print(resta(a, b))
def test_multiplicacion(a, b):
    assert multiplicacion(a, b) > 0 #es un valor positivo
    print(multiplicacion(a, b))

def test_division(a, b):
    assert b == 0 #es una division que no se puede realizar
    assert division(a, b) > 0 #es un valor positivo

def test():
    test_suma(5,6)
    test_resta(3,6)
    test_multiplicacion(5, -1)
    test_division(25, 5)

test()