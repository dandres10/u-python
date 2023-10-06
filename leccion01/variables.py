# se puede reasignar una variable "cambiar el tipo"
miVariable: str = 'hola desde python'
print(miVariable)

miVariable: int = 2
print(miVariable)

# operando memoria
x: int = 10
y: int = 2
z: int = x + y
print(z)

# saber la direccion en memoria donde esta almacenada la variable
print(id(z))

#ejercicio # 1
nombre: str = 'marlon'
celular: int = 3345567892
correo: str = 'marlon@gmail.com'

print(nombre)
print(celular)
print(correo)


#saber el tipo de dato esta almacenando mi variable
x: int = 10
print(type(x))
