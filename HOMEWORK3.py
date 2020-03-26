import requests
from bs4 import BeautifulSoup

header = 

data = requests.get("https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309")

print(data)
print(data.text)