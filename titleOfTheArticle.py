'''
패키지 설치
1. bs4
2. selenium
3. openpyxl
'''

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%9D%B4%EC%8A%A4%ED%8A%B8%EC%86%8C%ED%94%84%ED%8A%B8&sort=0&photo=0&field=0&pd=3&ds=2018.08.19&de=2021.08.19&cluster_rank=1777&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20180819to20210819,a:all&start=1"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

# 기사 제목의 셀렉터를 카피해서 넣음
articles = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')

for article in articles:
  a_tag = article.select_one('div > div > a')
  
  title = a_tag.text
  print(title)
  
driver.quit()
