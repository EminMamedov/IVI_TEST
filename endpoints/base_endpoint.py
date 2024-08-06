"""Это базовый эндпоинт, который мы используем во всех классах и методах, которые у нас есть - для проверки статус кодов"""


"""Здесь же я храню почту и пароль для авторизации, в задании было указано чтобы я не выгружал лог и пароль на ГИТ
Поэтому реальные данные будут заменены, а настоящие высланы вместе с задание HR."""
auth = ('mail@list.ru', 'pass')

class Endpoint:
    response = None
    response_json = None

    def check_response_is_200(self):
        if self.response.status_code == 200:
            return  # Если код ответа 200, просто возвращаем
        else:
            error_message = {
                "status": self.response.status_code,
                "message": self.response.text
            }
            raise Exception(f"Ошибка: {error_message}")  # Возвращаем описание ошибки в формате JSON


    def check_response_is_400(self):
        assert self.response.status_code == 400