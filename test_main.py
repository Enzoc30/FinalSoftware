import unittest
from flask import json
from flask import Flask, request, jsonify, abort
from main import *


class BilleteraTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    # Test Success
    def test_billetera_contactos_success(self):
        response = self.client.get('billetera/contactos?minumero=21345')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 200)
        self.assertEqual(data['contactos'], {"123": "Luisa", "456": "Andrea"})

    #Test Fail
    def test_billetera_contactos_fail(self):
        response = self.client.get('billetera/contactos?minumero=21345')
        data = json.loads(response.data)
        self.assertNotEqual(data["status"], 200)
        self.assertNotEqual(data['contactos'], {"123": "Ldsadasdasuisa", "4fsaas56": "Anfdsfdsdrea"})

    #Test Fail
    def test_historial_fail(self):
        response = self.client().get('/billetera/historial?minumero=123')
        data = json.loads(response.data)
        self.assertNotEqual(data["status"], 400)
        self.assertNotEqual(data['historial'], [ "Esta cuenta21345Te enviaron una operacion 100",
        "Esta cuenta21345Tgsdgfdglksfdhlksgasgaion 100"])

    def test_historial_fail(self):
        response = self.client().get('/billetera/pagar?minumero=21345&numerodestino=123&valor=100')
        data = json.loads(response.data)
        self.assertNotEqual(data["status"], 202)
        self.assertNotEqual(data['body'], "Realizado en 13/07/2023")


