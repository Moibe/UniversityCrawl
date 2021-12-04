import requests
# from bs4 import BeautifulSoup
import json
import csv
from datetime import date
from datetime import datetime

url = 'https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json'
res = requests.get(url)

today = date.today()
time = datetime.today()
csvTag = str(today)

js = json.loads(res.content)
results = []
results.append(['web_pages','name','alpha_two_code','state-province','domains','country'])
for row in js:
    results.append([row['web_pages'], row['name'], row['alpha_two_code'],row['state-province'],row['domains'],row['country']])
    
for i in results:
    with open('jsToExcel'+ str(csvTag) +'.csv','a',newline='',errors='ignore',encoding='ANSI') as fd:
        wr = csv.writer(fd, dialect='excel')
        wr.writerow(i)