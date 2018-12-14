# Importaciones del paquete archivos
from paquete_archivos.miarchivo import MiArchivo
# Importacion del paquete modelo con la clase persona y operaciones persona
from paquete_modelo.mimodelo import Persona, OperacionesPersona
# Creacion de objeto tipo MiArchivo
m = MiArchivo()
# Creamos una variable donde obtenemos la informacion del archivo
lista = m.obtener_informacion()
# Quitamos el caracter " | " de la lista
lista = [l.split("|") for l in lista]
# Creamos una lista de personas
lista_personas =[]
# Recorremos  la lista
lista = lista[1:]
for d in lista:
    # Creamos un objeto de tipo persona que recibe los diferentes atributos de nuestro archivo
    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5])
    # Agregamos cada objeto en nuestra lista_persona
    lista_personas.append(p)

#Creamos un objeto de tipo operaciones donde usamos la lista_personas
operaciones = OperacionesPersona(lista_personas)
#Presentacion
print("\t-- EJERCICIO EN CLASE --\n")
# Presentación del promedio 1
print(operaciones.obtener_promedio_n1())
# Presentación del promedio 2
print(operaciones.obtener_promedio_n2())
# Presentación de la lista con notas inferiores a 15 de la materia 1
print(operaciones.obtener_lista_n1())
# Presentación de la lista con notas inferiores a 15 de la materia 2
print(operaciones.obtener_lista_n2())
# Presentación de la lista de estudiantes que su nombre empieza con R o J
print(operaciones.obtener_listado_personas("R","J"))


