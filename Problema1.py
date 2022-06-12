while True:

    while True:
        fraccion = input("Ingrese la fraccion que registra en estos momentos: ")

        lista = fraccion.split("/")
        try:
            x = int(lista[0]) #Numerador
            y = int(lista[1]) #Denominador
            break
        except ValueError as mistake:
            print(mistake)
            print("Uno o ambos terminos de la fraccion no son numeros enteros, intentelo de nuevo.")

    try:
        resultado = x/y
        if x==y:
            print("COMBUSTIBLE: FULL")
            break
        elif x<y:
            print(f"COMBUSTIBLE: {int(resultado*100)}%")
            break
        elif resultado<0.01:
            print("COMBUSTIBLE: EMPTY")
        elif x>y and y!=0:
            print("Fraccion no valida (Numerador > Denominador). Intentelo de nuevo")
    except ZeroDivisionError as e:
            print("It can't be divided because it is a",e,". Try again")



