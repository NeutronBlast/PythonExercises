# ------------------------------------------------------------------------------------------------------------
# Escriba un programa que acepte una serie de números, con varios repetidos. La salida debe
# indicar la serie sin repetidos, la longitud de la serie y ordenada en orden creciente. Ejemplo,
# si recibe en la entrada [0, 3, 0, 1, 1, 1, 4, 2, 2, 3, 2, 3, 4], La salida debe ser [0, 1, 2, 3, 4] e
# indicar que su longitud es 5.
# ------------------------------------------------------------------------------------------------------------

from guia_1 import ej_seis

serie = ej_seis.seis()
serie_int = [int(x) for x in serie]
serie_filtered = sorted(list(set(serie_int)))
print(serie_filtered, "La longitud de la lista es", len(serie_filtered))
