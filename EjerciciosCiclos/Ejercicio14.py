#Calcular todos los números de 3 cifras tales que la suma
#de los cubos de las cifras es igual al valor del número.
#153   
#773 / 7x7x7:343 / 7x7x7:343 / 3x3x3: 27 ///// Un numero anterior 
#337 / 
#397
u=0
d=0
c=0

for i in range (100, 1000):
     num=i
     u= num%10
     num=num//10
     d= num%10
     c= num//10
     print(c, d, u)
     cubo= (c**3)+(d**3)+(u**3)
     if cubo==i:
          print(i)