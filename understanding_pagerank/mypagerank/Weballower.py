from xml.dom.pulldom import default_bufsize


class WebAllower:
    defaulturl = 'http://www.dr-chuck.com/'
    def __init__(self) -> None:
        pass


    def checkAndAllow(self, webpage, acursor, aconnection):
        if webpage is not None:
            print("=================CRAWL RETOMADO==================")
        else :
            starturl = input(f'Enter web url or enter to use {self.defaulturl}: ')
            if ( len(starturl) < 1 ) : starturl = self.defaulturl
            if ( starturl.endswith('/') ) : starturl = starturl[:-1]
            web = starturl
            if ( starturl.endswith('.htm') or starturl.endswith('.html') ) :
                pos = starturl.rfind('/')
                web = starturl[:pos]

            if ( len(web) > 1 ) :
                acursor.execute('INSERT OR IGNORE INTO Webs (url) VALUES ( ? )', ( web, ) )
                acursor.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( starturl, ) )
                aconnection.commit()

        
        acursor.execute('''SELECT url FROM Webs''')
        webs = list()

        #for each existing webpage in the db
        for any_axisting_webpage in acursor:
            webs.append(str(any_axisting_webpage[0]))

        return webs