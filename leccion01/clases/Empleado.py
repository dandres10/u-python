from clases.Persona import Persona
class Empleado(Persona):
    def __init__(self, nombre:str, apellido:str, edad: int, sueldo):
        super().__init__(nombre, apellido, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} Sueldo: {self.sueldo}'


empleado1 = Empleado('perry', 'loco', 67, 234567)

print(empleado1)