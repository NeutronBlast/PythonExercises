# ------------------------------------------------------------------------------------------------------------
# Escriba un programa que acepte el nombre de un archivo desde la entrada e imprima la
# extensión de ese archivo. Ejemplo: ingresa abc.java, salida: java
# ------------------------------------------------------------------------------------------------------------

name = input("Escriba el nombre de un archivo\n")
print(name.split(".")[-1])
