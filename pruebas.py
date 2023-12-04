def imprimirLetras(palabra: str):
    for l in palabra:
        print(l)

def operacionesSobreListas(lista: list):
    valor = "asdasd"
    valor2 = "asdasd2"
    lista[0] = valor # Establecer valor a un elemento de la lista
    elemento = lista[0] # Obtener un valor de la lista
    lista.append(valor2)
    lista.remove(valor)
    posicion = lista.index(valor)
    cantidadDeApariciones = lista.count(valor) # Devuelve la cantidad de apariciones del elemento
    lista.insert(1, valor) # Inserta valor antes de la posicion 1

from queue import LifoQueue as Pila

def operacionesSobrePilas(pila: Pila):
    p = Pila ()
    p. put (1) # apilar
    elemento = p.get () # desapilar
    p.empty () # vacia ?

    while not p.empty():
        elem = pila.get()
        p.put(elem)
        res = res + 1