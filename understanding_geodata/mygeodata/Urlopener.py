import urllib.request, urllib.parse, urllib.error
from Urlcreator import ctx
class UrlOpener:

    def __init__(self) -> None:
        pass

    def openURL(self, url):
        # print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        # print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
        return data

