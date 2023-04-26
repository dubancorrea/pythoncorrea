
num=1
cont=0
sum=0
menor=0
mayor=0
promedio=0
while num!=0:
    num=int(input('ingrese numero'))
    cont=cont+1
    sum=sum+num
    num+=num
print(f'fueron ingresados {cont-1} numeros')
print(f'La suma de los numeros es {sum}')