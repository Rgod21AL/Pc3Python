def get_float(msg: str)->float:
    """Solicita un número real"""
    try:
        x = float(input(msg))
        return x
    except:
        return get_float("ERROR! Por favor, ingrese un valor valido: ")

def suma(x: float,y: float )->float:
    """Calcula la suma entre 2 numeros"""
    return x+y

def resta(x: float,y: float )->float:
    """Calcula la diferencia entre 2 numeros"""
    return x-y

def producto(x: float,y: float )->float:
    """Calcula el producto entre 2 numeros"""
    return x*y

def division(x: float,y: float )->float:
    """Calcula la division entre 2 numeros"""
    try:
        return x/y
    except:
        if y==0:
            print("No es posible dividir entre 0")

