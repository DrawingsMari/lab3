import requests
import datetime
import json
import base_client

import classes


a = classes.GetId().execute()
print(a)

b = classes.FriendsAnalytics(a)
b.execute()































"""
data = {'user_id': '70165508', 'fields': 'bdate'}
r = requests.post('https://api.vk.com/method/friends.get', data = data)
print(r.json())


me = requests.get('https://api.vk.com/method/users.get?user_ids=kir_lys')

data = {'user_id': 70165508}
r = requests.post('https://api.vk.com/method/friends.get', data = data)
print(r.json())



#
ages_list = list()
for p in r.json()['response']:
    #requests.get('https://api.vk.com/method/users.get?user_ids=kir_lys')
    data = {'user_id': p,'fields':'bdate'}
    temp = requests.post('https://api.vk.com/method/users.get', data = data)
    if temp.json()['response'][0].get('bdate') != None:
        print(temp.json()['response'][0]['first_name'] + ' ' + temp.json()['response'][0].get('bdate'))

#pObj = json.load(g.text)

# Figura.__init__(self)

"""