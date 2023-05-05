import random

lista1=[]
suma_lista1=0
mayor_lista1=0
menor_lista1=0
lista2=[]
suma_lista2=0
mayor_lista2=0
menor_lista2=0



# LISTA 1
tam= random.randint(5,10)

for i in range(tam):
    num=random.randrange(10)
    lista1.append(num)
print(lista1)

# LISTA 2
tam= random.randint(5,10)

for i in range(tam):
    num=random.randrange(10)
    lista2.append(num)
print(lista2)

#SUMA LISTA 1
for i in lista1:
    suma_lista1 += i 
print(suma_lista1)

#SUMA LISTA 2
for i in lista2:
    suma_lista2 += i 
print(suma_lista2)

if suma_lista1 > suma_lista2:
    print (f'La suma de la lista 1 es {suma_lista1} y es mayor que la suma de la lista 2 {suma_lista2}')
else:
    suma_lista1 > suma_lista2
    print (f'La suma de la lista 2 es {suma_lista2} y es mayor que la suma de la lista 1 {suma_lista1}')

# MAYOR Y MENOR DE LISTA 1:

for i in lista1:
        if i>mayor_lista1:
             mayor_lista1=i
        if i<menor_lista1:
             menor_lista1=i
print("El mayor de la lista 1 es: ", mayor_lista1)
print("El menor de la lista 1 es: ", menor_lista1)

# MAYOR Y MENOR DE LISTA 2:

for i in lista2:
        if i>mayor_lista2:
             mayor_lista2=i
        if i<menor_lista2:
             menor_lista2=i
print("El mayor de la lista 2 es: ", mayor_lista2)
print("El menor de la lista 2 es: ", menor_lista2)

