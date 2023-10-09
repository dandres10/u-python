
# clase sin constructor
#class Persona:
    #def __init__(self):
        #self.nombre = 'Juan'
        #self.apellido = 'Leon'
        #self.edad = 28


#persona1 = Persona()

#print(persona1.nombre)


# clase con constructor
# self.__nombre el guion bajo significa privado, no se puede modificar afuera de la clase
class Persona:
    def __init__(self, nombre:str, apellido:str, edad: int):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    #get
    @property
    def nombre(self):
        return self._nombre

    #set
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # get
    @property
    def apellido(self):
        return self._apellido

   # set
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    # get

    @property
    def edad(self):
        return self._edad

    # set
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Animal: {self._nombre}, {self._apellido}, {self._edad}')

    def __str__(self):
        return f'Persona: {self._nombre}, {self._apellido}, {self._edad}'
