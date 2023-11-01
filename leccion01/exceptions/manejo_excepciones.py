from NumerosIgualesException import NumerosIgualesException
# ejemplo de manejo de exceptions
resultado = None
a = 10
b = 0


try:
    resultado = a/b
except Exception as e:
    print(f'ocurrio un error: {e}')
else:
    print(f'no se encontro ningun error')
finally:
    print('Ejecucion del metodo finally correctamente este metodo siempre se ejecuta al final')


print(resultado)

# ejemplo de manejo de exceptions personalizadas
a = 10
b = 10
if a == b:
    try:
       raise NumerosIgualesException('Numeros iguales esto no es permitido')
    except Exception as e:
        print(f'ocurrio un error exception personalizada: {e}')

