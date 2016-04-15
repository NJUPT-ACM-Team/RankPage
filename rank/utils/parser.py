from bs4 import BeautifulSoup
from ..database import Session
from ..database.models import *
import re

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all('table')[1]
    trs = table.find_all('tr')[1:]
    rows = []
    for tr in trs:
        row = []
        tds = tr.find_all('td')
        account = re.findall(r'(2016nycpc[\d]{4})', tds[1].prettify())[0]
        stu = Session.query(Student).filter(Student.account==account).first()
        row.append('<td>' + ''.join(re.findall(r'([\d]+?)', tds[0].prettify())) + '</td>')
        row.append('<td>' + account + '</td>')
        if stu is not None:
            row.append('<td>%s/%s</td>' % (stu.stu_id, stu.name))
        else:
            row.append('<td>(backup)</td>')
            
        row.append('<td>' + ''.join(re.findall(r'([\d]+?)', tds[2].prettify())) + '</td>')
        row.append('<td>' + ''.join(re.findall(r'([\d]+?)', tds[3].prettify())) + '</td>')
        for td in tds[4:]:
            row.append(td.prettify())
        rows.append('<tr>'+''.join(row)+'</tr>')
    return rows

def put_rows_together(rows):
    head = '<thead>' + \
           '''
    <th>Rank</th>
    <th>User's contest account</th>
    <th>User</th>
    <th>Solved</th>
    <th>Total</th>
    <th>A</th>
    <th>B</th>
    <th>C</th>
    <th>D</th>
    <th>E</th>
    <th>F</th>
    <th>G</th>
    <th>H</th>
    <th>I</th>
    <th>J</th>
    <th>K</th>
    <th>L</th>
           '''  \
           + '</thead>'
    body = '<tbody>' + ''.join(rows) + '</tbody>'

    return '<table>' + head + body + '</table>'
