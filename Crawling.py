from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'

}

data = requests.get(
    "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303", headers=headers)

print(data)
#print(data.text)

soup = BeautifulSoup(data.text, 'html.parser')
movies = soup.select('#old_content > table > tbody > tr')

#print(movies)

for m in movies:
    anchor = m.select_one('td.title > div > a')
    point = m.select_one("td.point")
    if anchor is not None:
        print(anchor.text,point.text)
