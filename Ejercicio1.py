
while True:
    try:
        numTarjeta = int(input("Ingrese el numero de su tarjeta: "))
        if numTarjeta>0:
            break
        else:
            print("No es un numero valido, intentelo de nuevo")
    except:
        print("ERROR, intentelo de nuevo")



