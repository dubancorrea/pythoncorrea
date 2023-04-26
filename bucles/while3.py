#Imprimir serie de numeros del 1 hasta "n"
#"n" Sera ingresada por el usuario
#Cada vez que encuentre un multiplo de 7 debe indicar que encontro un multiplo de 7

n=int(input("Ingrese un numero"))
multiplo_siete= 1

while multiplo_siete <= n:
    if multiplo_siete % 7 == 0:
        print (multiplo_siete, "El numero es multiplo de 7")
    else:
        print(multiplo_siete)
    multiplo_siete += 1