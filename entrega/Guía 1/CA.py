## Yo le digo la altura al triángulo (introduciendo un entero)
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")
#
## Genera un triángulo de 7 niveles
for i in range(7):
    for j in range(i+1):
        print("*", end="")
    print("")
#
##
print("ingrese usuario")
usuario=input()
print("ingrese numero")
numero=input()
print((usuario + "\n") * int(numero))