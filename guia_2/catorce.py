# ------------------------------------------------------------------------------------------------------------
# Escriba una función map, para que dada una lista con nombres, la salida sea la lista con los
# nombres en Mayúsculas. Ejm: entrada [“alfredo”, “luis”, “margarita”, “rosa”], salida
# [“ALFREDO”, “LUIS”, “MARGARITA”, “ROSA”]
# ------------------------------------------------------------------------------------------------------------

salida = lambda entrada: list(map(lambda item: item.upper(), entrada))