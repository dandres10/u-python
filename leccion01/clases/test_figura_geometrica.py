from clases.Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5,'negro')

print(cuadrado1.alto)
print(cuadrado1.ancho)
print(cuadrado1.color)
print(cuadrado1.calcular_area())

print(Cuadrado.mro())