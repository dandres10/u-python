#while

condicion = 1

while condicion < 3:
    condicion += 1
    print('Ejecutando ciclo while')
else:
    print(f'fin del cilo while')

#For

cadena = 'Hola'

for letra in cadena:
    print(letra)
else:
    print('fin ciclo for')


#For with break
cadena = 'Holanda'
for letra in cadena:
    if letra == 'a':
      print(f'Letra encontrada: {letra}')
      break
else:
    print('fin ciclo for')

# For continue
# first example
for i in range(6):
    if i % 2 == 0:
     print(f'Valor: {i}')
# second example
print(f'second example')
for i in range(6):
    if i % 2 != 0:
     continue
    print(f'valor: {i}')
