def imprimirLetras(palabra: str):
    for l in palabra:
        print(l)

# imprimirLetras("palabra")

def pertenece(sec: list, el: int):
    for e in sec:
        if(e == el):
            return True
        
    return False

# print(pertenece([1,2,3,4,5], 7))

def divideATodos(sec: list, ref: int):
    for e in sec:
        if(e % ref != 0):
            return False
        
    return True

# print(divideATodos([10, 20, 30, 41], 5))

def sumaTotal(sec: list):
    sum = 0
    for e in sec:
        sum += e

    return sum

# print(sumaTotal([1,2,3,4,5,6,7,8,9,10]))

def ordenados(sec: list):
    for i in range(len(sec) - 1):
        if not sec[i] < sec[i + 1]:
            return False
    return True

# print(ordenados([1,2,3,4]))

def longitudMayorQueSiete(sec: list):
    for p in sec:
        if(len(p) > 7):
            return True
    return False

# print(longitudMayorQueSiete(["palabra", "palabra"]))

def pruebaPop(palabra: str):
    lista = list(palabra)
    
    vieja_palabra = []
    for l in lista:
        vieja_palabra.append(l)

    nueva_palabra = []
    for _ in range(len(lista)):
        ultimo = lista.pop()
        nueva_palabra.append(ultimo)
    
    return vieja_palabra == nueva_palabra

# print(pruebaPop("matias"))

def analizarFortaleza(pw: str):
    