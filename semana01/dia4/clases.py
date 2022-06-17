#crear una clase
class Automovil:
    #crear atributos
    def __init__(self, aa,pl,col,mar):
        self.anio = aa
        self.placa = pl
        self.color = col
        self.marca = mar

    #crear metodos
    def enceder(self):
        print('enceder : ' + self.marca)

    def avanzar(self):
        print('avanzar : ' + self.marca)

    def acelear(self):
        print('acelear : ' + self.marca)

    def frenar(self):
        print('frenar : ' + self.marca)

#creacion de objetos
vw = Automovil(1970,'CH-1234','Amarillo','Volskwagen')
print("se creo el objeto vw con los siguientes datos :" )
print(" anio :" + str(vw.anio))
print(" color :" + vw.color)
print(" placa :" + vw.placa)
print(" marca :" + vw.marca)

vw.enceder()

