import os
import sys

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")



CONTRASEÑA = input("INGRESE LA CONTRASEÑA: ")
if(len(CONTRASEÑA) >=  8):
  print("TU CONTRASEÑA ES SUFICIENTEMENTE LARGA")
  print("")
  if (CONTRASEÑA == 'Holamundo'):
    print ("ADEMAS ES LA CONTRASEÑA CORRECTA")
    print("")
  else:
      print("PERO ES INCORRECCTA ")
      while CONTRASEÑA != "Holamundo":
       print("")
       print ("LA CONTRASEÑA ES INCORRECTA, INTENTALO DE NUEVO")
       print("")
       CONTRASEÑA = input("INTRODUCE CONTRASEÑA: ")

else:
  print("TU CONTRSEÑA ES MUY CORTA E INSEGURA")
  while (len(CONTRASEÑA) <=  8):
       print("")
       print ("LA CONTRASEÑA ES MUY CORTA, INTENTALO DE NUEVO")
       print("")
       CONTRASEÑA = input("INTRODUCE CONTRASEÑA: ")
print("")
clear()
print ("WELCOME ING. ANTHONY, ES UN GUSTO. ")
print ("")

def mostrar_menu(opciones):
    
    print ("=============================================================")
    print ("=                        MENU                               =")
    for clave in sorted(opciones):
        print(f'= ({clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    print("")
    while (a := input('= INCISO A ELEGIR: ')) not in opciones:
      print("")
      print('ESA OPCION NO ES VALIDA, ELIGA OTRA.')
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
      '1': ('= CALCULAR AREA Y PETRIMETRO DE UN CUADRADO           =', accion1),
      '2': ('= CALCULAR AREA Y PETRIMETRO DE UN TRIANGULO          =', accion2),
      '3': ('= CALCULAR AREA Y PETRIMETRO DE UN RECTANGULO         =', accion3),
      '4': ('= CONTADOR DE LETRAS                                  =', accion4),
      '5': ('= INGRESAR PALABRA                                    =', accion5),
      '6': ('= CONTRASEÑA                                          =', accion6),
      '7': ('= LISTA                                               =', accion7),
      '8': ('= SALIR                                             =', salir),
    }

    generar_menu(opciones, '4')


def accion1():
 clear()
 NUM1 = float(input("INGRESA LA LONGITUD DE UN LADO: "))
 print("")
 AREA = float
 PER = float
 AREA = NUM1*NUM1
 PER = NUM1 * 4
 print(f"EL AREA DEL CUADRADO ES {AREA:.2f} CM^2" )
 print("")
 print(f"EL PERIMETRO DEL CUADRADO ES {PER:.2f} CM")
 print ("")
 print ("=============================================================")
 input("preciones para continuar")
 clear()
  

def accion2():
 clear()
 NUM1 = float(input("INGRESA LA BASE: "))
 print("")
 NUM2 = float(input("INGRESA LA ALTURA: "))
 print("")
 AREA = float
 PER = float 
 AREA = NUM1*NUM2
 PER = 2*(NUM1+NUM2)
 print(f"EL AREA DEL RECTANGULO ES {AREA:.2f} CM^2" )
 print("")
 print(f"EL PERIMETRO DEL RECTANGULO ES {PER:.2f} CM")
 print ("")
 print ("=============================================================")
 input("preciones para continuar")
 clear()

def accion3():
 clear()
 NUM1 = float(input("INGRESA LA ALTURA "))
 print("")
 NUM2 = int(input("INGRESA LA BASE: "))
 print("")
 NUM3 = float(input("INGRESA EL LADO 1 "))
 print("")
 NUM4 = float(input("INGRESA EL LADO 2: "))
 print("")
 AREA = float
 PER = float 
 AREA = (NUM2*NUM1)/2
 PER = NUM2+NUM3+NUM4
 print (f"EL AREA DEL RECTANGULO ES {AREA:.2f} CM^2" )
 print ("")
 print (f"EL PERIMETRO DEL RECTANGULO ES {PER:.2f} CM")
 print ("")
 print ("=============================================================")
 input("preciones para continuar")
 clear()

def accion4():
  clear()
  CADENA = input ("INGRESA UNA CADENA: ")
  print ("")
  print (len (CADENA))
  print ("ES LA CANTIDAD DE PALABRAS QUE TIENE LA CADENA ")
  print ("")
  print ("=============================================================")
  input("preciones para continuar")
  clear()
def accion5():
  clear()
  NUMEROS = ["UNO ","DOS","TRES","CUATRO","CINCO","SEIS","SIETE","OCHO","NUEVE","DIEZ" ] 
  print ("NUMEROS EN EL ARREGLO")
  print ("") 
  for X in NUMEROS: 
     print(X)

  print("")
  COL = input("¿QUE NUMERO QUIERES AGREGAR? ")
  print("")
  POS = int (input("¿EN QUE POSICION? " ))
  print("")
  NUMEROS.insert(POS,COL)
  print("NUEVO NUMERO EN EL ARREGLO")
  print("")
  for X in NUMEROS:
     print(X)
  print ("")
  print ("=============================================================")
  input("preciones para continuar")
  clear()
  
def accion6():
  clear()
  CONTRASEÑA = input("INTRODUCE LA CONTRASEÑA: ")
  while CONTRASEÑA != "GYM":
    print("")
    print ("LA CONTRASEÑA ES INCORRECTA INTENTALO DE NUEVO")
    print("")
    CONTRASEÑA = input("INTRODUCE LA CONTRASEÑA: ")

  print("")
  print("CONTRASEÑA CORRRETA")
  print ("")
  print ("=============================================================")
  input("preciones para continuar")
  clear()
def accion7():
  clear()
  M1 = input ("INGRESA TU NOMBRE: ")
  print("")
  M2 = input ("INGRESA TU APELLIDO PATERNO: ")
  print("")
  M3 = input ("INGRESA TU APELLIDO MATERNO: ")
  print("")
  M4 = input ("INGRESA EDAD: ")
  print("")
  M5 = input ("INGRESA COLOR DE PIEL: ")
  print("")
  print("COMIENZO")
  for i in [M1, M2, M3, M4, M5]:
    print(f"Hola. Ahora i vale {i}")
  print("FINAL") 
  print ("")
  print ("=============================================================")
  input("preciones para continuar")
  clear()

def salir():
  sys.exit()
  input("preciones para continuar")
  clear()

if __name__ == '__main__':
    menu_principal()