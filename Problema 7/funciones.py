import random

lista_numeros = []

def generar_numeros(x: int):
    """Genera numeros aleatorios entre el 0 y 100"""
    for i in range(1,x+1):
        lista_numeros.append(random.randint(1,100))

def mostrar_lista():
    """Muestra la lista con los valores unicos"""
    print(lista_numeros)

def ordenar_lista():
    """Muestra la lista con los valores ordenados"""
    lista_numeros.sort() #Metodo para ordenar de forma ascendente
    print(lista_numeros)

def get_int(msg: str)->int:
    """Solicita un número entero y verifica que la cantidad sea valida"""
    try:
        x = int(input(msg))
        if x>1:
            return x
        else:
            return get_int("El numero ingresado debe ser un entero positivo, intentelo de nuevo: ")
    except:
        return get_int("ERROR! Por favor, ingrese un valor valido: ")
    


