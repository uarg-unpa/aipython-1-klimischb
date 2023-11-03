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
#
#
cont=0
while(cont<=10):
    print(cont)
    cont=cont+1
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
cadena="barbi"
if "i" in cadena:
    print("Barby")
for letra in cadena:
    print(letra)

for _ in range(3):
    print('un mensaje que se repiter 3 veces')
