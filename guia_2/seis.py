# ------------------------------------------------------------------------------------------------------------
# Escriba una función llamada find_indexes() que reciba como parámetro un string y un
# substring, y la salida sea un tuple que indique los índices de ocurrencia de ese substring en
# el primer string. Ejm, string = “tattattata” y el substring es “tt”, la salida debe ser (2, 5)
# ------------------------------------------------------------------------------------------------------------

import re


def find_indexes(inp, subs):
    return tuple([i.start() for i in re.finditer(subs, inp)])
