print("BOLETA")
print ("")
ESC = input ("INGRESA EL NOMBRE DE LA ESCUELA:  ")
print ("")
NOM = input ("INGRESA TU NOMBRE: ")
print ("")
GRdo = input ("INGRESA TU GRADO: ")
print ("")
GRPO = input ("INGRESA TU GRUPO: ")
print ("")
MAT1 = input ("INGRESA LA MATERIA 1:  ")
print ("")
MAT2 = input ("INGRESA LA MATERIA 2:  ")
print ("")
MAT3 = input ("INGRESA LA MATERIA 3:  ")
print ("")
MAT4 = input ("INGRESA LA MATERIA 4:  ")
print ("")
print (MAT1)
CAL1 = int(input ("INGRESA LA CALIFICACION 1:  "))
print ("")
CAL2 = int(input ("INGRESA LA CALIFICACION 2:  "))
print ("")
CAL3 = int(input ("INGRESA LA CALIFICACION 3:  "))
print ("")
print ("")
print (MAT2)
CALI1 = int(input ("INGRESA LA CALIFICACION 1:  "))
print ("")
print ("")
CALI2 = int(input ("INGRESA LA CALIFICACION 2:  "))
print ("")
print ("")
CALI3 = int(input ("INGRESA LA CALIFICACION 3:  "))
print ("")
print ("")
print (MAT3)
CALFI1 = int(input ("INGRESA LA CALIFICACION 1:  "))
print ("")
print ("")
CALFI2 = int(input ("INGRESA LA CALIFICACION 2:  "))
print ("")
print ("")
CALFI3 = int(input ("INGRESA LA CALIFICACION 3:  "))
print ("")
print ("")
print (MAT4)
CALIFI1 = int(input ("INGRESA LA CALIFICACION 1:  "))
print ("")
print ("")
CALIFI2 = int(input ("INGRESA LA CALIFICACION 2:  "))
print ("")
CALIFI3 = int(input ("INGRESA LA CALIFICACION 3:  "))
print ("")

print(ESC)
print("NOMBRE " + NOM)
print ("")
print("GRADO " + GRdo + " GRUPO "+ GRPO)
print ("")
prom1 = int
prom1 = (CAL1 + CAL2 + CAL3 )/3
prom2 = int
prom2 = (CALI1 + CALI2 + CALI3 )/3
prom3 = int
prom3 = (CALFI1 + CALFI2 + CALFI3 )/3
prom4 = int
prom4 = (CALIFI1 + CALIFI2 + CALIFI3 )/3
print("MATERIA " + ("  P1  ") + (" P2  ")+("   P3  ")  + (" PROMEDIO"))
print (f"{MAT1}   {CAL1}   { CAL2}     { CAL3}     {prom1:.2f}" )
print (f"{MAT2}   {CALI1}   { CALI2}     { CALI3}     {prom2:.2f}" )
print (f"{MAT3}   {CALFI1}   { CALFI2}     { CALFI3}     {prom3:.2f}" )
print (f"{MAT4}   {CALIFI1}   { CALIFI2}     { CALIFI3}     {prom4:.2f}" )
print("")
PROMF = int
PROMF = (prom1 + prom2 + prom3 + prom4) / 4
print("PROMEDIO FINAL")
print(f"{PROMF:.2f}")
print("\nGUILLEN MARTINEZ ANTHONY 20210575")