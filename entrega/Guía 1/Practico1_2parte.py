#Pratico1
#Punto3
nombre="Barbara"
print(nombre)
apellido="Klimisch"
print(apellido)
edad="36"
print(edad)
altura="1.72"
print(altura)
vuelo="1803"
print(vuelo)
temperatura_ambiente = "29 grados"
print(temperatura_ambiente)
salario_mensual="pesos 1 millon"
print(salario_mensual)
fin_juego="game over"
print(fin_juego)
inicio_juego="start game"
print(inicio_juego)
#Variables del ejercicio 3,¿con qué literales se asocian?
print("ingrese su nombre")
nombre=input()
print("ingrese su apellido")
apellido=input()
print("ingrese su edad")
edad=input()
print("Ser Creativo")
# Programa de dos números enteros:
num1=int(input("Ingrese el primer numero"))
num2=int(input("Ingrese el segundo numero"))
suma=(num1 + num2)
print(suma)
resta=(num1 - num2)
print(resta)
producto=(num1 * num2)
print(producto)
potencia=(num1 ** num2)
print(potencia)
resto=(num1//num2)
print(resto)
print('"fin de las operaciones"')
#7. Modificar el ejercicio 6 para que reciba un entero y un float.
 #   
cont=0
suma=0
while(cont<3):
    nota=int(input("ingrese nota"))
    suma=suma+nota
    cont=cont+1
promedio=suma/cont
print(f"el promedio es {promedio}")
#
cont=0
while(cont<=10):
    print(cont)
    cont=cont+1
#
cadena="BarbY"
if "Y" in cadena:
    print("Genia")
for letra in cadena:
    print(letra)
for _ in range(3):
    print('un mensaje que se repiter 3 veces')
