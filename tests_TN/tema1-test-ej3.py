import inspect
import unittest
from solucion import columnas_repetidas

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej3Test(unittest.TestCase):

    def test_unaFilaCumple(self): 
        res = columnas_repetidas([[1,2,1,2]])
        self.assertEqual(res, True)

    def test_unaFilaNoCumple(self): 
        res = columnas_repetidas([[1,2,3,2]])
        self.assertEqual(res, False)

    def test_filasParesCumple(self): 
        res = columnas_repetidas([[1,2,1,2],[-5,6,-5,6]])
        self.assertEqual(res, True)

    def test_filasImparesCumple(self): 
        res = columnas_repetidas([[1,2,1,2],[-5,6,-5,6],[0,1,0,1]])
        self.assertEqual(res, True)

    def test_filasParesNoCumple(self): 
        res = columnas_repetidas([[1,2,10,2],[-5,6,-5,6]])
        self.assertEqual(res, False)

    def test_filasImparesNoCumple(self): 
        res = columnas_repetidas([[1,2,1,4],[-5,2,-5,6],[0,1,1,1]])
        self.assertEqual(res, False)

    def test_todosIguales0(self): 
        res = columnas_repetidas([[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]])
        self.assertEqual(res, True)

    def test_todosIgualesPositivos(self): 
        res = columnas_repetidas([[0,0,0,0,0,0], [1,1,1,1,1,1], [2,2,2,2,2,2]])
        self.assertEqual(res, True)

    def test_todosIgualesNegativos(self): 
        res = columnas_repetidas([[0,0,0,0,0,0], [-1,-1,-1,-1,-1,-1], [-2,-2,-2,-2,-2,-2]])
        self.assertEqual(res, True)

    def test_espejado(self): 
        res = columnas_repetidas([[1,2,3,3,2,1]])
        self.assertEqual(res, False)

    def test_espejado2(self): 
        res = columnas_repetidas([[1,2,3,3,2,1], [1,2,3,3,2,1]])
        self.assertEqual(res, False)

    def test_espejado3(self): 
        res = columnas_repetidas([[1,2,3,3,2,1], [1,2,3,3,2,1], [1,2,3,3,2,1]])
        self.assertEqual(res, False)

    def test_espejado4(self): 
        res = columnas_repetidas([[1,2,3,3,2,1], [1,2,3,3,2,1], [1,2,3,3,2,1], [1,2,3,3,2,1]])
        self.assertEqual(res, False)

    def test_algunasFilasCumplenYOtrasNo(self): 
        res = columnas_repetidas([[0,0,0,0,0,0], [1,2,3,3,2,1], [1,2,1,1,2,1]])
        self.assertEqual(res, False)

    def test_cumpleUnaSola1(self): 
        res = columnas_repetidas([[0,0,0,2,0,0], [1,2,3,3,2,1], [1,2,1,1,2,1]])
        self.assertEqual(res, False)

    def test_cumpleUnaSola2(self): 
        res = columnas_repetidas([[0,0,0,2,0,0], [1,2,1,1,2,1], [1,2,3,3,2,1]])
        self.assertEqual(res, False)

    def test_cumpleUnaSola3(self): 
        res = columnas_repetidas([[1,2,1,1,2,1], [0,0,0,2,0,0], [1,2,3,3,2,1]])
        self.assertEqual(res, False)

    def test_dosXUnoCumple(self): 
        res = columnas_repetidas([[1,1]])
        self.assertEqual(res, True)

    def test_dosXDosCumple(self): 
        res = columnas_repetidas([[1,1],[1,1]])
        self.assertEqual(res, True)

    def test_dosXUnoNoCumple(self): 
        res = columnas_repetidas([[1,-1]])
        self.assertEqual(res, False)

    def test_dosXDosNoCumple(self): 
        res = columnas_repetidas([[1,1],[3,1]])
        self.assertEqual(res, False)

    def test_dos_columnas_true(self):
        res = columnas_repetidas([[1,1],[3,3],[2,2],[-1,-1]])
        self.assertTrue(res)

    def test_dos_columnas_false(self):
        res = columnas_repetidas([[1,2],[3,3],[2,2],[-1,-1]])
        self.assertFalse(res)
    
    def test_filas_iguales_no_columnas(self): 
        # doy vuelta la matriz y comparo como si fuesen filas, no columnas
        res = columnas_repetidas([[6,0,-5,1],[-5,1,6,2],[6,0,-5,1],[-5,1,6,2]])
        self.assertFalse(res)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)

