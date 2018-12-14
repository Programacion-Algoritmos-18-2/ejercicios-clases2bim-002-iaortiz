"""
    creación de clases
"""
# Creación de clase persona
class Persona(object):
    # Constructor de la clase
    def __init__(self, n, ape, ed, cod, not1, not2):
        """
        """
        # Atributos
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota_1 = int(not1)
        self.nota_2 = int(not2)

    # Métodos gets y sets de cada variable
    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_edad(self, n):
        self.edad = int(n)

    def obtener_edad(self):
        return self.edad
    
    def agregar_codigo(self, n):
        self.codigo = int(n)

    def obtener_codigo(self):
        return self.codigo
    
    def obtener_apellido(self):
        return self.apellido

    def agregar_nota_1(self, not1):
        self.nota_1 = int(not1)

    def obtener_nota_1(self):
        return self.nota_1

    def agregar_nota_2(self, not2):
        self.nota_2 = int(not2)

    def obtener_nota_2(self):
        return self.nota_2

    # Método str para presentar
    def __str__(self):
        return "%s - %s - %d - %d - %d - %d" % (self.nombre, self.apellido,\
                self.edad, self.codigo, self.nota_1, self.obtener_nota_2())

# Creación de clase Operaciones eprsona
class OperacionesPersona(object):
    # Constructor
    def __init__(self, listado):
        # Atributo
        self.listado_personas = listado

    # Metodo para obtener el promedio de nota 1
    def obtener_promedio_n1(self):
        # Variable acumuladora de nota 1
        suma = 0
        print("Promedio de estudiantes con la nota 1:")
        # Recorremos la lista de personas
        for n in self.listado_personas:
            # Sumamos la nota 1 de cada persona y la almacenamos en la variable suma
            suma = suma + n.obtener_nota_1()
        # OBtenemos el promedio de la suma para el número de estudiantes
        promedio = suma/len(self.listado_personas)
        return promedio

    def obtener_promedio_n2(self):
        # Variable acumuladora de nota 2
        suma = 0
        print("Promedio de estudiantes con la nota 2:")
        # Recorremos la lista de personas
        for n in self.listado_personas:
            # Sumamos la nota 1 de cada persona y la almacenamos en la variable suma
            suma = suma + n.obtener_nota_2()
        # OBtenemos el promedio de la suma para el número de estudiantes
        promedio = suma/len(self.listado_personas)
        return promedio
    # Método para obtener la lista de estudiantes con notas inferiores a 15 de la materia 1
    def obtener_lista_n1(self):
        cadena = ""
        print("Estudiantes con notas inferiores 15 de la materia 1:")
        # Recorremos la lista de personas
        for n in self.listado_personas:
            # Condicional para obtener las notas inferiores a 15 de la materia 1
            if (n.obtener_nota_1() < 15):
                # Almacenamos cada objeto obtenido en una cadena
                cadena = "%s %s %s - %d \n" %(cadena,n.obtener_nombre(), n.obtener_apellido(), n.obtener_nota_1())
        return cadena

    def obtener_lista_n2(self):
        cadena = ""
        print("Estudiantes con notas inferiores 15 de la materia 2:")
        # Recorremos la lista de personas
        for n in self.listado_personas:
            # Condicional para obtener las notas inferiores a 15 de la materia 2
            if (n.obtener_nota_2() < 15):
                # Almacenamos cada objeto obtenido en una cadena
                cadena = "%s %s %s - %d \n" %(cadena,n.obtener_nombre(), n.obtener_apellido(), n.obtener_nota_2())
        return cadena

    def obtener_listado_personas(self, letra_1, letra_2):
        cadena = ""
        print("Lista de personas que tienen en su nombre la letra R o J:")
        # Recorremos la lista de personas
        for n in self.listado_personas:
            # Condicional para que compare la primera letra del nombre con el parametro ingreesado
            if (n.obtener_nombre()[0] == letra_1 or n.obtener_nombre()[0] == letra_2):
                # Almacenamos cada objeto obtenido en una cadena
                cadena = "%s %s %s \n" %(cadena,n.obtener_nombre(), n.obtener_apellido())
        return cadena
