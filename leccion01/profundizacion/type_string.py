from profundizacion.mi_clase import MiClase

import  math
# manejo de cadenas II

# concatenacion automatica en python
mensaje = 'hola'  'mundo'
print(mensaje)
#mirar que tiene la clase str
'''
help(str)
help(str.capitalize)
help(math)
'''

'''
help(MiClase)
print(MiClase.__doc__)
print(MiClase.__init__.__doc__)
print(MiClase.mi_metodo.__doc__)
'''

'''
Join
tupla = ('hola','como','estan')
lista = ['java','javascript']
print(' '.join(tupla))
print(' '.join(lista))
'''



'''
split

help(str.split)
cadena = '1.234.567.456'
print(cadena.split('.',2))
'''

nombre = 'Juan'
edad = 28
mensaje = 'Mi nombre es %s y tengo %d' %(nombre,edad)
print(mensaje)

#forma 1
persona = ('karla', 'gomez', 5000.00)
mensaje = 'Hola %s %s. Tu sueldo es %s' %persona
print(mensaje)

#forma 2
persona = ('karla', 'gomez', 5000.00)
mensaje = 'Hola %s %s. Tu sueldo es %s'
print(mensaje%persona)

#forma 1
nombre = 'Juan'
edad = 28
sueldo = 3000
mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre,edad,sueldo)
print(mensaje_con_formato)

#forma 2
nombre = 'Juan'
edad = 28
sueldo = 3000
mensaje_con_formato = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre,edad,sueldo)
print(mensaje_con_formato)

diccionario = {'nombre':'Leon'}
mensaje = 'Nombre {dic[nombre]}'.format(dic=diccionario)
print(mensaje)


# multiplicacion de str
resultado = 5 * 'hola'
print(resultado)

# multiplicacion de tuplas
resultado = 5 * ('hola',)
print(resultado)

# multiplicacion de listas
resultado = 10*[0]
print(resultado)

# replace
text = ' hola como estan'
print(text.replace(' ','-'))

#sin espacios
text = ' hola como estan'
print(text.strip())

#sin caracteres especificados
text = ' hola como estan+++'
print(text.strip('+').strip())













