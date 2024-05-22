import unittest
from rest_framework.test import APIClient
from rest_framework import status

class TestObterNumDiv(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_intervalo_valido(self):
        response = self.client.get('/api/obter-num-div/', {'intervaloDe': 1, 'intervaloAte': 10})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('resultado', response.data, "Não retornou resultado")
        self.assertIsInstance(response.data['resultado'], int)

    def test_intervalo_naoint(self):
        response = self.client.get('/api/obter-num-div/', {'intervaloDe': 'abc', 'intervaloAte': 10})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data, "Não retornou erro")
        self.assertEqual(response.data['error'], "Por favor, informe números inteiros válidos")

    def test_intervalo_negativo(self):
        response = self.client.get('/api/obter-num-div/', {'intervaloDe': -1, 'intervaloAte': 10})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data, "Não retornou erro")
        self.assertEqual(response.data['error'], "Por favor, informe números de intervalo válidos")

if __name__ == '__main__':
    unittest.main()
