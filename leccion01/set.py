#set
planetas = {'marte', 'jupiter', 'venus'}
print(planetas)

#validar si un elemento esta dentro del set
print('marte' in planetas)

#agregar un elemento
planetas.add('tierra')
print(planetas)

#eliminar elementos
planetas.remove('tierra')
planetas.discard('tierra')
print(planetas)

#limpiar
planetas.clear()
print(planetas)