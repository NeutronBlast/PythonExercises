# ------------------------------------------------------------------------------------------------------------
# Escriba un programa que solicite el nombre y el apellido (separadamente) y luego
# imprímalos en orden inverso.
# ------------------------------------------------------------------------------------------------------------

nombre = input("Escriba su nombre\n")
apellido = input("Escriba su apellido\n")
print("Su nombre es: {} {}".format(nombre[::-1], apellido[::-1]))
