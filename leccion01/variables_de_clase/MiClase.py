class MiClase:
    variable_clase = 'Valor de variable'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_statico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_statico()



ob1 = MiClase('variable de instalcia')
ob1.metodo_instancia()
