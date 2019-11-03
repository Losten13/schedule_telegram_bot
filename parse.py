from bs4 import BeautifulSoup
import requests
import codecs
import binascii
import urllib

def hex_to_normal(bin_text):
    str1 = bin_text.hex()
    str2 = binascii.unhexlify(str1).decode('UTF-8')
    return str2

def get_data(group,date):
    group_encode = group.encode('windows-1251')
    date_encode = date.encode('windows-1251')
    data = {"group":group_encode,"sdate":"","edate":date_encode,"faculty":"0","teacher":"","n":"700"}
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "194.44.112.6",
        "Connection": "keep-alive",
        "Content-Length": "60",
        "Cache-Control": "max-age=0",
        "Origin": "http://194.44.112.6",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "http://194.44.112.6/cgi-bin/timetable.cgi?n=700",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6"}
    URL = 'http://194.44.112.6/cgi-bin/timetable.cgi?n=700'
    s = requests.Session()
    bin_html = s.post(URL, data=data,headers=header).content
    normal_html=hex_to_normal(bin_html)
    return normal_html

def myparse(group,date):
    html = get_data(group,date) 
    soup = BeautifulSoup(html,"lxml")
    trs = soup.find_all('tr')
    result = []
    for tr in trs:
        tds = tr.find_all('td')
        lesson = []
        for td in tds :
            lesson.append(str(td.string).replace("  ",""))
        result.append(lesson)

    return result    

