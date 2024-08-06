import requests
from endpoints.base_endpoint import Endpoint
from endpoints.base_endpoint import auth

"""Это класс с методом DELETE"""
class DeleteObject(Endpoint):

    def delete_by_name(self, object_id):
        self.response = requests.delete(f'http://rest.test.ivi.ru/v2/character?name={object_id}',
                                        auth=auth)
        self.response_json = self.response.json()
