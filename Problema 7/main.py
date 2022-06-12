import funciones
MSG="""BIENVENIDO A SU MENU DE OPCIONES
[1]. Generar numeros aleatorios entre 0 y 100
[2]. Mostrar lista con los numeros
[3]. Ordenar valores y mostrar la nueva lista
[4]. SALIR
Opcion: """

while True:
    opcion=input(MSG)
    if opcion == '1':
        cantidad=funciones.get_int('Cantidad de numeros: ')
        funciones.generar_numeros(cantidad)
    elif opcion == '2':
        funciones.mostrar_lista()
    elif opcion == '3':
        funciones.ordenar_lista()
    elif opcion == '4':
        print("Gracias por usar el programa, vuelva pronto!")
        break
    else:
        print("Opcion no valida, intentelo de nuevo")