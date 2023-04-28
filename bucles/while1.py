
# num=1
# print(type(num))
# num="sena"
# print(type(num))
num=1
cont=0 #Variable contador
sum=0
menor=1000000
mayor=0
while num!=0:
    num=int(input('ingrese numero'))
    cont=cont+1 #Contador que sume la variable mas 1
    sum=sum+num #Suma del numero ingresado mas la suma 
    if num>mayor:
        mayor=num
    if num<menor and num!=0:#Numero menor excluyendo el 0
        menor=num

print(f'fueron ingresados {cont-1} numeros')
print(f'La suma es {sum}')
print(f'El promedio es {sum/(cont-1)}')
print(f'El mayor es {mayor}')
print(f'El menor es {menor}')