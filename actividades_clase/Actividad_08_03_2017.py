#Programa para sumar numeros flotantes
n1=0.3
n2=4.8
n3=5.9
n4=6.1
n5=5.4
suma=(n1+n2+n3+n4+n5)
print(suma)
#Segundo programa
numero=501
if numero == 500:
    print('Es igual a 500')
elif numero < 1000:
        print('Es menor a 1000')
elif numero>1000:
    print('Es mayor a 1000')
else:
    print('El numero es igual a 1000')
#Programa para calcular el area de un triangulo

b=30
h=20
area= (b*h) / (2)
print(area)
#Programa para calcular la hipotenusa de un triangulo

import math
lado1=20
lado2=20
print(str(math.sqrt(lado1*lado1)+(lado2*lado2)))


#Programa para encontrar numero par e impar
numeros=('5,6,7,8,9')
for i in numeros:
    if i == ',':
        t=0
    else:
        if int(i)%2==0:
            print('numero par'+' '+i)






