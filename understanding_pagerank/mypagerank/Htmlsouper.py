from bs4 import BeautifulSoup
from Sslignorer import ctx
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen

class HTMLSouper:
    def __init__(self) -> None:
        pass

    def soupIt(self,url, acursor, aconnection):
        document = urlopen(url, context=ctx)

        html = document.read()
        if document.getcode() != 200 :
            print("Error on page: ",document.getcode())
            acursor.execute('UPDATE Pages SET error=? WHERE url=?', (document.getcode(), url) )

        if 'text/html' != document.info().get_content_type() :
            print("Ignore non text/html page")
            acursor.execute('DELETE FROM Pages WHERE url=?', ( url, ) )
            aconnection.commit()
            return 'go up'
            # continue

        print('('+str(len(html))+')', end=' ')

        soup = BeautifulSoup(html, "html.parser")
        return (soup,html)