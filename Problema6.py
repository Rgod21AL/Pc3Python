import math
class Punto:
    def __init__(self, notacion, x, y):
        self.nombre = notacion
        self.abscisa = x
        self.ordenada = y

    def determinar_cuadrante(self):
        if self.abscisa>0 and self.ordenada>0:
            print("Se encuentra en el PRIMER cuadrante")
        elif self.abscisa<0 and self.ordenada>0:
            print("Se encuentra en el SEGUNDO cuadrante")
        elif self.abscisa<0 and self.ordenada<0:
            print("Se encuentra en el TERCER cuadrante")
        elif self.abscisa>0 and self.ordenada<0:
            print("Se encuentra en el CUARTO cuadrante")
        elif self.abscisa!=0 and self.ordenada==0:
            print("Se encuentra en el EJE X")
        elif self.abscisa==0 and self.ordenada!=0:
            print("Se encuentra en el EJE Y")
        elif self.abscisa==0 and self.ordenada==0:
            print("Se encuentra en el ORIGEN de coordenadas")

    def string(self):
        print(f"El punto {self.nombre} es {self.abscisa,self.ordenada}")
    pass

    def vector(self, x, y):
        absFinal = x - self.abscisa
        ordFinal = y - self.ordenada
        print(f"{absFinal, ordFinal}")
    
    def distancia(self, x, y):
        sumaCuadrados = (x-self.abscisa)**2 + (y-self.ordenada)**2
        print(math.sqrt(sumaCuadrados))
      
def get_num(msg: str)->int:
    """Solicita un número y verifica que sea valido"""
    try:
        x = int(input(msg))
        return x
    except:
        return get_num("ERROR! Por favor, ingrese un valor valido: ")

letra = input("Letra del punto: ")
abs = get_num("Abscisa: ")
ord = get_num("Ordenada: ")

punto1 = Punto(letra.upper(), abs, ord)
punto1.string()
punto1.determinar_cuadrante()

punto2 = Punto('B', 1, 2)
punto2.string()
punto2.determinar_cuadrante()
#Punto A = (4,5)
#Punto B = (1,2)
#VECTOR AB = (3,3)

print(f"Vector {punto2.nombre}{punto1.nombre}:") #BA
punto2.vector(punto1.abscisa, punto1.ordenada)
print(f"Vector {punto1.nombre}{punto2.nombre}:")
punto1.vector(punto2.abscisa, punto2.ordenada)

print("Distancia entre A y B")
punto1.distancia(1,2)







