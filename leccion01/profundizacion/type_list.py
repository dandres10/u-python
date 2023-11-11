#listas son mutables

nombres1 = ['Juan', 'Pepe', 'Pedro']
nombres2 = 'Laura Maria Gonzalo Ernesto'.split()

# sumar listas
print(f'Sumar listas {nombres1 + nombres2}')

#Extender la lista
nombres1.extend(nombres2)
print(f'Extender la lista1 {nombres1}')

#lista de numeros
numeros1 = [10, 40, 15, 4, 20, 90, 4]
#obtener el inice del primer elemento encontrado en la lista
print(numeros1)
print(f'numero 4 en q posicion esta en la lista: {numeros1.index(4)}')

#invertir el orden de una lista
numeros1.reverse()
print(f'Lista invertida: {numeros1}')

#ordenar los elementos de una lista menor a mayor
numeros1.sort()
print(f'lista ordenada: {numeros1}')

#ordenar los elementos de una lista mayor a menor
numeros1.sort(reverse=True)
print(f'lista ordenada mayor a menor: {numeros1}')

#obtener el valor maximo y minimo de una lista
print(f'valor minimo de la lista: {min(numeros1)}')
print(f'valor maximo de la lista: {max(numeros1)}')

#copiar una lista en otra
numeros2 = numeros1.copy()
print(numeros2)
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

#podemos usar el constructor de la lista para crear una copia
numeros2 = list(numeros1)
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

#slicing
numeros2 = numeros1[:]
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

#multiplicacion de listas
lista_multiplicacion = 5*[[2,5]]
print(lista_multiplicacion)
print(f'Misma referencia? {lista_multiplicacion[0] is lista_multiplicacion[1]}')
print(f'Mismo contenido? {lista_multiplicacion[0] == lista_multiplicacion[1]}')

#matrices
matriz = [[10,20], [30, 40, 50], [60,70,80, 90]]
print(matriz)
print(f'reglon 0 columna 0: {matriz[0][0]}')
print(f'reglon 0 columna 0: {matriz[2][2]}')

lista_listas = [[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
lista_listas.sort(key=len)
print(lista_listas)

# sorted built-in
# help(sorted)

nombres1 = ['Laura', 'Viviana', 'Andres']
nombres1 = sorted(nombres1)
print(nombres1)

nombres1 = ['Laura', 'Viviana', 'Andres']
nombres1 = sorted(nombres1,reverse=True)
print(nombres1)

#ordenar por la cantidad de caracteres
nombres1 = sorted(nombres1,key=len)
print(nombres1)

nombres1 = reversed(nombres1)
print(list(nombres1))


