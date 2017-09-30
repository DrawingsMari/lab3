import requests
import base_client
import json
import datetime
from datetime import datetime



class GetId(base_client.BaseClient):
    BASE_URL = "https://api.vk.com/method/"
    method = 'users.get'
    http_method = 'get'

    # Отправка запроса к VK API
    def _get_data(self, method, http_method):
        screen_name = input()
        response = requests.get(base_client.BaseClient.generate_url(self, GetId.method), params={'user_ids': screen_name})
        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        if response.status_code == 200:
            res = str(response.json()['response'][0]['uid'])
            return res
        else:
            print("Error!")

class Friends(base_client.BaseClient):
    BASE_URL = "https://api.vk.com/method/"
    method = 'friends.get'
    http_method = 'post'
    user_id = None

    # Конструктор
    def __init__(self, vk_id):
        self.user_id = vk_id

    # Отправка запроса к VK API
    def _get_data(self, method, http_method):
        data = {'user_id': self.user_id,'count': '5000', 'fields': 'bdate'}
        response = requests.post(base_client.BaseClient.generate_url(self, self.method), data=data)
        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        if response.status_code == 200:
            return response
        else:
            print("Error!")
            return "Error!"

    def PrintAges(self,response):
        if response.json()['response'] is not None:     # Есть ли друзья
            age_list = [0 for i in range(120)]
            today = datetime.now()
            for f in response.json()['response']:
                bdate_str = f.get('bdate')
                try:
                    bdate = datetime.strptime(bdate_str, '%d.%m.%Y')
                    days = (today - bdate).days
                    age = days // 365
                    age_list[age] += 1
                except:
                    pass
            # печать гистограммы
            for i in range(120):
                if age_list[i] > 0:
                    print(i, ': ', '#' * age_list[i])


    # Запуск клиента
    def execute(self) -> object:
        res = self._get_data(self.method, http_method=self.http_method)
        if res == "Error!":
            print("Error!")
            return res
        # Печать гистограммы
        self.PrintAges(res)




"""
    def get_params(self):
        r = requests.get(base_client.BaseClient.BASE_URL)
        return r.text

    def response_handler(self,r):
        if r.status_code  == requests.codes.ok:
            return r.json
        else

    def _get_data(self):

        return

"""