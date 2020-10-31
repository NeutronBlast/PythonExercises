from guia_1 import ej_seis

serie = ej_seis.seis()
serie_int = [int(x) for x in serie]
serie_filtered = sorted(list(set(serie_int)))
print(serie_filtered, "La longitud de la lista es", len(serie_filtered))
