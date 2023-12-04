# Ejercicio 1
""" def pos_clientes(s: list, n: int) -> int:
    ref = -1
    suma = 0

    for cant in s:
        suma += cant
        if(cant > n or suma > n):
            return s.index(cant)

    return ref

print(pos_clientes([1, 2, 3, 4, 5, 6], 20)) """

# Ejercicio 2
""" def ordenar(s1: list) -> list:
    s2 = []

    for i in s1:
        if(i == "LLA"):
            s2.append(i)

    for i in s1:
        if(i == "UP"):
            s2.append(i)

    return s2

print(ordenar(['LLA', 'LLA', 'UP', 'LLA', 'UP', 'LLA', 'LLA', 'UP', 'UP', 'UP',])) """

# Ejercicio 3
# naciones= ["arg", "aus", "nz", "sud"]
# torneos= {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}}
# res = {"arg": [0,0,1,1], "aus": [0,0,1,1], "nz": [2,0,0,0], "sud": [0,2,0,0]}
""" def frecuencia_posicion_por_nacion(naciones: list, torneos: dict) -> dict:
    resultados = {}

    defaultResultadoTorneos = []

    for na in naciones:
        defaultResultadoTorneos.append(0)

    for na in naciones:

        for torneo in torneos.values():
            resultadosTorneo = defaultResultadoTorneos
            
            for i, res in enumerate(torneo):
                if(res == na):
                   resultadosTorneo[i] += 1
            resultados[na] = resultadosTorneo
                    

    return resultados

naciones = ["aus"]
torneos = {2022:["aus"],2023:["aus"]}
print(frecuencia_posicion_por_nacion(naciones,torneos)) """


# Ejercicio 4
def columnas_duplicadas(m: list) -> bool:
    n = int(len(m[0]) / 2)

    for listado in m:
        sum = 0
        primeros = []
        segundos = []

        while sum <= (len(listado) - 1):
            sum += 1
            if(sum <= n):
                primeros.append(listado[sum - 1])
            else:
                segundos.append(listado[sum - 1])

        if(primeros != segundos):
            return False
             
    return True


print(columnas_duplicadas([[1,2,10,2],[-5,6,-5,6]]))