import inspect
import unittest
from solucion import pos_umbral

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej2Test(unittest.TestCase):

    def test_noEntroNadieUmbral1(self):  
        res = pos_umbral([], 1)
        self.assertEqual(res, -1)

    def test_noEntroNadieUmbral0(self):  
        res = pos_umbral([], 0)
        self.assertEqual(res, -1)

    def test_noEntroNadieUmbral10(self):  
        res = pos_umbral([], 10)
        self.assertEqual(res, -1)

    def test_todosNegativosUmbral0(self):  
        res = pos_umbral([-1, -2, -3, -4, -8, -2], 10)
        self.assertEqual(res, -1)

    def test_todosNegativosUmbralMayorA0(self):  
        res = pos_umbral([-1, -2, -3, -4, -8, -2], 10)
        self.assertEqual(res, -1)

    def test_todosNegativosMenosUnoYNoLlega(self):  
        res = pos_umbral([-1, -2, -3, -4, 10, -2], 10)
        self.assertEqual(res, -1)

    def test_todosNegativosMenosUnoYNoLlega2(self):  
        res = pos_umbral([10, -2, -3, -4, -8, -2], 10)
        self.assertEqual(res, -1)

    def test_todosNegativosMenosUnoYNoLlega3(self):  
        res = pos_umbral([-1, -2, -3, -4, -8, 10], 10)
        self.assertEqual(res, -1)

    def test_noLlegaAlUmbral(self):  
        res = pos_umbral([1, -2, 3, 4], 11)
        self.assertEqual(res, -1)

    def test_todosPositivosYNoLlegaAlUmbral(self):  
        res = pos_umbral([1, 2, 3, 4], 10)
        self.assertEqual(res, -1)

    def test_llegaAlUmbralAlComienzo(self):  
        res = pos_umbral([11, 2, 4, 4], 10)
        self.assertEqual(res, 0)

    def test_llegaAlUmbralAlComienzo2(self):  
        res = pos_umbral([10, 11, 4, 4, 2], 10)
        self.assertEqual(res, 1)

    def test_llegaAlUmbralAlComienzo3(self):  
        res = pos_umbral([-11, 11, 4, 4, 2], 10)
        self.assertEqual(res, 1)

    def test_llegaAlUmbralAlFinal(self):  
        res = pos_umbral([-11, 2, 3, 5, -5, 1, 1], 11)
        self.assertEqual(res, 6)

    def test_TodosPositivosYLlegaAlUmbralAlFinal(self):  
        res = pos_umbral([1, 2, 3, 4, 5, 6], 20)
        self.assertEqual(res, 5)

    def test_llegaAlUmbralAlMedio(self):  
        res = pos_umbral([-12, 9, 1, 10, -32], 10)
        self.assertEqual(res, 3)

    def test_TodosPositivosYLlegaAlUmbralAlMedio(self):  
        res = pos_umbral([1, 1, 0, 0, 3, 4, 2, 1], 3)
        self.assertEqual(res, 4)

    def test_positivoYNegativoYLlegaAlUmbral(self):  
        res = pos_umbral([0, 0, 1, -1, 2, -2, -3, 3, -4, 4, 10], 15)
        self.assertEqual(res, 10)

    def test_todos_negativos(self):
        res = pos_umbral([-5,-3,-7], 2)
        self.assertEqual(res,-1)

    def test_todos_negativos_umbral_cero(self):
        res = pos_umbral([-5,-3,-7], 0)
        self.assertEqual(res, -1)

    def test_todos_negativos_algun_cero(self):
        res = pos_umbral([-5,-3, 0,-7], 2)
        self.assertEqual(res,-1)
    
    def test_todos_negativos_algun_cero_umbral_cero(self):
        res = pos_umbral([-5,-3, 0,-7], 0)
        self.assertEqual(res, -1)

    def test_umbral_cero(self):
        res = pos_umbral([0,2,3], 0)
        self.assertEqual(res,1)

    def test_umbral_se_supera(self):
        res = pos_umbral([-1,2,0,5], 6)
        self.assertEqual(res,3)

    def test_umbral_no_se_supera(self):
        res = pos_umbral([-1,2,0,5], 15)
        self.assertEqual(res,-1)

if __name__ == '__main__':
    unittest.main(verbosity=2)

