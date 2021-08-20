'''
openpyxl 사용 예시

from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
#sheet이름
ws1.title = "네이버 기사 스크래핑"
#행 추가 
ws1.append(["제목", "링크", "신문사"])
#행 추가 
ws1.append(['1','2','3'])

#파일이름
wb.save(filename='네이버 기사 스크래핑.xlsx')
'''

from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

wb = Workbook()
ws1 = wb.active

#sheet이름
ws1.title = "네이버 기사 스크래핑"
#행 추가
ws1.append(["제목", "본문", "날짜"])
# 총 400페이지까지 크롤링
for p in range(1, 4000+1, 10):
    # 주소 맨 마지막 start 부분을 format()으로 처리
    url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%9D%B4%EC%8A%A4%ED%8A%B8%EC%86%8C%ED%94%84%ED%8A%B8&sort=0&photo=0&field=0&pd=3&ds=2018.08.19&de=2021.08.19&cluster_rank=1777&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20180819to20210819,a:all&start={p}".format(p = p)
    driver.get(url)
    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')
    articles = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')

    for article in articles:
        a_tag1 = article.select_one('div > div > a')
        a_tag1 = article.select_one("a.news_tit")
        title = a_tag1.text

        a_tag2 = article.select_one('div > div > div')
        a_tag2 = article.select_one("div.news_dsc")
        content = a_tag2.text

        a_tag3 = article.select_one('div > div > div > a > span')
        a_tag3 = article.select_one("span.info")
        date = a_tag3.text

        ws1.append([title, content, date])

driver.quit()

wb.save(filename='네이버 기사 스크래핑.xlsx')
