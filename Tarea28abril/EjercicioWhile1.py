#El sistema leeara dos numeros y garantizara que hay un numero mayor que el otro si no es el caso los pedira de nuevo

while True:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    if num1 > num2:
        print("El número", num1, "es mayor que", num2)
        resultado = num1 - num2
        print("La resta de", num1, "-", num2, "es igual a", resultado)
        if resultado > 0:
            print("Como el resultado es mayor que cero, se puede restar nuevamente.")
            num3 = int(input("Introduce el tercer número: "))
            resultado2 = resultado - num3
            print("La resta de", resultado, "-", num3, "es igual a", resultado2)
            if resultado2 > 0:
                print("Sobra", resultado2)
            else:
                print("No sobra nada.")
        else:
            print("No se puede restar nuevamente.")
        break
    elif num2 > num1:
        print("El número", num2, "es mayor que", num1)
        resultado = num2 - num1
        print("La resta de", num2, "-", num1, "es igual a", resultado)
        if resultado > 0:
            print("Como el resultado es mayor que cero, se puede restar nuevamente.")
            num3 = int(input("Introduce el tercer número: "))
            resultado2 = resultado - num3
            print("La resta de", resultado, "-", num3, "es igual a", resultado2)
            if resultado2 > 0:
                print("Sobra", resultado2)
            else:
                print("No sobra nada.")
        else:
            print("No se puede restar nuevamente.")
        break
    else:
        print("Los números son iguales. Inténtalo de nuevo.")