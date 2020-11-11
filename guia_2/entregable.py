from guia_2 import uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez, once, doce, trece, catorce, quince

print("""
""")

print("************************************")
print("\t\t\tEJERCICIO 1")
print("************************************\n")

uno.secuencia()

print("\n************************************")
print("\t\t\tEJERCICIO 2")
print("************************************\n")

lst = [1, 2, 3, 4, 5, 6]
n = int(input("Escriba un numero n desde donde se rotará la lista [1, 2, 3, 4, 5, 6]\n"))
print(dos.rotate(lst, n))

print("\n************************************")
print("\t\t\tEJERCICIO 3")
print("************************************\n")

my_list = [3, 4, 3, 6, 7, 2, 5, 42, 3, 56, 2]
print("La lista [3, 4, 3, 6, 7, 2, 5, 42, 3, 56, 2] sin duplicados es: {}".format(tres.delete_duplicates(my_list)))

print("\n************************************")
print("\t\t\tEJERCICIO 4")
print("************************************\n")

n = int(input("Ingrese un número\n"))
print(cuatro.print_tuple(n))

print("\n************************************")
print("\t\t\tEJERCICIO 5")
print("************************************\n")

print("La persona con mayor edad es:", cinco.max_age())

print("\n************************************")
print("\t\t\tEJERCICIO 6")
print("************************************\n")

st = input("Ingrese un string\n")
sst = input("Ingrese un substring\n")
print("Ocurrencias: ", seis.find_indexes(st, sst))

print("\n************************************")
print("\t\t\tEJERCICIO 7")
print("************************************\n")

st = input("Ingrese un string con caracteres numericos\n")
print(siete.sumNumbers(st))

print("\n************************************")
print("\t\t\tEJERCICIO 8")
print("************************************\n")

numero = int(input("Ingrese un numero\n"))
print("El numero {} es {}".format(numero, ocho.primeOrComposite(numero)))

print("\n************************************")
print("\t\t\tEJERCICIO 9")
print("************************************\n")

print("La lista [1, 2, 3, 4, 5] intercambiada es: ", nueve.interchange([1, 2, 3, 4, 5]))

print("\n************************************")
print("\t\t\tEJERCICIO 10")
print("************************************\n")

paises = ["China", "India", "Estados Unidos", "Indonesia"]
poblaciones = [1391, 1364, 327, 264]
print(diez.my_zip(paises, poblaciones))

print("\n************************************")
print("\t\t\tEJERCICIO 11")
print("************************************\n")

x = int(input("Ingrese un valor de x\n"))
print("e^{} = {}".format(x, once.e_func(x)))

print("\n************************************")
print("\t\t\tEJERCICIO 12")
print("************************************\n")

lst = [2, 3, 5, 5, 7, 8, 3, 4]
print("Primer valor de lista {} es {}:".format(lst, doce.primero(lst)))
print("Ultimo valor de lista {} es {}".format(lst, doce.ultimo(lst)))

print("\n************************************")
print("\t\t\tEJERCICIO 13")
print("************************************\n")

lista = [1, 2, 3, 4]
gen_obj = trece.generate_par_impar(lista)
print("[1, 2, 3, 4]")
trece.print_obj(gen_obj)

print("\n************************************")
print("\t\t\tEJERCICIO 14")
print("************************************\n")

entrada = ["alfredo", "luis", "margarita", "rosa"]
print("Nombres convertidos a mayusculas en la lista {} es: {}".format(entrada, catorce.salida(entrada)))

print("\n************************************")
print("\t\t\tEJERCICIO 15")
print("************************************\n")

entrada = [13, 20, 15, 18, 12, 19, 14, 17, 18]
print("Notas superiores a 17 en la lista {} es: {}".format(entrada, quince.salida(entrada)))
