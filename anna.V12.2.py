import requests 
import json
import sys 

searching_word = "राजनीति"
uri ='https://bg.annapurnapost.com/'
p = 'api/search?page={}&title='

data ={}
articles =[]
pageCount = 1
uniqueId =True
try:
    with open("data.json", "r") as df:
        data = json.load(df)
        articles =data['articles']
        pageCount =data['pageCount']
        uniqueId =False
       
except:
    print('..first time..')


def start_from(articleId):
    for art in articles[-10:]:
        if art['id'] == articleId:
            return False
    global uniqueId
    uniqueId = True
    return True

def req(url):
    try:
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
            # check if it already enter in prevoius stop
            if uniqueId or start_from(article['id']):
                articles.append(article)
    except:
        print('--error--')
        data['articles'] = articles
        data['pageCount'] = pageCount
        with open("data.json", "w") as df:
            json.dump(data, df)
        sys.exit()
while True:
    url = uri+p.format(pageCount) + searching_word
    req(url)
    pageCount +=1