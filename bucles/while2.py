x,y=3,5 #Se almacenan en la variable unos numeros para que el "while" los pueda tomar
cont=1
while not(x%y==0 or y%x==0): #Mientras los numeros ingresados no sean factoriales etre si repite el bucle
    print(f'intento numero {cont}')
    x=int(input('ingrese numero'))
    y=int(input('ingrese numero'))
    cont+=1 #Un contador que muestre la cantidad de intentos realizados

print(f'{x} y {y} son factor') #Imprime si son factoriales entre si

