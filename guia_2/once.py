# ------------------------------------------------------------------------------------------------------------
# Escriba una función lambda que encuentre el valor de e^x dada por la expresión ((1 + (1/n)^n)^x para un valor
# de n = 1000
# ------------------------------------------------------------------------------------------------------------
import math

e_func = lambda x: (math.pow((math.pow(1+(1/1000), 1000)), x))
