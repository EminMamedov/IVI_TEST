import requests
from endpoints.base_endpoint import Endpoint
from endpoints.base_endpoint import auth

"""Это класс для использования запросов метода PUT и проверки для тестов с содержанием полей"""
class UpdateObject(Endpoint):

    def update_by_name(self, object_id, payload):
        self.response = requests.put('http://rest.test.ivi.ru/v2/character', json=payload, auth=auth)
        self.response_json = self.response.json()

    def check_name(self, name):
        assert self.response_json["result"]["name"] == name

    def check_universe(self, universe):
        assert self.response_json["result"]["universe"] == universe

    def check_education(self, education):
        assert self.response_json["result"]["education"] == education

    def check_weight(self, weight):
        assert self.response_json["result"]["weight"] == weight

    def check_height(self, height):
        assert self.response_json["result"]["height"] == height

    def check_identity(self, identity):
        assert self.response_json["result"]["identity"] == identity