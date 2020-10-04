def suma(a, b):
	return a + b

def resta(a, b):
	return a - b

def multiplicacion(a, b):
	return a * b

def divide(a, b):
    if (b == 0):
        return print("No se puede dividir por cero!")
    else:
        return a / b


def main():
    print(suma(2,4))
    

if __name__ == "__main__":
    main()
