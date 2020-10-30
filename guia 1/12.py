serie = [0, 3, 0, 1, 1, 1, 4, 2, 2, 3, 2, 3, 4]
serie_filtered = list(set(sorted(serie)))
print(serie_filtered, "La longitud de la lista es", len(serie_filtered))