
#El sistema le mostrara cuanto debe pagar para ingresar en una tienda
edad = int(input("Introduce tu edad: "))
# Mostrara cuanto tiene que pagar dependiendo su edad
if edad < 10:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
# Mostrar precio
print("El precio de la entrada es", precio, "$.")