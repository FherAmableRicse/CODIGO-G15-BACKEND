"""
Atar a la rata
radar
oso
ana
"""
palabraInicial = input("escribe una palabra : ")
palabraInicial = palabraInicial.replace(' ', '').lower()
palabraReversa =  palabraInicial[::-1]
if(palabraInicial == palabraReversa):
    print("Es un palindromo")
else:
    print("No es un palindromo")
