l1 = int(input("Lado 1: "))
l2 = int(input("Lado 2: "))
l3 = int(input("Lado 3: "))

print('Si lado 1 =',l1,', lado 2 =',l2,'y lado 3 =',l3,', el tipo de triangulo es: ')
if l1==l2==l3:
  print('Equilatero')
elif l1==l2 or l2==l3 or l1==l3:
  print('Isósceles')
else:
  print('Escaleno')