# ------------------------------------------------------------------------------------------------------------
# Escriba un programa que dado tres tuples con nombres, edades y ciudades. Como entrada
# solicite un numero n y en la salida indique el nombre, edad y ciudad correspondiente a es
# número. Ejemplo:
# nombres = (“Juan”, “Maria”, “Ricardo”, “Ana”, “Cecilia”)
# edades = (23, 21, 19, 25, 22)
# ciudades = (“Maracay”, “Valencia”, “Caracas”, “Barquisimeto”, “Barcelona”)
# n = 2, la salida será: Ricardo 19 Caracas
# ------------------------------------------------------------------------------------------------------------

def print_tuple(n):
    nombres = ("Juan", "Maria", "Ricardo", "Ana", "Cecilia")
    edades = (23, 21, 19, 25, 22)
    ciudades = ("Maracay", "Valencia", "Caracas", "Barquisimeto", "Barcelona")

    try:
        return nombres[n], edades[n], ciudades[n]
    except IndexError:
        return "Elemento no se encuentra en ese indice"