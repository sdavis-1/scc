import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200325',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#select를 이용하여 tr 불러오기
# TODO: tbody 를 사용하지 않는 건 어떨까요?
songs = soup.select('tbody > tr.list')
#print(songs)
rank = 1
for song in songs:
   name = song.select_one('td.info > a.title.ellipsis')
   artist = song.select_one('td.info > a.artist.ellipsis')
   print(rank, name.text.strip(), ": ", artist.text.strip())
   rank +=1