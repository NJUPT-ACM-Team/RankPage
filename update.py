from rank.utils.parser import * 
from rank.database import Session
from rank.database.models import * 
import datetime
import time

import requests
URL = 'http://acm.njupt.edu.cn/acmhome/contestRankList.do?&contestId=240&page=%d'

def get_rows():
    rows = []
    for i in range(1, 13):
        url = URL % i
        print(url)
        r = requests.get(url)
        r.encoding='utf8'
        try:
            rs = parse_page(r.text)
        except Exception as var:
            print(var)
        rows = rows + rs
    return rows

def get_html():
    rows = get_rows()
    return put_rows_together(rows)

def update():
    html = get_html()
    rank = RankPage(html=html, time=datetime.datetime.now())
    Session.add(rank)
    Session.commit()
    r = Session.query(RankPage).order_by(RankPage.id.desc()).first()

if __name__ == '__main__':
    while True:
        update()
        time.sleep(40)
