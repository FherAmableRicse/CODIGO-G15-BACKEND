listaNombre = []
strNombre = "cesar mayta"
for i in strNombre:
  listaNombre.append(i)
print(listaNombre)

listaNombre = [i for i in strNombre]
print(listaNombre)

listaNumeros = [i for i in range(101)]
print(listaNumeros)

listMultiploDeDos = [i for i in listaNumeros if i % 2 == 0]
print(listMultiploDeDos)

