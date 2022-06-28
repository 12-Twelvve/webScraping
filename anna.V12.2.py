import requests 
import json
import sys 

searching_word = "राजनीति"
uri ='https://bg.annapurnapost.com/'
p = 'api/search?page={}&title='

data ={}
articles =[]
pageCount = 1

try:
    with open("data.json", "r") as df:
        data = json.load(df)
        articles =data['articles']
        pageCount =data['pageCount']
        uniqueId =False
except:
    print('..first time..')

def req(url):
    print(len(articles))
    print(pageCount)
    article ={}
    res = requests.get(url).json()
    articleData = res['data']
    for i in articleData['items']:
        article['id'] = i['id']
        article["title"] =i['title']
        article["content"] =i['content']
        article["author"] =i['author']
        if len(articles)>=100:
            data['articles'] = articles
            data['pageCount'] = pageCount
            with open("data.json", "w") as dff:
                json.dump(data, dff)
            sys.exit()
        articles.append(article)
        
while True:
    url = uri+p.format(pageCount) + searching_word
    req(url)
    pageCount +=1
