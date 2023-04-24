
#El programa le solicitara que ingrese su fecha de nacimiento y le mostrara todos los años que ha cumplido desde entonces
edad = int(input("¿Cuántos años tienes? "))
for i in range(edad):
    print("Has cumplido " + str(i+1) + " años")
