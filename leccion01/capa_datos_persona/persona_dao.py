from capa_datos_persona.conexion import Conexion
from capa_datos_persona.cursor_del_pool import CursorDelPool
from capa_datos_persona.persona import Persona
from capa_datos_persona.logger_base import log


class PersonaDAO:
   _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
   _INSERTAR = 'INSERT INTO persona(nombre,apellido, email) VALUES(%s, %s, %s)'
   _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
   _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

   @classmethod
   def seleccionar(cls):
       with CursorDelPool() as cursor:
           cursor.execute(cls._SELECCIONAR)
           registros = cursor.fetchall()
           personas = []
           for registro in registros:
               persona = Persona(registro[0], registro[1], registro[2], registro[3])
               personas.append(persona)
           return personas

   @classmethod
   def insertar(cls, persona):
       with CursorDelPool() as cursor:
           valores = (persona.nombre, persona.apellido, persona.email)
           cursor.execute(cls._INSERTAR, valores)
           log.debug(f'Persona a insertada: {persona}')
       return cursor.rowcount

   @classmethod
   def actualizar(cls, persona):
       with CursorDelPool() as cursor:
           valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
           cursor.execute(cls._ACTUALIZAR, valores)
           log.debug(f'persona actualizada: {persona}')
           return cursor.rowcount

   @classmethod
   def eliminar(cls, persona):
       with CursorDelPool() as cursor:
           valores = (persona.id_persona,)
           cursor.execute(cls._ELIMINAR,valores)
           log.debug(f'Objeto eliminado {persona}')
           return cursor.rowcount




if __name__ == '__main__':

    # actualizar un registro
    # persona1 = Persona(9, 'act', 'act', 'act@gmail.com')
    # personas_actualizados = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas actualizadas: {personas_actualizados}')

    # Insertar un registro
    persona1 = Persona(nombre='Pedro', apellido='lopez', email='pedro@gmail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas insertadas {personas_insertadas}')

    # Elimiar un registro
    #persona1 = Persona(id_persona=9)
    #personas_eliminadas = PersonaDAO.eliminar(persona1)
    #log.debug(f'Personas eliminadas: {personas_eliminadas}')



    # seleccionar objetos
    personas = PersonaDAO.seleccionar()
    log.debug(len(personas))
    for persona in personas:
        log.debug(persona)