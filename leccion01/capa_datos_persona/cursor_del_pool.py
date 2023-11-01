from capa_datos_persona.logger_base import log
from capa_datos_persona.conexion import Conexion


class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    # este es bloque with lo que se va a ejecutar que se esta sobre escribiendo
    def __enter__(self):
        log.debug(f'Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('Se ejecuta metodo exit')
        if valor_excepcion:
            self._conexion.rollback()
            log.debug(f'Ocurrio una excepcion, se hace rollback: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')
        else:
            self._conexion.commit()
            log.debug(f'Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
     with CursorDelPool() as cursor:
         log.debug('Dentro del bloque with')
         cursor.execute('SELECT * FROM persona')
         log.debug(cursor.fetchall())


