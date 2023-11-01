import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password= 'marlon',
    host= 'localhost',
    port= '5432',
    database= 'test_db'
)
# sentencia plana --------------------------------------
#try:
#    with conexion:
#      with conexion.cursor() as cursor:
#        sentencia = 'SELECT * FROM persona'
#        cursor.execute(sentencia)
#        registros = cursor.fetchall()
#except Exception as e:
#    print(f'Ocurrio un error: {e}')
#finally:
#    conexion.close()

#print(registros)

# sentencia con parametro -------------------------------
#try:
#    with conexion:
#      with conexion.cursor() as cursor:
#        sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
#        id_persona = 1
#        cursor.execute(sentencia, (id_persona,))
#        registros = cursor.fetchall()
#except Exception as e:
#    print(f'Ocurrio un error: {e}')
#finally:
#    conexion.close()


# sentencia para retornar un solo registro --------------------------------------------
#try:
#    with conexion:
#      with conexion.cursor() as cursor:
#        sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
#        id_persona = 1
#        cursor.execute(sentencia, (id_persona,))
#        registros = cursor.fetchone()
#except Exception as e:
#    print(f'Ocurrio un error: {e}')
#finally:
#    conexion.close()

# sentencia para retornar varios --------------------------------------------
#try:
#    with conexion:
#      with conexion.cursor() as cursor:
#        sentencia = 'SELECT * FROM persona WHERE id_persona IN (1,2)'
#        cursor.execute(sentencia)
#        registros = cursor.fetchall()
#except Exception as e:
#    print(f'Ocurrio un error: {e}')
#finally:
#    conexion.close()

# sentencia para retornar varios mejora --------------------------------------------
#try:
#    with conexion:
#      with conexion.cursor() as cursor:
#        llaves_primarias = ((1,2),)
#        sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
#        cursor.execute(sentencia, llaves_primarias)
#        registros = cursor.fetchall()
#except Exception as e:
#    print(f'Ocurrio un error: {e}')
#finally:
#    conexion.close()

#print(registros)



# sentencia para insertar --------------------------------------------
'''
try:
    with conexion:
      with conexion.cursor() as cursor:
        sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s, %s, %s)'
        valores = ('alenandra', 'leon', 'alejandra@gmail.com')
        cursor.execute(sentencia, valores)
        #conexion.commit()
        registros_insertados = cursor.rowcount
        print(f'registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

'''


# sentencia para insertar varios registros --------------------------------------------

'''
try:
    with conexion:
      with conexion.cursor() as cursor:
        sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s, %s, %s)'
        valores = (('perry', 'leon', 'perry@gmail.com'),
                   ('lau', 'pi', 'lau@gmail.com'))
        cursor.executemany(sentencia, valores)
        #conexion.commit()
        registros_insertados = cursor.rowcount
        print(f'registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
'''

# actualizar uno a las vez  --------------------------------------------
'''
try:
    with conexion:
      with conexion.cursor() as cursor:
        sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
        valores = ('act', 'act', 'act', 1)
        cursor.execute(sentencia, valores)
        #conexion.commit()
        registros_insertados = cursor.rowcount
        print(f'registros actualizados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
'''


# actualizar dos a las vez  --------------------------------------------
'''
try:
    with conexion:
      with conexion.cursor() as cursor:
        sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
        valores = (('uno', 'uno', 'uno', 1),('dos', 'dos', 'dos', 2))
        cursor.executemany(sentencia, valores)
        #conexion.commit()
        registros_insertados = cursor.rowcount
        print(f'registros actualizados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
'''


# eliminar uno a las vez  --------------------------------------------
'''
try:
    with conexion:
      with conexion.cursor() as cursor:
        sentencia = 'DELETE FROM persona WHERE id_persona=%s'
        valores = (1,)
        cursor.execute(sentencia, valores)
        #conexion.commit()
        registros_eliminados = cursor.rowcount
        print(f'registros eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
'''


# eliminar varios registros  --------------------------------------------

try:
    with conexion:
      with conexion.cursor() as cursor:
        sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
        valores = ((2,3),)
        cursor.execute(sentencia, valores)
        #conexion.commit()
        registros_eliminados = cursor.rowcount
        print(f'registros eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()