import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject

@pytest.fixture()
def obj_id():
    create_object = CreateObject()
    payload = {
        "name": "Emka",
        "universe": "Marvel Universe",
        "education": "MTK",
        "weight": 999,
        "height": 1.73,
        "identity": "Publicly known"
    }

    create_object.new_object(payload)
    yield create_object.response_json["result"]["name"]
    delete_object = DeleteObject()
    delete_object.delete_by_name(create_object.response_json["result"]["name"])

"""Payload для метода POST"""
payload1 = {
        "name": "Konihamaru",
        "universe": "Naruto",
        "education": "ninjutsu school",
        "weight": 83,
        "height": 1.83,
        "identity": "Publicly known"
    }


"""Payload для метода PUT"""
payload2 = {
        "name": "Emka",
        "universe": "Marvel Universe",
        "education": "Mik",
        "weight": 59,
        "height": 1.43,
        "identity": "Publicly known"
    }


"""Payload для метода POST с пустыми полями"""
payload3 = {
        "name": "Konihamaru",
        "universe": "",
        "education": "",
        "weight": 83,
        "height": 1.83,
        "identity": "Publicly known"
    }

"""Payload для метода POST c добавлением 200-х записей"""
base_payload = {
        "name": "Konihamaru",
        "universe": "Naruto",
        "education": "ninjutsu school",
        "weight": 83,
        "height": 1.83,
        "identity": "Publicly known"
    }