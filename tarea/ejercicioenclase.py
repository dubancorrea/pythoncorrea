
#El programa le solicitara que ingrese tres numeros y muestre cual es el mayor
num1= int(input("Ingrese el primer numero"))
num2= int(input("Ingrese el segundo numero"))
num3= int(input("Ingrese el primer numero"))

if num1>num2:
    if num1>num3:
        print("El primer numero es el mayor")
    else: print("El tercer numero ingresado es el mayor")
elif num2>num3:
    print