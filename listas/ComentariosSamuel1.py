#[], {}, (), {()}
x=100                     #Una variable puede tener un valor 
print(type(x))
x='Soacha'
print(type(x))            # Y luego puede tener otro valor
lista=['python',100,[1,2,3,[]],'a']   #Una lista con distintos datos, desde enteros hasta string
print(type(lista))
print(len(lista))
print(lista[0])      # Posiciones dentro de una lista con indexacion desde 0
print(lista[1])      #Las posiciones comiienzan desde 0
print(lista[3])
print(lista[-4])   

del lista[-2]     # Elimina de la lista la posicion "-2" de derecha a izquierda
print(lista)

"""
cuenta1=cuenta()              #Hace anotaciones de como varias variables pertenecen a la misma lista
cuenta2=cuenta()
cuenta3=cuenta()                # El metodo dentro de una lista : Es una funcion que hace parte de la clase
cuenta1.deposit()               # Su existencia es dependiente de la clase
print(type(cuenta1))           #Imprime que tipo de dato es "cuenta1"
cuenta2.deposit() 
cuenta3.deposit()
"""