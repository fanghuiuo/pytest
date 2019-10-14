from bs4 import BeautifulSoup
from multiprocessing import Pool
import requests
import lxml
import pymysql
import time 

header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='fh@791204', db='xiaozhu')
cursor=conn.cursor()

def getfz(url):
    res=requests.get(url,headers=header)
    soup=BeautifulSoup(res.text,'lxml')
    links=soup.select('#page_list > ul > li > a')
    for link in links:
        href=link.get('href')
        getxx(href)
def getxx(url):
    res=requests.get(url,headers=header)
    soup=BeautifulSoup(res.text,'lxml')
    fzmcs=soup.select('div.con_l > div.pho_info > h4 > em')
    fzdzs=soup.select('div.con_l > div.pho_info > p > span')
    fzjgs=soup.select('#pricePart > div.day_l > span')
    fzxms=soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    insql='insert into fz (fzmc,fzdz,fzjg,fzxm) values (%s,%s,%s,%s)'
    for fzmc,fzdz,fzjg,fzxm in zip(fzmcs,fzdzs,fzjgs,fzxms):
        fzmc=fzmc.get_text().strip()
        fzdz=fzdz.get_text().strip()
        fzjg=fzjg.get_text().strip()
        fzxm=fzxm.get_text().strip()
        cursor.execute(insql,(fzmc,fzdz,fzjg,fzxm))
        print(fzmc)
        conn.commit()
if __name__ == "__main__":
    urls = ['http://sy.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,13)]   
    pool=Pool(processes=3)
    pool.map(getfz,urls)
    '''for url in urls:
        getfz(url)
        time.sleep(2)'''