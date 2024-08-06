import requests
from endpoints.base_endpoint import Endpoint
from endpoints.base_endpoint import auth

"""Это класс для использования запросов метода POST и проверки для тестов с содержанием полей"""
class CreateObject(Endpoint):

    def new_object(self, payload):
        self.response = requests.post('http://rest.test.ivi.ru/v2/character', json=payload, auth=auth)
        self.response_json = self.response.json()

    def delete_first_initial_condition(self):
        self.response = requests.post('http://rest.test.ivi.ru/v2/reset', json=None, auth=('baku23@list.ru', 'APZrVp83vFNk5F'))

    def create_200_superheroes(self, base_payload):
        for i in range(200):
            # Добавляем номер к имени
            payload = base_payload.copy()  # Создаем копию, чтобы не изменять базовые данные
            payload["name"] = f"Konihamaru{i + 1}"
            self.response = requests.post('http://rest.test.ivi.ru/v2/character', json=payload,
                                     auth=('baku23@list.ru', 'APZrVp83vFNk5F'))
            if self.response.status_code == 200:
                print(f"Запись {i + 1} успешно создана")
            else:
                print(f"Ошибка при создании записи {i + 1}: {self.response.text}")


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