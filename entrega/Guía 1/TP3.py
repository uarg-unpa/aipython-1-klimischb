#TP3
#1 Iterar de 0 a 100 usando un bucle while y mostrar dichos números.
#2 Tomar el ejercicio 1 y realizarlo con un bucle for, tip usar range. los números deben salir uno al lado del otro.
#3 Iterar de 10 a 0 usando un bucle while y un bucle for.
#4 Escribir un programa que pida al usuario dos números enteros e imprima todos los números entre ellos.
#5 Escribe un bucle que haga siete llamadas a print(), de modo que obtengamos UN TRIANGULO

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
