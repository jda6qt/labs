import pandas as pd
import requests
import streamlit as st
import urllib.request
import json
# Conduct analysis:
url = 'https://www.saferproducts.gov/RestWebServices/Recall'
query = '?format=json&RecallTitle=Gas'
# header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'}
# raw = requests.get(url+query,headers=header)
# data = raw.json()
response = urllib.request.urlopen(url+query)
response_bytes = response.read()
data = json.loads(response_bytes)
response.close()
df = pd.DataFrame.from_dict(data)
temp = df['ManufacturerCountries']
clean_countries = []
for i in range(len(temp)):
    if len(temp[i]) > 0: 
        countries = []
        for j in range(len(temp[i])):
            countries.append(temp[i][j]['Country']) 
        clean_countries.append(countries)  
    else:
        clean_countries.append('')  
df['manufacturer_countries'] = clean_countries
country_counts = df['manufacturer_countries'].value_counts()
# Create streamlit output:
st.title('Manufacturer Country Statistics')
st.write(country_counts)