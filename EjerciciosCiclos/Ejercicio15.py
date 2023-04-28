# Diseñar e implementar un programa que solicite a su 
#usuario un valor no negativo n y visualice La lista del numero en decremento de uno en uno

n= int(input("Ingrese un numero positivo"))

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end='')
    print()
