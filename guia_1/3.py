# ------------------------------------------------------------------------------------------------------------
#
# Escriba un programa que acepte el radio de un círculo por el usuario y calcule y muestre por pantalla el área
#
# ------------------------------------------------------------------------------------------------------------


import math

radio = float(input("Escriba el radio\n"))
area = math.pi * (radio ** 2)
print("El area del circulo es {:.2f}".format(area))
