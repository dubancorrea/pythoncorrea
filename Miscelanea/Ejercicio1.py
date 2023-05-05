#Se usan con los corchetes "[]"
#Sumarlos
#Promedio
#Mayor
#Menor
#Moda: El numero que mas se repite
#Mediana : si la lista es impar, ordenar la lista de menor a mayor y tomar la l
#Desviacion estandar : calcular la media
#calcular el cuadrado de la distancia a la media para cada DeprecationWarnin
#sumar los valores que resultaron del paso


import random
import math
lista=[]
suma=0
resta=0
division=0
cuadrado=2
promedio=0
menor=10000
mayor=0
moda=0
media=0
modas=0

tam= random.randint(5,10)

for i in range(tam):
    num=random.randrange(10)
    lista.append(num)
print(lista)

for i in lista:
    suma += i 
print(suma)
for i in lista:
    promedio= suma//tam
print(promedio)

for i in lista:
        if i>mayor:
             mayor=i
        if i<menor:
             menor=i
print("El mayor es:", mayor)
print("El menor es:", menor)

max = 0
for num in lista:
    cont = 0
    for s in lista:
        if num == s:
            cont +=1
    if cont > max:
        max = cont
        moda = num
print ("La moda es: ", moda )

for i in lista:
    i = resta - (suma) / (promedio)
    cuadrado = resta ** 2
    suma += cuadrado
    division = suma / promedio
raiz = math.sqrt(division)
print((f'La desviacion estandar es: {raiz}'))

for i in range(tam):
    for j in range(i+1,tam):
        if lista[i]<lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux

print(lista)

for i in range(tam):
    for j in range(i+1,tam):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux

print(lista)