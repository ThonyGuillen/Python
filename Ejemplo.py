import os
import keyword 

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()
# Solicitamos un identificador al usuario
identificador = input("Ingrese un identificador: ")

# Verificamos si el identificador es válido
ide = identificador.isidentifier()

print(ide)
