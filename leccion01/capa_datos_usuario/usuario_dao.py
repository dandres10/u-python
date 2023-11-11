from capa_datos_usuario.usuario import Usuario
from capa_datos_persona.cursor_del_pool import CursorDelPool
from capa_datos_usuario.logger_base import log

class UsuarioDAO:
   _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
   _INSERTAR = 'INSERT INTO usuario(username,password) VALUES(%s, %s)'
   _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
   _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'
   @classmethod
   def seleccionar(cls):
       with CursorDelPool() as cursor:
           cursor.execute(cls._SELECCIONAR)
           registros = cursor.fetchall()
           usuarios = []
           for registro in registros:
               usuario = Usuario(registro[0], registro[1], registro[2])
               usuarios.append(usuario)
           return usuarios

   @classmethod
   def insertar(cls, usuario):
       with CursorDelPool() as cursor:
           valores = (usuario.username, usuario.password)
           cursor.execute(cls._INSERTAR, valores)
           log.debug(f'Usuario a insertado: {usuario}')
       return cursor.rowcount

   @classmethod
   def actualizar(cls, usuario):
       with CursorDelPool() as cursor:
           valores = (usuario.username, usuario.password, usuario.id_usuario)
           cursor.execute(cls._ACTUALIZAR, valores)
           log.debug(f'Usuario actualizado: {usuario}')
           return cursor.rowcount

   @classmethod
   def eliminar(cls, usuario):
       with CursorDelPool() as cursor:
           valores = (usuario.id_usuario,)
           cursor.execute(cls._ELIMINAR,valores)
           log.debug(f'Objeto eliminado {usuario}')
           return cursor.rowcount

if __name__ == '__main__':
    #insertar
    '''
    usuario1 = Usuario(username='pablito',password='guerra')
    usuarios_insertados = UsuarioDAO.insertar(usuario1)
    log.debug(f'Usuario insertado: {usuarios_insertados}')
    '''
    #listar
    usuarios_seleccionados = UsuarioDAO.seleccionar()
    for usuario in usuarios_seleccionados:
        log.debug(f'Usuario seleccionados: {usuario}')


