print(22+33)
print(22-33)
print(22*33)
print(22/33) #DIVISION COMUN
print(22%33) #MODULO O RESTO 
print(22//33) #DIVISION ENTERA: CUNATO ENTEROS ENTRAN EN ELUMERO
print(22**33)
print(22+33+45)
#Las variables: no pueden tener espacios, ni guion medio o signo menos, no pueden empezar con un numero, ni símbolos, si con minuscula, si con guion bajo, no se pden llamar como un palabra reservada o fx(ej. print)
#Pueden ser numeros o cadenas(ej color=verde)
#Las variables siempre tienen que estar definidas previamente
#VARIABLE(una caja para guardar los literales(numeros, golianos y cadenas)) 
#valor=7 tiene un nombre o identificador, el operador, asignación y un valor ("un algo" adentro de la caja)
#valor=10 el operador asignacion da valor al algo dentro dela caja
#valor=valor + 3
#13
color="rojo"
print(color) #esta línea es ignorada por el intérprete, se conoce como comentario
color=3+5
print("color")
print("\'inteligente\'") 
# #la variable no esta definida
#vARIABLES INMUTABLES ej EDAD=37. Si hacemos 37+1 es otra caja
edad=37
edad=38
print(id(edad))
mi_texto="texto"

print("ingrese su edad")
edad=input()
print("su edad es", edad)
#input("")
input#ingresa datos desde lamcponsola y se lo asignamoda a ala variable

edad=input("ingrese su edad")
print(edad)
#tamaño= len (texto)
mi_texto="python"
una_parte=mi_texto [0:3]