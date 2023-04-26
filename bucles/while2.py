num1=3
num2=5
cont=1
while not(num1%num2==0 or num2%num1==0):
    num1= int(input('Ingrese numero'))
    num2= int(input('Ingrese numero'))
    cont+=1
print (f'{num1}y{num2} son factor')

