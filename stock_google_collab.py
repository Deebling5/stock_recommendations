
## ET Now Feed Scrapper
import pandas as pd
#import quandl as q
import requests
#import plotly.graph_objects as go
from bs4 import BeautifulSoup
import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import os
#from twilio.rest import Client
from selenium.webdriver.common.keys import Keys 

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)
   
driver.get("https://economictimes.indiatimes.com/markets/stocks/recos")  
driver.execute_script("window.scrollTo(0, 6080)") 
time.sleep(3)
page_source = driver.page_source

L = []

for x in range(50):
    soup = BeautifulSoup(page_source, 'lxml')
    #print(soup)
    a = soup.find_all('div', {'class':'eachStory'})[x].find('h3').text    
    L.append(a)
    
Str = ' '.join([str(elem) for elem in L])

#df = pd.DataFrame(L, columns=['Recos'])
#print (df)

for x in range(45):
    print(L[x])
