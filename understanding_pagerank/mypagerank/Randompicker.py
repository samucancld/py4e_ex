class RandomPicker:

    def __init__(self) -> None:
        pass

    def pickRandomLink(self, acursor):
        from_id = ''
        try:
            acursor.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')
            row = acursor.fetchone()
            print(row)
            fromid = row[0]
            url = row[1]
        except:
            print('No unretrieved HTML pages found')
            many = 0
            return 'break_it'

        # print(fromid, url, end=' ')

        # If we are retrieving this page, there should be no links from it
        acursor.execute('DELETE from Links WHERE from_id=?', (fromid, ) )
        return (url,fromid)
