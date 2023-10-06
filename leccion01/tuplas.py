#definir una tupla
frutas = ('naranja', 'platano', 'guayaba')

# elementos de una tupla
print(len(frutas))

#acceder a un elemento
print(frutas[0])

#navegacion inversa
print(frutas[-1])

# rango de valores
print(frutas[0:1])

#recorrer elementos
for fruta in frutas:
    print(fruta, end=' ')

#cambiar valor de la dupla
frutasLista = list(frutas)
frutasLista[0] = 'pera'
frutas = tuple(frutasLista)
print('\n', frutas)


