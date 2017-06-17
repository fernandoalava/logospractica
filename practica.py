class Persona(object):

    def __init__(self, nombre):
        if type(nombre) == str:
            self.nombre = nombre
        else:
            print ("error")

    def imprimir(self):
        print (self.nombre)


class Trabajador(Persona):
    def __init__(self, nombre, edad):
        super(Trabajador, self)
        self.nombre = nombre
        self.edad = edad

    def imprimir(self, saludo):
        """
            Imprime un nombre
        """
        print (saludo, self.nombre)

    def _test(self):
        print (1)

    @staticmethod
    def imprimir_saludo(nombre):
        print ("Hola", nombre)


persona1 = Persona("Pablo")
persona2 = Persona("Alvaro")
persona3 = Trabajador("Juan", 33)

print (persona3._test())

empleados = [persona1, persona2, persona3]
lista1 = [i for i in empleados if i.nombre == "Juan"]

Trabajador.imprimir_saludo("Juanito")

print (lista1)
