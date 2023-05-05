import random         #Hace llamado a la biblioteca random (importa)
lista=[]            #Crea una lista para los valores de la lista
cuadrado=[]         #Crea otra lista para los valores cuadrados de la anterior lista
tam=random.randint(5,10)    #Crea una variable que genere valores aleatorios en un rango de 5 a 10 (9)
print(tam)                 #Imprime tamaño
for i in range(tam):      
    num=random.randrange(100)   #Para los numeros en rango de "tam" (5-10)
    lista.append(num)          #Ingresa en la lista la variable num (un numero aleatorio de 1-100)
print(lista)                  #Imprime la lista

for i in range(len(lista)):  
    cuadrado.append(lista[i]**2) # En la lista de los cuadrados ingresa los numeros cuadrados de la lista "lista"
    #lista[i]=lista[i]**2       
    # print(lista[i]*lista[i])
    # print(lista[i]**2)
    # print(math.pow(lista[i],2))

print(cuadrado)      #Imprime la lista de los cuadrados
print(sum(lista))    #Imprime la suma de los valore en la lista "lista"