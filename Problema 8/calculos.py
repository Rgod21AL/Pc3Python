import operaciones

n1 = operaciones.get_float("Ingrese el primer numero: ")

n2 = operaciones.get_float("Ingrese el segundo numero: ")

MENU="""BIENVENIDO A SU MENU DE OPCIONES
[1]. Determinar suma
[2]. Hallar diferencia (n1-n2)
[3]. Mostrar Producto
[4]. Calcular cociente
[5]. Salir
Opcion: """

while True:
    opcion = input(MENU)
    if opcion == '1':
        print(operaciones.suma(n1,n2))
    elif opcion == '2':
        print(operaciones.resta(n1,n2))
    elif opcion == '3':
        print(operaciones.producto(n1,n2))   
    elif opcion == '4':
        print(operaciones.division(n1,n2))   
    elif opcion =='5':
        print("¡Hasta pronto! Ha sido un placer ayudarte")
        break
    else:
        print("Opcion no valida, vuelve a intentarlo")