"""
Incorporar un menu de opciones para el programa monedas que 
tenga 3 opciones 1 - convertir de soles a dolares 2 - convertir 
de dolares a soles 3 - salir , y que se ejecute con un ciclo while 
mientras la opción no sea salir, si selecciono la opción salir debe 
terminar el programa
"""
montoOrigen = input("Ingrese el monto: ")
montoDestino = 0
opcion = "0"
while(opcion != "3"):
    print(" Opción 1 - Soles a dolares")
    print(" Opción 2 - Dolares a soles")
    print(" Opción 3 - Salir")
    opcion = input("Elija una opción :")
    if(opcion=="1"):
        montoDestino = float(montoOrigen) / 3.778
        montoFormato = " $ {:,.2f}".format(montoDestino)
        print("-----------------------------------------")
        print("El monto en dolares es :" + str(montoFormato))
        print("-----------------------------------------")
    elif(opcion=="2"):
         montoDestino = float(montoOrigen) * 3.778
         montoFormato = " S/. {:,.2f}".format(montoDestino)
         print("-----------------------------------------")
         print("El monto en soles es : " + str(montoFormato))
         print("-----------------------------------------")
    elif(opcion=="3"):
         print("Finalizando programa...")
         exit()
    else:
       print("-----------------------------------------")
       print("Seleccione una opción válida")
       print("-----------------------------------------")
       opcion = "0" 

