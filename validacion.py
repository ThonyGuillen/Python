import os
import re

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()
dato = input("Ingrese un dato: ")

if re.match(r"^[a-zA-Z0-9_-]{6,12}$", dato):
    print("El dato ingresado (" + dato + ") es un ID.")
elif re.match(r"^[0-9]+$", dato):
    print("El dato ingresado (" + dato + ") es un número")
elif re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", dato):
    print("El dato ingresado (" + dato + ") es un correo.")
elif re.match(r"^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", dato):
    print("El dato ingresado (" + dato + ") es una URL")
else:
    print("El dato ingresado no es válido.")

