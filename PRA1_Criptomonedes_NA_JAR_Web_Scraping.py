#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -------- Importació de llibreries --------------------
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import json
import time
import os
from datetime import datetime

# --------- WEB SCRAPING ------------------------------
## Obtencio de la llista de crytomonedes ##
# Seleccionem la pàgina
url_site = 'https://coinmarketcap.com/'

# Baixem el codi de la pàgina
# Utilitzem la funció get de la llibreria request i l'objecte BeautifulSoup per manegar el codi html
page = requests.get(url_site)
soup_list = BeautifulSoup(page.content, 'html.parser')

data = soup_list.find('script', id="__NEXT_DATA__",type="application/json")
coins = {}

coin_data = json.loads(data.contents[0])
listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']

## Obtenció de les dades històriques per cada criptomoneda ##
for i in listings:
    coins[str(i['id'])] = i['slug']

# Declarar un dataframe buit
df = pd.DataFrame(columns=('Coin', 'Open($)', 'High($)', 'Low($)', 'Close($)', 'Volum($)', 'Market_cap($)'))

# Fem seguiment de les diferents criptomonedes
for i in coins:
    url_web = f'https://coinmarketcap.com/currencies/{coins[i]}/historical-data'
    driver = webdriver.Chrome("C:\chromedriver")
    driver.get(url_web)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source,'html')
    driver.quit()
    # Només hi apareix una taula, que serà l'índex [0]
    tables = soup.find_all('table')
    
    table = tables[0]
    # Agafem tots els "th" ("head") i "td" ("data")
    row_header = table.find_all(["tr","th","td"])
    date_rows = row_header[9].text
    date_row = datetime.strptime(date_rows, '%b %d, %Y').date()
    open_row = pd.to_numeric(row_header[10].text.replace('$', '').replace(',',''))
    high_row = pd.to_numeric(row_header[11].text.replace('$', '').replace(',',''))
    low_row = pd.to_numeric(row_header[12].text.replace('$', '').replace(',',''))
    close_row = pd.to_numeric(row_header[13].text.replace('$', '').replace(',',''))
    volume_row = pd.to_numeric(row_header[14].text.replace('$', '').replace(',',''))
    market_cap_row = pd.to_numeric(row_header[15].text.replace('$', '').replace(',',''))
    coin = coins[i]

    # Amb pandas bolquem les dades a un "dataframe", a partir del diccionari creat
    df = df.append({'Coin': coin, 'Open($)': open_row, 'High($)': high_row, 'Low($)': low_row, 'Close($)': close_row, 'Volum($)': volume_row, 'Market_cap($)': market_cap_row}, ignore_index=True)

# I el "dataframe" es grava a un fitxer "csv"
fileName = 'Criptomonedes_Historical_Data_' + date_row.strftime('%Y%m%d') + '.csv'
pathName = r"C:\python\\" + fileName
# Es comprova si no existeix abans de crear-lo
if not os.path.exists(pathName):
    df.to_csv(pathName, index = False)


# In[ ]:




