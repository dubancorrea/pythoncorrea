
#El sistema le pedira al usuario que ingrese la cantidad de jueguos de play que tiene y  mostrara en pantalla si tiene muchos juegos
cantidad_juegos = int(input("¿Cuantos juegos tiene? "))
if cantidad_juegos < 20: 
    print ("tiene pocos juegos, no eres gamer")
else:
    print("tiene muchos juegos, es un gamer de verdad")