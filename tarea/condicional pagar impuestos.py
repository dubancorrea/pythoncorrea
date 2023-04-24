
#El sistema le mostrara en pantalla dependiendo la edad que tenga si debe pagar impuestos o no
edad= int(input("¿Cuál es tu edad? "))
ingresos = float(input("¿Cuales son tus ingresos mensuales?"))
if edad > 16 and ingresos >= 1000:
    print("Tienes que pagar impuestos")
else:
    print("No tienes que pagar impuestosr")