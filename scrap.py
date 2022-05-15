import requests 
import json
import sys 

searching_word = "राजनीति"
uri ='https://bg.annapurnapost.com/'
p = 'api/search?page={}&title='
page = 1

articles = {}

def req(url):
    j = requests.get(url).json()
    data = j['data']
    items = data['items']
    for i in items:
        articles[i['title']]=i['content']
        if len(articles)>=30:
            print(len(articles))
            with open('data.json', 'w') as jsonfile:
                json.dump(articles, jsonfile)
            sys.exit()
    next = data['links']['next']
    return next

while True:
    url = uri+p.format(page) + searching_word
    j = req(url)
    page +=1