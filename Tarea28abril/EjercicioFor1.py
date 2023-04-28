# El sistema le solicitara al usuario inicio, fin y cantidad a incrementar o decrementar segun el caso
#Solicitara al usuario un numerpo positivo que debera incluirse en la serie 
#Mostrara cuantos multiplos de n hay en la serie desde 0 hasta ek numero ingresado, "n" se ingresa por teclado
inicio = int(input("Ingrese el inicio de la serie: "))
fin = int(input("Ingrese el fin de la serie: "))
cantidad = int(input("Ingrese la cantidad a incrementar o decrementar según el caso: "))
n = int(input("Ingrese un número positivo que deberá incluirse en la serie: "))

serie = [i for i in range(inicio, fin, cantidad)]
print("La serie es:", serie)
multiplos = [i for i in serie if i % n == 0]
print(f"La cantidad de múltiplos de {n} en la serie es:", len(multiplos))

