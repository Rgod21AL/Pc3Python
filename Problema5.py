
class Alumno:
    def __init__(self, nombre, num_registro) -> None:
       self.nombre = nombre
       self.num_registro = num_registro
#Metodos
    def Display(self):
        """Metodo que describe los atributos del objeto"""
        return f"""Estudiante: {self.nombre}\nNumero de registro: {self.num_registro}"""
    def setAge(self, edad):
        return f"Edad: {edad}"

    def setNotas(self, n1, n2, n3):
        return f"""Nota1: {n1}\nNota2: {n2}\nNota3: {n3}"""

def get_int(msg: str)->int:
    """Solicita un número entero positivo y verifica que la cantidad sea valida"""
    try:
        x = int(input(msg))
        if x>=0 and x<=20:
            return x
        else:
            return get_int("Por favor, ingrese un nota entre 0 y 20: ")
    except:
        return get_int("ERROR! Por favor, ingrese un valor valido: ")

student = Alumno('Rodrigo Apaza Alva', 293077)

while True:
    try:
        age = int(input("Cuantos años tiene?: "))
        if age>0 and age<100:
            break
        else:
            print("Edad no valida, ingrese otro valor")   
    except:
        print("Error!!, por favor ingrese una valor valido")

grade1 = get_int("Cuanto obtuvo en el primer examen?: ")
grade2 = get_int("Cuanto obtuvo en el segundo examen?: ")
grade3 = get_int("Cuanto obtuvo en el tercer examen?: ")

print(f"\n{student.Display()}")

print(student.setAge(age))

print(student.setNotas(grade1, grade2, grade3))
