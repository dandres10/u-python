from laboratorio.monitor import Monitor
from laboratorio.raton import Raton
from laboratorio.teclado import Teclado


class Computadora:
    contador_computadoras = 0
    def __init__(self, nombre, monitor, teclado,raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre} : {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''

if __name__ == '__main__':
    monitor1 = Monitor('HP', 23)
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP','USB')
    computadora1 = Computadora('ASUS',monitor1, teclado1, raton1)
    print(computadora1)

    monitor2 = Monitor('ACER', 23)
    teclado2 = Teclado('ACER', 'USB')
    raton2 = Raton('ACER', 'USB')
    computadora2 = Computadora('ASUS', monitor2, teclado2, raton2)
    print(computadora2)