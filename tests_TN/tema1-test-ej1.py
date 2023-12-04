import inspect
import unittest
from solucion import acomodar

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej1Test(unittest.TestCase):


    def test_noHayListas(self): # Testea que la lista devuelta tenga 0 o mas elementos
        res = acomodar([])
        self.assertEqual(len(res), 0)

    def test_listasIgualCantidad(self): # Testea una lista con la misma cantidad de boletas por lista
        res = acomodar(['UP', 'LLA', 'UP', 'LLA', 'UP', 'LLA', 'UP', 'LLA', 'UP', 'LLA'])
        self.assertEqual(res, ['UP', 'UP', 'UP', 'UP', 'UP', 'LLA', 'LLA', 'LLA', 'LLA', 'LLA'])

    def test_masLLAQueUP(self): # Testea una lista con más de LLA que de UP
        res = acomodar(['LLA', 'UP', 'LLA', 'UP', 'LLA', 'UP', 'LLA', 'UP', 'LLA'])
        self.assertEqual(res, ['UP', 'UP', 'UP', 'UP', 'LLA', 'LLA', 'LLA', 'LLA', 'LLA'])

    def test_masUPQueLLA(self): # Testea una lista con más de UP que de LLA
        res = acomodar(['UP', 'UP', 'LLA', 'UP', 'LLA', 'UP', 'LLA', 'UP', 'LLA'])
        self.assertEqual(res, ['UP', 'UP', 'UP', 'UP', 'UP', 'LLA', 'LLA', 'LLA', 'LLA'])

    def test_soloLLA(self): # Testea una lista con solo boletas de LLA
        res = acomodar(['LLA', 'LLA', 'LLA', 'LLA', 'LLA'])
        self.assertEqual(res, ['LLA', 'LLA', 'LLA', 'LLA', 'LLA'])

    def test_soloUnaDeLLA(self): # Testea una lista con solo una boleta de LLA
        res = acomodar(['LLA'])
        self.assertEqual(res, ['LLA'])

    def test_soloUP(self): # Testea una lista con solo boletas de UP
        res = acomodar(['UP', 'UP', 'UP', 'UP', 'UP'])
        self.assertEqual(res, ['UP', 'UP', 'UP', 'UP', 'UP'])

    def test_soloUnaDeUP(self): # Testea una lista con solo una boletas de UP
        res = acomodar(['UP'])
        self.assertEqual(res, ['UP'])

    def test_estaOrdenada(self): # Testea una lista ya ordenada
        res = acomodar(['UP', 'UP', 'UP', 'UP', 'UP', 'LLA', 'LLA', 'LLA', 'LLA', 'LLA'])
        self.assertEqual(res, ['UP', 'UP', 'UP', 'UP', 'UP', 'LLA', 'LLA', 'LLA', 'LLA', 'LLA'])

    def test_estaOrdenadaAlReves(self): # Testea una lista que tiene primero todas boletas de LLA y dsp todas de UP
        res = acomodar(['LLA', 'LLA', 'LLA', 'LLA', 'LLA', 'UP', 'UP', 'UP', 'UP', 'UP'])
        self.assertEqual(res, ['UP', 'UP', 'UP', 'UP', 'UP', 'LLA', 'LLA', 'LLA', 'LLA', 'LLA'])

    def test_estaOrdenadaSalvoLaPrimera(self): # Testea una lista que tiene todo ordenado salvo la primer boleta
        res = acomodar(['UP', 'UP', 'UP', 'UP', 'LLA', 'LLA', 'LLA', 'UP', 'LLA', 'LLA'])
        self.assertEqual(res, ['UP', 'UP', 'UP', 'UP', 'UP', 'LLA', 'LLA', 'LLA', 'LLA', 'LLA'])

    def test_estaOrdenadaSalvoLaUltima(self): # Testea una lista que tiene todo ordenado salvo la ultima boleta
        res = acomodar(['LLA', 'UP', 'UP', 'UP', 'UP', 'UP', 'LLA', 'LLA', 'LLA', 'LLA'])
        self.assertEqual(res, ['UP', 'UP', 'UP', 'UP', 'UP', 'LLA', 'LLA', 'LLA', 'LLA', 'LLA'])

    def test_random1(self): # Testea una lista random
        res = acomodar(['UP', 'UP', 'LLA', 'LLA', 'LLA', 'UP', 'LLA', 'UP', 'UP', 'LLA'])
        self.assertEqual(res, ['UP', 'UP', 'UP', 'UP', 'UP', 'LLA', 'LLA', 'LLA', 'LLA', 'LLA'])

    def test_random2(self): # Testea una lista random
        res = acomodar(['LLA', 'UP', 'UP', 'UP', 'UP','LLA', 'LLA', 'UP', 'LLA', 'LLA'])
        self.assertEqual(res, ['UP', 'UP', 'UP', 'UP', 'UP', 'LLA', 'LLA', 'LLA', 'LLA', 'LLA'])

    def test_random3(self): # Testea una lista random
        res = acomodar(['LLA', 'LLA', 'UP', 'LLA', 'UP', 'UP', 'LLA', 'UP', 'LLA', 'UP'])
        self.assertEqual(res, ['UP', 'UP', 'UP', 'UP', 'UP', 'LLA', 'LLA', 'LLA', 'LLA', 'LLA'])

    def test_random4(self): # Testea una lista random
        res = acomodar(['UP', 'UP', 'LLA', 'UP', 'LLA', 'UP', 'UP', 'LLA', 'LLA', 'LLA',])
        self.assertEqual(res, ['UP', 'UP', 'UP', 'UP', 'UP', 'LLA', 'LLA', 'LLA', 'LLA', 'LLA'])

    def test_elementos_legales(self):
        l = ["UP","LLA","UP","LLA","UP",]
        res = acomodar(l)
        up = res.count("UP")
        lla = res.count("LLA")
        for _ in range(up):
            res.remove("UP")
        for _ in range(lla):
            res.remove("LLA")
        self.assertEqual([], res)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)

