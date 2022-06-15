"""
EJERCICIO 01:
INGRESE UN TEXTO Y UN DIVISOR Y LUEGO MUESTRE EL MISMO TEXTO PERO DIVIDIDO POR EL DIVISOR
EJEMPLO:
INGRESO
TEXTO = 
A B C D E F G
0 1 2 3 4 5 6
DIVISOR = 2
RESULTADO:
AB
CD
EF
G

"""

#ENTRADA
texto = input("ingresa texto: ")
divisor = int(input("ingresa divisor: "))
#PROCESO
for contador in range(0,len(texto),divisor):
    #SALIDA
    print(texto[contador:divisor+contador])