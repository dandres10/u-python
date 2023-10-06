nombres = ['juan', 'karla', 'ricardo', 'maria']

# imprimir la lista de nombres
for nombre in nombres:
    print(nombre)

print(nombres)

# acceder a un elemento de una lista
print(nombres[0])

# acceder al ultimo elemento de la lista
print(nombres[-1])

# rango de una lista
print(nombres[0:2])

# ir del inicio al inice sin incluirlo
print(nombres[ :3])

#ir apartir de un item hasta el final
print(nombres[1: ])

#  cambiar un valor de la lista
nombres[3] = 'Marlon'
print(nombres[3])

# cuantos elementos tiene la lista
print(len(nombres))

# agregar un elemento a la lista
nombres.append('lau')
print(nombres)

# insertar en un indice en especifico
nombres.insert(1, 'octavio')
print(nombres)

# remover un elemento
nombres.remove('octavio')
print(nombres)

# remover el ultimo valor agregado
nombres.pop()
print(nombres)

# eliminar un elemento en el incide
del nombres[0]
print(nombres)

# limpiar toda la lista
nombres.clear()
print(nombres)

# borrar la lista de la memoria
del nombres
print(nombres)

