
#El sistema le pedira a la persona que ingrese una frase y una letra, mostrara cuantas veces aparece en la frase
frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))