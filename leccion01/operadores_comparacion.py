a = 4
b = 2

#igual
resultado = a == b
print(f'Resultado == : {resultado}')

#distinto
resultado = a != b
print(f'Resultado != : {resultado}')

#mayor que
resultado = a > b
print(f'Resultado > : {resultado}')


#menor que
resultado = a < b
print(f'Resultado < : {resultado}')


#mayor o igual
resultado = a >= b
print(f'Resultado >= : {resultado}')

#menor o igual
resultado = a <= b
print(f'Resultado <= : {resultado}')


a = True
b = True

#and
resultado = a and b
print(f'Resultado and : {resultado}')

#or
resultado = a or b
print(f'Resultado or : {resultado}')

#not invertir el sentido del resultado
resultado = not b
print(f'Resultado not : {resultado}')

edad = 30

# es un and aplicar un rango en este caso la edad entre 20 y 30
if (20 <= edad <= 30):
    print(f'Resultado edad : esta dentro del rango')
else:
    print(f'Resultado edad : esta fuera del rango')




