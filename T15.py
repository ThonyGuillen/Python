def cantidad_vocales(cadena):
    cant=0
    for x in range(len(cadena)):
            cant=cant+1
    print("Cantidad de vocales de la palabra" , cadena, "es", cant)
   
#Bloque principal
cantidad_vocales("administracion")
cantidad_vocales("hola mundo")
cantidad_vocales("ana")