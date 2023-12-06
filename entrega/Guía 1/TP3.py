#### TP3 ####Lo logramos
### 1 Iterar de 0 a 100 usando un bucle while y mostrar dichos números.
cont=0
while(cont<=100):
    print(cont)
    cont=cont+1
#
### 2 Tomar el ejercicio 1 y realizarlo con un bucle for, tip usar range. los números deben salir uno al lado del otro.
for num in range (0, 101,1):
    print(num,end="")
    print(end="")
#
### 3 Iterar de 10 a 0 usando un bucle while y un bucle for.
#Bucle while de 10 a o
cont=10
while(cont>=0):
    print(cont,end="")
    cont=cont-1
    print(end="")
#Bucle for
for num in range (11, -1,-1):
    print(num)
#
### 4 Programa que pide al usuario dos números enteros e imprime todos los números entre ellos.
num1=int(input("Ingrese el primer numero"))
num2=int(input("Ingrese el segundo numero"))
for num in range (num1,num2,1):
    print(num) 
#
###5 Bucle de siete llamadas a print(), de modo que obtengamos UN TRIANGULO
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")