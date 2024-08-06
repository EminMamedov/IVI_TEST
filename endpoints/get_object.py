import requests
from endpoints.base_endpoint import Endpoint
from endpoints.base_endpoint import auth

"""Это класс с методами GET, для отправки запросов и проверкой полей"""
class GetObject(Endpoint):

    def get_by_name(self, obj_id):
        self.response = requests.get(f'http://rest.test.ivi.ru/v2/character?name={obj_id}', auth=auth)
        self.response_json = self.response.json()


    def get_by_characters(self):
        self.response = requests.get('http://rest.test.ivi.ru/v2/characters', auth=('baku23@list.ru', 'APZrVp83vFNk5F'))
        self.response_json = self.response.json()


    def check_first_params(self):
        assert (len(self.response_json['result'])) == 302
        print(len(self.response_json['result']))


    def check_response_name(self):
        assert self.response_json["result"]["name"] == 'Emka'

    def check_response_universe(self):
        assert self.response_json["result"]["universe"] == 'Marvel Universe'

    def check_response_education(self):
        assert self.response_json["result"]["education"] == 'MTK'

    def check_response_weight(self):
        assert self.response_json["result"]["weight"] == 999

    def check_response_height(self):
        assert self.response_json["result"]["height"] == 1.73

    def check_response_identity(self):
        assert self.response_json["result"]["identity"] == 'Publicly known'


    def test_get_characters(self):
        assert len(self.response.json()["result"]) > 0
