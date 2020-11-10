# ------------------------------------------------------------------------------------------------------------
# Escriba un programa que calcule el volumen de esfera de un radio r dado
# ------------------------------------------------------------------------------------------------------------

import math

radio = float(input("Escriba el radio\n"))
volume = math.pi * (radio ** 3) * 4/3
print("El volumen de la esfera {:.2f}".format(volume))
