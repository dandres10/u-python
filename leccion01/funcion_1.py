#Funcion
def mi_funcion():
    print('saludos desde mi pc')

mi_funcion()

# funcion con parametros
def mi_funcion_params(nombre,apellido):
    print(f'{nombre} {apellido}')

mi_funcion_params('marlon', 'leon')

# funcion para sumar
def sumar(a: int, b: int):
    return a + b

resultado = sumar(5,9)
print(resultado)

# valores default

def restar(a: int, b: int = 5) -> int:
    return a - b

resultado = restar(2)
print(resultado)

#argumentos variables - esto es un tupla y es inmutable

def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres('juan', 'karla', 'maria')

#argumetos llave valor

def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE= 'Integrate develop', PK= 'primary key')


#argumento tipo lista

def desplegarNombres(nombres:list)-> None:
    for nombre in nombres:
        print(nombre)

nombres = ['juan', 'karla', 'maria']

desplegarNombres(nombres)


# funcion recursiva
def factorial(numero:int):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

print(f'Factorial {factorial(5)}')