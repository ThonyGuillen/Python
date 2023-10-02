import os


def clear():
    
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def mostrar_menu(opciones):
    print('Seleccione el programa:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Programa 1', accion1),
        '2': ('Programa 2', accion2),
        '3': ('Programa 3', accion3),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')


def accion1():
    clear()
    p1 = input("Nombre: ")
    print("")
    p2 = int(input("Edad: "))
    print("")
    p3 = float(input("Estatura: "))
    print("")
    print("")

    print(f"Hola, mi nombre es {p1}, tengo {p2} años y mido {p3}" )


    input("Precione cualquier tecla para continuar")
    clear()


def accion2():
    clear()
    print('Has elegido la opción 2')
    for i in range(3):
      m1 = float(input("Cuanto mides(centimetros): "))
      m2 = m1/2.54

      print(f"Tu altura de {m1} centimetros, en pulgadas es {m2:.3f}")
      print("")
      print("")

  
    input("Precione cualquier tecla para continuar")
    clear()


def accion3():
    clear()
    p1 = input("Nombre: ")
    print("")
    p2 = int(input("Edad: "))
    print("")
    p3 = float(input("Estatura: "))
    print("")
    p4 = input("Materia: ")
    print("")
    p5 = int(input("Semestre: "))
    print("")
    p6 = float(input("Calificación: "))
    print("")
    print("")

    print(f"Hola, mi nombre es {p1}, tengo {p2} años y mido {p3}" )
    print("")
    print(f"Usted en la materia: {p4}, en el semestre {p5} con calificación de {p6}" )

    print("")
    input("Precione cualquier tecla para continuar")
    clear()



def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()