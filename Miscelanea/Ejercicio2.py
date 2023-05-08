import random

lista1=[]
suma_lista1=0
mayor_lista1=0
menor_lista1=0
lista2=[]
suma_lista2=0
mayor_lista2=0
menor_lista2=0
tam1=0
tam2=0
promedio_lista1=0
promedio_lista2=0

# LISTA 1
tam1= random.randint(5,10)

for i in range(tam1):
    num=random.randrange(10)
    lista1.append(num)
print(lista1)

# LISTA 2
tam2= random.randint(5,10)

for i in range(tam2):
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
    print (f'La suma de la lista 1 es {suma_lista1} y es mayor que la suma de la lista 2: {suma_lista2}')
else:
    suma_lista1 > suma_lista2
    print (f'La suma de la lista 2 es {suma_lista2} y es mayor que la suma de la lista 1: {suma_lista1}')

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

#MAYOR ENTRE LISTA 1 Y 2

if mayor_lista1 > mayor_lista2:
    print (f'El numero mayor de la lista 1: {mayor_lista1} es mayor que el de la lista 2: {mayor_lista2}')
else:
    mayor_lista2 > mayor_lista1
    print (f'El numero mayor de la lista 1: {mayor_lista2} es mayor que el de la lista 2: {mayor_lista1}')

#MENOR ENTRE LISTA 1 Y 2
 
if menor_lista2 > menor_lista1:
    print (f'El numero menor de la lista 1: {menor_lista1} es menor que el de la lista 2: {menor_lista2}')
else:
    menor_lista1 > menor_lista2
    print (f'El numero menor de la lista 2: {menor_lista2} es menor que el de la lista 1: {menor_lista1}')

#PROMEDIO DE LAS DOS LISTAS SUMADAS (CONJUNTO)/ TAMAÑO DE LISTA 1 MAS LISTA 2

promedio_conjunto=(suma_lista1+suma_lista2)/(tam1+tam2)
print("El promedio de las dos listas sumadas es: ", promedio_conjunto)

#PROMEDIO LISTA 1, ¿Es (MAYOR O MENOR QUE PROMEDIO LISTA CONJUNTO)?

promedio_lista1= suma_lista1/tam1
print ("El promedio de la lista 1 es:", promedio_lista1)

if promedio_lista1 > promedio_conjunto:
    print (f'El promedio de la lista 1: {promedio_lista1} es mayor que el promedio conjunto: {promedio_conjunto}')
else:
    promedio_conjunto > promedio_lista1
    print (f'El promedio conjunto: {promedio_conjunto} es mayor que el promedio de la lista 1: {promedio_lista1}')

#PROMEDIO LISTA 2, ¿Es (MAYOR O MENOR QUE PROMEDIO LISTA CONJUNTO)?

promedio_lista2= suma_lista2/tam2
print ("El promedio de la lista 2 es:", promedio_lista2)

if promedio_lista2 > promedio_conjunto:
    print (f'El promedio de la lista 2: {promedio_lista2} es mayor que el promedio conjunto: {promedio_conjunto}')
else:
    promedio_conjunto > promedio_lista2
    print (f'El promedio conjunto: {promedio_conjunto} es mayor que el promedio de la lista 2: {promedio_lista2}')


pares_lista1=0
pares_lista2=0
impares_lista1=0
impares_lista2=0

# CUAL DE LOS DOS TIENE MAYOR CANTIDAD DE PARES

for i in lista1:
     if i % 2 == 0:
          pares_lista1+=1
print("La tabla 1 tiene", pares_lista1, "Numeros pares")
for i in lista2:
     if i % 2 == 0:
          pares_lista2+=1
print("La tabla 2 tiene", pares_lista2, "Numeros pares")

# CUAL DE LOS DOS TIENE MAYOR CANTIDAD DE IMPARES

for i in lista1:
     if i % 2 == 2:
          impares_lista1+=1
print("La tabla 1 tiene", impares_lista1, "Numeros impares")
for i in lista2:
     if i % 2 == 1:
          impares_lista2+=1
print("La tabla 2 tiene", impares_lista2, "Numeros impares")