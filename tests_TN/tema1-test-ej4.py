import inspect
import unittest
from solucion import cuenta_posiciones_por_nacion

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej4Test(unittest.TestCase):
    
    def test_unSoloAño(self): 
        res = cuenta_posiciones_por_nacion(
            ["arg", "aus", "nz", "sud"], 
            {2023:["nz", "sud", "arg", "aus"]})
        self.assertEqual(res, {"arg": [0,0,1,0], "aus": [0,0,0,1], "nz": [1,0,0,0], "sud": [0,1,0,0]}) 

    def test_dosAños(self): 
        res = cuenta_posiciones_por_nacion(
            ["arg", "aus", "nz", "sud"], 
            {2023:["nz", "sud", "arg", "aus"],
             2022:["nz", "sud", "aus", "arg"]})
        self.assertEqual(res, {"arg": [0,0,1,1], "aus": [0,0,1,1], "nz": [2,0,0,0], "sud": [0,2,0,0]}) 

    def test_tresAños(self): 
        res = cuenta_posiciones_por_nacion(
            ["arg", "aus", "nz", "sud"], 
            {2023:["nz", "sud", "arg", "aus"],
             2022:["nz", "sud", "aus", "arg"],
             2021:["nz", "sud", "aus", "arg"]})
        self.assertEqual(res, {"arg": [0,0,1,2], "aus": [0,0,2,1], "nz": [3,0,0,0], "sud": [0,3,0,0]}) 

    def test_posicionesIgualesANaciones(self): 
        res = cuenta_posiciones_por_nacion(
            ["arg", "aus", "nz", "sud"], 
            {2023:["arg", "aus", "nz", "sud"],
             2022:["arg", "aus", "nz", "sud"],
             2021:["arg", "aus", "nz", "sud"],
             2020:["arg", "aus", "nz", "sud"]})
        self.assertEqual(res, {"arg": [4,0,0,0], "aus": [0,4,0,0], "nz": [0,0,4,0], "sud": [0,0,0,4]}) 

    def test_nacionesEspejado(self): 
        res = cuenta_posiciones_por_nacion(
            ["arg", "aus", "nz", "sud"], 
            {2023:["sud", "nz", "aus", "arg"],
             2022:["sud", "nz", "aus", "arg"],
             2021:["sud", "nz", "aus", "arg"],
             2020:["sud", "nz", "aus", "arg"]})
        self.assertEqual(res, {"arg": [0,0,0,4], "aus": [0,0,4,0], "nz": [0,4,0,0], "sud": [4,0,0,0]}) 

    def test_resultadosRandom(self): 
        res = cuenta_posiciones_por_nacion(
            ["arg", "aus", "nz", "sud"], 
            {2023:["aus", "arg", "nz", "sud"],
             2022:["arg", "nz", "sud", "aus"],
             2021:["nz", "aus", "arg", "sud"],
             2020:["arg", "sud", "nz", "aus"]})
        self.assertEqual(res, {"arg": [2,1,1,0], "aus": [1,1,0,2], "nz": [1,1,2,0], "sud": [0,1,1,2]}) 

    def test_unAñoSinParticipar(self): 
        res = cuenta_posiciones_por_nacion(
            ["arg", "aus", "nz", "sud"], 
            {2023:["aus", "arg", "nz", "sud"],
             2022:["arg", "nz", "sud", "aus"],
             2021:["nz", "aus", "arg", "sud"],
             2019:["arg", "sud", "nz", "aus"]})
        self.assertEqual(res, {"arg": [2,1,1,0], "aus": [1,1,0,2], "nz": [1,1,2,0], "sud": [0,1,1,2]}) 

    def test_renuncio_michael_cheika(self):
        naciones= ["arg", "aus", "nz", "sud"]
        torneos= {2025:["arg","sud", "nz", "aus"],
                  2024:["arg","nz", "sud", "aus"]}

        res = cuenta_posiciones_por_nacion(naciones,torneos)
        self.assertEqual(res,{"arg": [2,0,0,0], "aus": [0,0,0,2], "nz": [0,1,1,0], "sud": [0,1,1,0]})

    def test_juega_solo(self):
        naciones = ["aus"]
        torneos = {2022:["aus"],2023:["aus"]}

        res = cuenta_posiciones_por_nacion(naciones,torneos)
        self.assertEqual(res, {"aus": [2]})

    def test_en_res_solo_hay_naciones_validas(self):
        naciones = ["arg", "aus", "nz", "sud"]
        torneos = {2023:["aus", "arg", "nz", "sud"],
             2021:["nz", "aus", "arg", "sud"],
             2019:["arg", "sud", "nz", "aus"]}
        resultado = cuenta_posiciones_por_nacion(naciones, torneos)
        for nacion in naciones:
            try:
                del resultado[nacion]
            except:
                self.assertFalse(True, "Faltan Naciones en el diccionario resultado")
        
        self.assertDictEqual(resultado,{})


if __name__ == '__main__':
    unittest.main(verbosity=2)

