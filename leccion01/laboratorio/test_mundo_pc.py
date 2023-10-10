from clases_1.Orden import Orden
from laboratorio.computadora import Computadora
from laboratorio.monitor import Monitor
from laboratorio.teclado import Teclado
from laboratorio.raton import Raton

monitor1 = Monitor('HP', 23)
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
computadora1 = Computadora('ASUS', monitor1, teclado1, raton1)


monitor2 = Monitor('ACER', 23)
teclado2 = Teclado('ACER', 'USB')
raton2 = Raton('ACER', 'USB')
computadora2 = Computadora('ASUS', monitor2, teclado2, raton2)


monitor3 = Monitor('ACER', 23)
teclado3 = Teclado('ACER', 'USB')
raton3 = Raton('ACER', 'USB')
computadora3 = Computadora('ASUS', monitor3, teclado3, raton3)


computadoras1 = [computadora1,computadora2]

orden1 = Orden(computadoras1)
orden1.agregar_producto(computadora3)

print(orden1)
