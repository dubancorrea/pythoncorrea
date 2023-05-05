#Se usan con los corchetes "[]"
#sumarlos
#promedio
#mayor
#menor
#moda
#mediana
#desviacion estandar
#Mediana : si la lista es impar, ordenar la lista de menor a mayor y tomar la l
#Desviacion estandar : calcular la media
#calcular el cuadrado de la distancia a la media para cada DeprecationWarnin
#sumar los valores que resultaron del paso


import random
lista=[]
sum=0
promedio=0
menor=10000
mayor=0
moda=0
media=[]
tam= random.randint(5,10)

for i in range(tam):
    num=random.randrange(10)
    lista.append(num)
print(lista)

for i in lista:
    sum += i 
print(sum)
for i in lista:
    promedio= sum//tam
print(promedio)

for i in lista:
        if i>mayor:
             mayor=i
        if i<menor:
             menor=i
print("El mayor es:", mayor)
print("El menor es:", menor)

for i in lista:
     if i==i:
          print("la moda es", moda)

for i in lista():
  print(media)

#Hacer el ultimo punto 
##Terminar ejercicio y hacer los del pdf
#Coger lo que samuelito programo
#Comentarear el codigo que hizo en la sesion de hoy
#Hacer los programas de hoy
