
class Circulo:
    color= "negro"    #Atributo de clase
    def __init__(self, radio):
        self.radio=radio  #Atributo de instancia --> Varía segun el objeto que se cree
    pass

#Métodos de instancia
    def area(self):
        """Metodo que calcula el area del circulo"""
        area = self.radio**2
        print(f"El area es {area}π u^2") #Imprimimos

    def description(self):
        """Metodo que describe los atributos del objeto"""
        return f"Se tiene un circulo de circunferencia color {self.color} y radio {self.radio}" #Otra manera de imprimir

def get_num(msg: str)->int:
    """Solicita un número y verifica que sea valido"""
    try:
        x = float(input(msg))
        if x>0:
            return x
    except:
        return get_num("ERROR! Por favor, ingrese un valor valido para el radio: ")

r=get_num("Ingrese el radio del circulo: ")

circle1 = Circulo(r)     #Creamos un objeto de la clase Circulo

print(circle1.description())        #print(f"Radio: {circle.radio}") <--- Otra manera de mostrar el radio que se ingresó

circle1.area() #Se imprime el valor del área

print(circle1) # Imprimir posición de memoria del objeto