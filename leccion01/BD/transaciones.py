import psycopg2 as bd

conexion = bd.connect(
    user='postgres',
    password= 'marlon',
    host= 'localhost',
    port= '5432',
    database= 'test_db'
)


try:
 conexion.autocommit = False
 cursor = conexion.cursor()
 sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
 values = ('maria','esperanza','esperanza@gmail.com')
 cursor.execute(sentencia, values)
 conexion.commit()
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo rollback: {e}')
finally:
    conexion.close()