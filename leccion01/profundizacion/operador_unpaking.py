numeros = [1,2,3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')

def sumar(a,b,c):
    print(f'resultado suma: {a + b + c}')


sumar(*numeros)

#extraer algunas partes
mi_lista = [1,2,3,4,5,6]
a,*b,c,d = mi_lista
print(a,b,c,d)

# unir listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1, lista2]
print(lista3)
lista3 = [*lista1, *lista2]
print(lista3)

#unir diccionarios
dic1 = {'A':1, 'B':2, 'C':3 }
dic2 = {'D':4, 'E':5 }
dic3 = {**dic1, **dic2}
print(dic3)


lista = [*'HolaMundo']
print(lista)