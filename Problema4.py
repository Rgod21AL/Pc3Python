        
class Rectangulo:
    def __init__(self, largo, ancho) -> None:
        self.largo = largo
        self.ancho = ancho
        pass
#Metodos 
    def setArea(self):
        """Metodo que calcula el area del rectangulo"""
        getArea = self.largo*self.ancho
        print(f"El area es {getArea}u^2")

    def description(self):
        """Metodo que describe los atributos del objeto"""
        return f"Se tiene un rectangulo de ancho = {self.ancho} y largo = {self.largo}"

def get_num(msg: str)->int:
    """Solicita un número y verifica que sea valido"""
    try:
        x = float(input(msg))
        if x>0:
            return x
        else:
            return get_num("Este valor tiene que ser un entero positivo, intentelo de nuevo: ")
    except:
        return get_num("ERROR! Por favor, ingrese un valor valido: ")

l=get_num("Ingrese el largo del rectangulo: ")
a=get_num("Ingrese el ancho del rectangulo: ")

rectangulo1 = Rectangulo(l,a)

print(rectangulo1.description())

rectangulo1.setArea()