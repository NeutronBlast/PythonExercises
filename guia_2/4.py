# ------------------------------------------------------------------------------------------------------------
# Escriba un programa que dado tres tuples con nombres, edades y ciudades. Como entrada
# solicite un numero n y en la salida indique el nombre, edad y ciudad correspondiente a es
# número. Ejemplo:
# nombres = (“Juan”, “Maria”, “Ricardo”, “Ana”, “Cecilia”)
# edades = (23, 21, 19, 25, 22)
# ciudades = (“Maracay”, “Valencia”, “Caracas”, “Barquisimeto”, “Barcelona”)
# n = 2, la salida será: Ricardo 19 Caracas
# ------------------------------------------------------------------------------------------------------------

nombres = ("Juan", "Maria", "Ricardo", "Ana", "Cecilia")
edades = (23, 21, 19, 25, 22)
ciudades = ("Maracay", "Valencia", "Caracas", "Barquisimeto", "Barcelona")

n = int(input("Ingrese un número\n"))
try:
    print(nombres[n], edades[n], ciudades[n])
except IndexError:
    print("Elemento no se encuentra en ese indice")