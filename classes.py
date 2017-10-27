import requests
import base_client
import json
import datetime


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
        if response.status_code == requests.codes.ok:
            res = str(response.json()['response'][0]['uid'])
            return res
        else:
            print("Error!")

class FriendsAnalytics(base_client.BaseClient):
    BASE_URL = "https://api.vk.com/method/"
    method = 'friends.get'
    http_method = 'post'
    user_id = None

    def __init__(self, vk_id):
        self.user_id = vk_id

    # Отправка запроса к VK API
    def _get_data(self, method, http_method):
        data = {'user_id': self.user_id,'count': '5000', 'fields': 'bdate'}
        response = requests.post(base_client.BaseClient.generate_url(self, self.method), data=data)
        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        if response.status_code == requests.codes.ok:
            return response
        else:
            print("Error!")

    def Diagram(self,response):
        if response.json()['response'] is not None:     # Есть ли друзья
            blist = list()
            for person in response.json()['response']:
                if person.get('bdate') is None:     # Человек с не пустой датой
                    continue
                else:
                    try:
                        blist.append(datetime.datetime.strptime(person['bdate'], '%d.%m.%Y'))
                    except:
                        continue
            today = datetime.datetime.today()
            agelist = list()
            for b in blist:
                age = today.year - b.year - 1
                if today.month <= b.month:
                    if today.day <= b.day:
                        age += 1
                agelist.append(age)
            agelist.sort()
            temp = agelist[0]
            print(agelist[0], end='\t')
            for a in agelist:
                if a != temp:
                    print()
                    print(a, end='\t')
                    print('#', end='')
                    temp = a
                else:
                    print('#', end='')


    # Запуск клиента
    def execute(self) -> object:
        res = self._get_data(self.method, http_method=self.http_method)
        if res == "Error!":
            print("Error!")
            return res
        # Печать диаграммы
        self.Diagram(res)




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