# ------------------------------------------------------------------------------------------------------------
# La función zip() de Python, toma dos o más objetos iterables y retorna una lista de tuples
# con un elemento de cada lista de entrada, de acuerdo a su índice. Ejemplo entrada, paises
# = ["China", "India", "Estados Unidos", "Indonesia"] ; poblaciones = [1391, 1364, 327, 264].
# La salida es [('China', 1391), ('India', 1364), ('Estados Unidos', 327), ('Indonesia', 264)].
# Escriba una función llamada my_zip(), que realice lo mismo (limítelo a sólo dos iterables).
# ------------------------------------------------------------------------------------------------------------

def my_zip(it1, it2):
    new_it = []
    if len(it1) != len(it2):
        return "No se puede hacer zip de dos iterables de diferente tamaño"
    else:
        for i in range(len(it1)):
            new_it.append((it1[i], it2[i]))
    return new_it


paises = ["China", "India", "Estados Unidos", "Indonesia"]
poblaciones = [1391, 1364, 327, 264]
print(my_zip(paises, poblaciones))
