
#Comenzaremos a introducir el tema de condicionales con (if-else-elif) con el sisguiente ejercicio

x=int(input('ingrese numero'))
y=int(input('ingrese numero'))
z=int(input('ingrese numero'))
#indentación / Pide con un input que ingrese las variables
if x>y:
    if x>z:
        print(f'el mayor es {x}')
    else:
        print(f'el mayor es {z}')
else:
    if y>z:
        print(f'el mayor es {y}')
    else:
        print(f'el mayor es {z}')
        
        #Enlaza encadenamientos de if-else haciendo que tome varios condiciones dependiendo el numero
        #Si no se cumple una condicion tomara otro camino