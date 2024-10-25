if __name__ == '__main__':
    #tipos de datos basicos
    entero = 42 #int
    decimal = 3.14 #float
    complejo = 2 + 3j   #complex
    booleano = True  #bool
    cadena = 'Hola, Phyton!'   #str
    binario = bytes([50, 100, 150])  #bytes

    print("Tipos basicos: ")
    print("entero: ", entero)
    print("decimal: ", decimal)
    print("complejo:  ", complejo)
    print("booleano: ", booleano)
    print("cadena: ", cadena)
    print("bytes: ", binario, "\n")

    #estructuras de datos avanzada
    lista = [1, 2, 3, "cuatro"]  #list
    tupla = (5, 6, 7, "ocho")  #tuple
    conjunto = {9, 10, "once", "doce"} #set
    diccionario = {"clave1": "valor1", "clave2": 20} #

    print("ESTRUCTURAS AVANZADAS: ")
    print("lista: ", lista)
    print("tupla", tupla)
    print("conjunto: ", conjunto)
    print("diccionario: ", diccionario, "\n")

    #otros tipos especiales
    nulo = None   #NoneType
    rango = range(3)#range (equivale a [0,1,2,3,4,5,6,7,8,9]

print("Tipos especiales: ")
print("Nulo: ", nulo)
print("rango: ", list(rango))#convertimos a lista

#ejemplo de iteracion con el tipo range
print("\nIteracion sobre el rango: ")

#esta es la manera mas corta de recorrer un rango
for numero in rango:
    print(numero)
