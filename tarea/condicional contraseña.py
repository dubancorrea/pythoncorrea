
#El sistema le pedira que ingrese un correo y contraseña y si estos son correctos mostrara mensaje en pantalla
contraseña= "12345"
contraseña= input("Introduce la contraseña: ")
if contraseña == contraseña.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")