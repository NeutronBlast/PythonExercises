# ------------------------------------------------------------------------------------------------------------
# Escriba una función filter, que aplicada a una lista con notas de alumnos, devuelva a la salida
# una lista con aquellas notas superiores a 17. Ejm: entrada [13, 20, 15, 18, 12, 19, 14, 17,18]
# la salida debe ser [20, 18, 19, 18]
# ------------------------------------------------------------------------------------------------------------

entrada = [13, 20, 15, 18, 12, 19, 14, 17, 18]
salida = list(filter(lambda item: item > 17, entrada))
print(salida)