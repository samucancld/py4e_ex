from urllib.parse import urljoin, urlparse


class Spider:

    def __init__(self) -> None:
        pass

    def spiderIt(self, soup, url, allowed_websites, acursor, aconnection, fromid ):
        '''por cada ancor tag en el html parseado (soup) evita errores y si está todo bien agrega urls a las paginas y setea los from y to id'''
        tags = soup('a')
        count = 0
        for tag in tags:
            href = tag.get('href', None)
            if ( href is None ) : continue
            # Resolve relative references like href="/contact"
            up = urlparse(href)
            if ( len(up.scheme) < 1 ) :
                href = urljoin(url, href)
            ipos = href.find('#')
            if ( ipos > 1 ) : href = href[:ipos]
            if ( href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif') ) : continue
            if ( href.endswith('/') ) : href = href[:-1]
            # print href
            if ( len(href) < 1 ) : continue

		    # Check if the URL is in any of the webs
            found = False
            for web in allowed_websites:
                if ( href.startswith(web) ) :
                    found = True
                    break
            if not found : continue

            acursor.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( href, ) )
            count = count + 1
            aconnection.commit()

            acursor.execute('SELECT id FROM Pages WHERE url=? LIMIT 1', ( href, ))
            try:
                row = acursor.fetchone()
                toid = row[0]
            except:
                print('Could not retrieve id')
                continue
            # print fromid, toid
            acursor.execute('INSERT OR IGNORE INTO Links (from_id, to_id) VALUES ( ?, ? )', ( fromid, toid ) )
        return count