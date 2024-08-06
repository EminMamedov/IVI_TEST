import conftest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject
from conftest import obj_id

"""Это тестовый файл, где мы прогоняем все наши тесты по сценаирию , который я описал в файле test_scenarios.md"""


"""Добавление нового персонажа"""
def test_post():
    new_object_endpoint = CreateObject()
    payload = conftest.payload1
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_name(payload["name"])
    new_object_endpoint.check_universe(payload['universe'])
    new_object_endpoint.check_education(payload['education'])
    new_object_endpoint.check_weight(payload['weight'])
    new_object_endpoint.check_height(payload['height'])
    new_object_endpoint.check_identity(payload['identity'])
    new_object_endpoint.check_response_is_200()

"""Проверить, что при отправке некорректных данных (неверные типы, пропущенные поля) возвращается ошибка."""
def test_post_null():
    new_object_endpoint = CreateObject()
    payload = conftest.payload3
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_response_is_400()



"""Получение информации о персонаже по имени с использованием независимого теста с фиктурой из conftest.py"""
def test_get_name(obj_id):
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_name(obj_id)
    get_obj_endpoint.check_response_is_200()
    get_obj_endpoint.check_response_name()
    get_obj_endpoint.check_response_education()
    get_obj_endpoint.check_response_identity()
    get_obj_endpoint.check_response_weight()
    get_obj_endpoint.check_response_height()
    get_obj_endpoint.check_response_universe()

"""Получение списка персонажей"""
def test_get_characters():
    get_object_endpoint_all = GetObject()
    get_object_endpoint_all.get_by_characters()
    get_object_endpoint_all.check_response_is_200()
    get_object_endpoint_all.get_by_characters()


"""Изменение информации о персонаже с использованием независимого теста с фиктурой из conftest.py"""
def test_put(obj_id):
    update_object_endpoint = UpdateObject()
    payload = conftest.payload2
    update_object_endpoint.update_by_name(obj_id, payload)
    update_object_endpoint.check_response_is_200()
    update_object_endpoint.check_name(payload['name'])
    update_object_endpoint.check_universe(payload['universe'])
    update_object_endpoint.check_education(payload['education'])
    update_object_endpoint.check_weight(payload['weight'])
    update_object_endpoint.check_height(payload['height'])
    update_object_endpoint.check_identity(payload['identity'])

"""Удаление персонажа"""
def test_delete_name():
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_by_name('Konihamaru')
    delete_object_endpoint.check_response_is_200()


"""Проверить, что при попытке удалить несуществующего персонажа возвращается ошибка "No such name"."""
def test_delete_name_null():
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_by_name('Itaci')
    delete_object_endpoint.check_response_is_400()


"""Проверить, что при попытке добавления больше 500 персонажей возвращается ошибка "Collection can't contain more than 500 items"""
def test_post_many_obj():
    create_200_superheroes = CreateObject()
    base_payload = conftest.base_payload
    create_200_superheroes.create_200_superheroes(base_payload=base_payload)
    create_200_superheroes.check_response_is_400()

"""Сброс коллекции в первоначальное состояние"""
def test_delete_first_initial_condition():
    delete_all_endpoints = CreateObject()
    delete_all_endpoints.delete_first_initial_condition()
    delete_all_endpoints.check_response_is_200()


"""Проверить, что база данных была сброшена в первоначальное состояние."""
def test_api():
    get_first_params = GetObject()
    get_first_params.get_by_characters()
    get_first_params.check_first_params()