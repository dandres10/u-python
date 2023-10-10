from clases_1.Orden import Orden
from clases_1.Producto import Producto

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Medias', 50.00)
producto4 = Producto('Blusa', 40.00)
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
print(orden1)
print(f'Total del compra: {orden1.calcular_total()}' )
orden2 = Orden(productos2)
print(orden2)
print(f'Total del compra: {orden2.calcular_total()}' )