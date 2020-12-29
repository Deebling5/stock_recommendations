import streamlit as st
import pandas as pd
import quandl as q
import requests
import plotly.graph_objects as go
from bs4 import BeautifulSoup
import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import os
from twilio.rest import Client
from selenium.webdriver.common.keys import Keys 
import pandas as pd

## ET Now Feed Scrapper

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(r"C:\Users\91801\Desktop\Python Learning\Stock Indigator -Abhijay\chromedriver.exe", options = options)    
driver.get("https://economictimes.indiatimes.com/markets/stocks/recos")  
driver.execute_script("window.scrollTo(0, 6080)") 
time.sleep(3)
page_source = driver.page_source

L = []

for x in range(45):
    soup = BeautifulSoup(page_source, 'lxml')
    #print(soup)
    a = soup.find_all('div', {'class':'eachStory'})[x].find('h3').text    
    L.append(a)
    
Str = ' '.join([str(elem) for elem in L])

df = pd.DataFrame(L, columns=['Recos'])
#print (df)

for x in range(45):
    print(L[x])
st.dataframe(df)
