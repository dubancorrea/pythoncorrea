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
divi=0
cuad=2
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

for i in range(len(lista)):
        for i in range (num):
            if num == num:
               modas= (i) = (num) 
               moda=modas
print(f'La moda es: {moda}')

for i in lista:
    i = resta - (suma) / (promedio)
    cuadrado = resta ** 2
    suma += cuadrado
    division = suma / promedio
raiz = math.sqrt(division)
print((f'La desviacion estandar es: {raiz}'))

#Hacer el ultimo punto 
##Terminar ejercicio y hacer los del pdf
#Coger lo que samuelito programo
#Comentarear el codigo que hizo en la sesion de hoy
#Hacer los programas de hoy
