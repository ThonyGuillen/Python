from math import degrees
from tkinter import *
from tkinter import messagebox
import webbrowser

calculadora = Tk()
calculadora.geometry("312x394")
calculadora.resizable(0, 0)
calculadora.title("Calculadora")

#-------------------------------------------------FUNCIONES-------------------------------------------------
def portada():
    messagebox.showinfo('Portada',"Nombre: \nGuillen Martinez Anthony \n\nNo. Control \n20210575 \n\nMateria: \nLenguaje de Interfaz \n\nTitulo: \nExamen II \n\nDocente: \nCAÑEZ VALLE RODRIGO")
    
def web():
    webbrowser.open("https://www.youtube.com/watch?v=BtLSaxRnIhc")
    
def botonclick(item): 
    global expresion
    inputText.set(inputText.get()+(str(item)))

def borrar():
    global expresion
    expresion = ""
    inputText.set(inputText.get()[0:-1])

def clear():
    inputText.set("")

def calcular():
    resultado = ""
    try:
        resultado = eval(inputText.get())
        inputText.set(resultado)
    except:
        resultado = "_ERROR_"
        inputText.set(resultado)

#-------------------------------------------------BARRA MENU-------------------------------------------------
menubarra = Menu(calculadora,bg="#f0e4e1",fg="grey")
archivomenu = Menu(menubarra, tearoff=0,bg="#f0e4e1",fg="black")
menubarra.add_cascade(label="INICIO", menu=archivomenu)
archivomenu.add_command(label="PORTADA", command=portada)
archivomenu.add_command(label="NO ABRIR", command=web)
archivomenu.add_separator()
archivomenu.add_command(label="SALIR", command=calculadora.quit)

calculadora.config(bg="grey",menu=menubarra)  

#-------------------------------------------------FRAME-------------------------------------------------
expresion = ""
inputText = StringVar()

#Entrada Frame
inputFrame = Frame(calculadora, width=312, height=50, bd=0, highlightbackground="#d9b7c0", highlightcolor="crimson", highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('arial', 17 ), textvariable=inputText, width=50,fg="black", bg="#bcacb6", bd=0, justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=19)

#Boton Frame
button_frame = Frame(calculadora, width=312, height=272.5, bg="#a26b9c")
button_frame.pack()

#-------------------------------------------------BOTONES-------------------------------------------------
#Fila 1
limpiar = Button(button_frame, text = "C", fg = "black", width = 10, height = 3, bd = 0, bg = "#d9b7c0", cursor = "hand2", command = lambda: clear()).grid(row = 1, column = 0, padx = 1, pady = 1)
pi= Button(button_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "#d9b7c0", cursor = "hand2", command = lambda: botonclick("(")).grid(row = 1, column = 1, padx = 1, pady = 1)
pd = Button(button_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "#d9b7c0", cursor = "hand2", command = lambda: botonclick(")")).grid(row = 1, column = 2, padx = 1, pady = 1)
borr = Button(button_frame, text = "<", fg = "black", width = 10, height = 3, bd = 0, bg = "#d9b7c0", cursor = "hand2", command = lambda: borrar()).grid(row = 1, column = 3, padx = 1, pady = 1)

#Fila 2
elevacion = Button(button_frame, text = "^", fg = "black", width = 10, height = 3, bd = 0, bg = "#d9b7c0", cursor = "hand2", command = lambda: botonclick("**")).grid(row = 2, column = 0, padx = 1, pady = 1)
pi = Button(button_frame, text = "π", fg = "black", width = 10, height = 3, bd = 0, bg = "#d9b7c0", cursor = "hand2", command = lambda: botonclick(3.1416)).grid(row = 2, column = 1, padx = 1, pady = 1)
e  = Button(button_frame, text = "e", fg = "black", width = 10, height = 3, bd = 0, bg = "#d9b7c0", cursor = "hand2", command = lambda: botonclick(2.71828)).grid(row = 2, column = 2, padx = 1, pady = 1)
divicion= Button(button_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#d9b7c0", cursor = "hand2", command = lambda: botonclick("/")).grid(row = 2, column = 3, padx = 1, pady = 1)

#Fila 3
siete = Button(button_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#bcacb6", cursor = "hand2", command = lambda: botonclick(7)).grid(row = 3, column = 0, padx = 1, pady = 1)
ocho = Button(button_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#bcacb6", cursor = "hand2", command = lambda: botonclick(8)).grid(row = 3, column = 1, padx = 1, pady = 1)
nueve = Button(button_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#bcacb6", cursor = "hand2", command = lambda: botonclick(9)).grid(row = 3, column = 2, padx = 1, pady = 1)
multiplicacion = Button(button_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#d9b7c0", cursor = "hand2", command = lambda: botonclick("*")).grid(row = 3, column = 3, padx = 1, pady = 1)

#Fila 4
cuatro = Button(button_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#bcacb6", cursor = "hand2", command = lambda: botonclick(4)).grid(row = 4, column = 0, padx = 1, pady = 1)
cinco = Button(button_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#bcacb6", cursor = "hand2", command = lambda: botonclick(5)).grid(row = 4, column = 1, padx = 1, pady = 1)
seis = Button(button_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#bcacb6", cursor = "hand2", command = lambda: botonclick(6)).grid(row = 4, column = 2, padx = 1, pady = 1)
resta = Button(button_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#d9b7c0", cursor = "hand2", command = lambda: botonclick("-")).grid(row = 4, column = 3, padx = 1, pady = 1)

#Fila 5
uno = Button(button_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#bcacb6", cursor = "hand2", command = lambda: botonclick(1)).grid(row = 5, column = 0, padx = 1, pady = 1)
dos = Button(button_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#bcacb6", cursor = "hand2", command = lambda: botonclick(2)).grid(row = 5, column = 1, padx = 1, pady = 1)
tres = Button(button_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#bcacb6", cursor = "hand2", command = lambda: botonclick(3)).grid(row = 5, column = 2, padx = 1, pady = 1)
suma = Button(button_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#d9b7c0", cursor = "hand2", command = lambda: botonclick("+")).grid(row = 5, column = 3, padx = 1, pady = 1)

#Fila 6
punto = Button(button_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#d9b7c0", cursor = "hand2", command = lambda: botonclick(".")).grid(row = 6, column = 0, padx = 1, pady = 1)
cero = Button(button_frame, text = "0", fg = "black", width = 10, height = 3, bd = 0, bg = "#bcacb6", cursor = "hand2", command = lambda: botonclick(0)).grid(row = 6, column = 1, padx = 1, pady = 1)
igual = Button(button_frame, text = "=", fg = "black", width = 21, height = 3, bd = 0, bg = "#d9b7c0", cursor = "hand2", command = lambda: calcular()).grid(row = 6, column = 2, columnspan = 2, padx = 1, pady = 1)
 
calculadora.mainloop()