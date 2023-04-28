#Imprimir serie de numeros del 1 hasta "n"
#"n" Sera ingresada por el usuario
#Cada vez que encuentre un multiplo de 7 debe indicar que encontro un multiplo de 7

n=int(input('ingrese numero'))
i=1
while i<n: #Los numeros menores a el numero ingresado limite "n"
    if i%7==0: #Si el modulo de este numero es igual a "0" es multiplo de 7
        print(f'{i} es multiplo de 7')
    else:
        print(i) #Se imprimen los otros numeros de totas formas
    i+=1
