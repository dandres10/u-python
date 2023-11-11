#tipos numericos
valor = 0
resultado = bool(valor)
print(f'resultado {resultado}')
valor = 45
resultado = bool(valor)
print(f'resultado {resultado}')

#tipo string
valor = ''
resultado = bool(valor)
print(f'resultado {resultado}')
valor = 'hola'
resultado = bool(valor)
print(f'resultado {resultado}')

#tipo colecciones
valor = []
resultado = bool(valor)
print(f'resultado {resultado}')
valor = [2,3,45]
resultado = bool(valor)
print(f'resultado {resultado}')

#tipo tupla
valor = ()
resultado = bool(valor)
print(f'resultado {resultado}')
valor = (2,3,45)
resultado = bool(valor)
print(f'resultado {resultado}')


#tipo diccionario
valor = {}
resultado = bool(valor)
print(f'resultado {resultado}')
valor = {'nombre': 'pedro', 'apellido':'perez'}
resultado = bool(valor)
print(f'resultado {resultado}')

#estructuras de control
if '':
    print('regreso verdadero')
else:
    print('regreso falso')
