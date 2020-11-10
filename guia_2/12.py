# ------------------------------------------------------------------------------------------------------------
# Escriba una función lambda que obtenga el primer y último valor de una lista
# ------------------------------------------------------------------------------------------------------------

lst = [2, 3, 5, 5, 7, 8, 3, 4]
primero = lambda x: x[0]
ultimo = lambda x: x[-1]

print("Primer valor:", primero(lst))
print("Ultimo valor:", ultimo(lst))
