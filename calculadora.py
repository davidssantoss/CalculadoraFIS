def suma(a, b):
	return a + b

def resta(a, b):
	return a - b

def multiplicacion(a, b):
	return a * b

def division(a, b):
    if (b == 0):
        return print("No se puede dividir por cero!")
    else:
        return a / b

def run():
    tipos = "1) Sumar dos numeros \n2) Restar dos numeros \n3) Multiplicar dos numeros \n4) Dividir dos numeros \n5) Terminar"
    opcion = int(input("\n Seleccione el numero de la opcion a consultar: \n{}:\n".format(tipos)))
    if opcion == 1:            
        n1 = int(input("Digite el primer numero: "))
        n2 = int(input("Digite el segundo numero: "))
        print("El resultado de la suma es: ", suma(n1, n2))
    elif opcion == 2:
        n1 = int(input("Digite el primer numero: "))
        n2 = int(input("Digite el segundo numero: "))
        print("El resultado de la resta es: ", resta(n1, n2))
    elif opcion == 3:
        n1 = int(input("Digite el primer numero: "))
        n2 = int(input("Digite el segundo numero: "))
        print("El resultado de la multiplicacion es: ", multiplicacion(n1, n2))
    elif opcion == 4:
        n1 = int(input("Digite el primer numero: "))
        n2 = int(input("Digite el segundo numero: "))
        print("El resultado de la division es: ", division(n1, n2))            
    elif opcion == 5:
        exit()
    else:
        print("Opcion no valida, vuelva a digitar una opcion")


def main():
    print("*** Calculadora basica ***")
    run()
    
if __name__ == "__main__":
    main()
