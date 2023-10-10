from polimorfismo.Empleado import Empleado
from polimorfismo.Gerente import Gerente


def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))

empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Perry', 6000, 'Sistemas')
imprimir_detalles(gerente)