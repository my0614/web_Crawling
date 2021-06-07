import requests
from bs4 import BeautifulSoup
from datetime import datetime 

#웹크롤링할 url가져오기
source = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98%ED%99%95%EC%A7%84%EC%9E%90&oquery=%EC%9D%BC%EB%B3%84%EC%BD%94%EB%A1%9C%EB%82%98%ED%99%95%EC%A7%84%EC%9E%90&tqi=h7Gfmlprvxsss4OyKNGssssssHG-349957').text
#html 형식으로 가져오기
soup = BeautifulSoup(source, "html.parser")
#class 이름이 info_variation인것 찾기
a = soup.select(".info_variation")

#리스트로 국내현황 요소이름 저장
part = ['확진환자','격리해제','사망자','검사진행']

#datetime함수를 사용하여 현재 날짜 가져오기
print(datetime.today().strftime("<%Y년 %m월 %d일 코로나확진자 국내현황>"))
for i in range(4):
    print(part[i],a[i].text) #요소이름과 웹크롤링한 코로나수 출력하기

      
