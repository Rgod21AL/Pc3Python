calificaciones = input("Ingrese sus calificaciones [0,20]: ")

lista = calificaciones.split(',')

print(lista) 

num = len(lista)

print("""\tNotas ingresadas
\t----------------""")
for i in range(num):
    try:
        n=int(lista[i])
        if n<0 or n>20:
            print(f"{n} {type(n)} No es una nota valida")
        else:
            print(f"{n}, {type(n)} Nota valida")
    except:
        print("No pudimos convertirlo, debido a un error de formato")

