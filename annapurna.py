import requests
import time
import json
 
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--kiosk")

path = '/usr/bin/chromedriver'

# webdriver.maximize_window()

driver = webdriver.Chrome(path, options=chrome_options)
url = 'https://annapurnapost.com'

res = driver.get(url)

searchIcon =driver.find_element(By.ID,'global-search-trigger')
searchIcon.click()
search = driver.find_element(By.ID, 'searchField')
# query term
searching_word = "राजनीति"
search.send_keys( searching_word + Keys.ENTER)

try:
    lk = []
    while True:
        search_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchPage"))
        )
        articles = search_page.find_elements_by_tag_name('a')
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        for ar in articles:
            l = ar.get_attribute("href")
            if l not in lk:
                lk.append(l)
            if len(lk)>= 30 :
                break
        if len(lk)>=30:
            break
    # loop through each article to get the data
    data ={}
    for elink in lk:
        res = requests.get(elink)
        soup = bs(res.content, 'html.parser')
        title = soup.find('h1').text
        content = soup.find('p').text
        data[title] =content
    with open('data.json', 'w') as jsonfile:
        json.dump(data, jsonfile)


except:
     driver.quit()
