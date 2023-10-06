#diccionarios
diccionario = {
    'IDE': 'integrate development enviroment',
    'OOP': 'programacion orientada a objetos',
    'DBMS': 'database management system'
}

print(diccionario)

#largo
print(len(diccionario))

#acceder a un elemeto por medio de una key
print(diccionario['IDE'])

#otra forma de recuperar un elemento
print(diccionario.get('OOP'))

#modificar un elemento
diccionario['IDE'] = 'entorno de desarrollo'
print(diccionario)

#recorrer elementos
for termino, valor in diccionario.items():
    print(termino, valor)

#recorrer elementos o solo retornar las keys
for key in diccionario.keys():
    print(key)

#recorrer elementos o solo retornar las values
for value in diccionario.values():
    print(value)

#find
print('IDE' in diccionario)

#agregar un elemento
diccionario['PK'] = 'primary key of a database'
print(diccionario)

#remover
diccionario.pop('PK')
print(diccionario)

#limpiar
diccionario.clear()
print(diccionario)

