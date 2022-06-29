from random import random
from urllib.parse import urljoin, urlparse;from urllib.request import urlopen
from bs4 import BeautifulSoup
from Sslignorer import *;from Sqlconnector import SQLiteConnector;from Weballower import WebAllower;from Randompicker import RandomPicker;from Htmlsouper import HTMLSouper; from spider import Spider

my_sql_connector = SQLiteConnector()
my_conection = my_sql_connector.connect(dbname = 'spider')

my_cursor = my_conection.cursor()

stsquery = ''
queryhandler = open('starting_script.sql')
for line in queryhandler:
    stsquery = stsquery + line
stsquery = stsquery.rstrip()


my_cursor.executescript(stsquery)
any_axisting_webpage = my_cursor.fetchone()

my_web_allower = WebAllower()
allowed_websites = my_web_allower.checkAndAllow(webpage=any_axisting_webpage,acursor=my_cursor,aconnection=my_conection)

print('Debug Allowed Websites:',allowed_websites)

many = 0
while True:
    if ( many < 1 ) :
        sval = input('How many pages:')
        if ( len(sval) < 1 ) : break
        many = int(sval)
    many = many - 1
   
    my_random_picker = RandomPicker()
    random_tuple = my_random_picker.pickRandomLink()
    if random_tuple == 'break_it' : break
    url = random_tuple[0]
    fromid = random_tuple[1]

    try:
        my_html_souper = HTMLSouper()
        soup_and_html = my_html_souper.soupIt(url=url, acursor=my_cursor,aconnection=my_conection)
        if soup_and_html == 'go up': continue
        soup = soup_and_html[0]
        html = soup_and_html[1]

    except KeyboardInterrupt:
        print('')
        print('Program interrupted by user...')
        break
    except:
        print("Unable to retrieve or parse page")
        my_cursor.execute('UPDATE Pages SET error=-1 WHERE url=?', (url, ) )
        my_conection.commit()
        continue

    my_cursor.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( url, ) )
    my_cursor.execute('UPDATE Pages SET html=? WHERE url=?', (memoryview(html), url ) )
    my_conection.commit()
 
    my_spider = Spider()

    count = my_spider.spiderIt(soup=soup,url=url,allowed_websites=allowed_websites,acursor=my_cursor,aconnection=my_conection,fromid=fromid)

    print(count)

my_cursor.close()
