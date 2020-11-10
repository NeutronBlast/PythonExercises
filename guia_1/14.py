# ------------------------------------------------------------------------------------------------------------
# Escriba un programa que dada un dirección IPv4 válida retorne un versión deformada de
# esa dirección. Una versión de una dirección IP deformada reemplaza cada “.” con “[ . ]”.
# Ejemplo, entrada: dirección “255.100.50.0”, salida: “255[ . ]100[ . ]50[ . ]0”
# ------------------------------------------------------------------------------------------------------------

ip = "255.100.50.0"
print(ip.replace(".", "[ . ]"))
