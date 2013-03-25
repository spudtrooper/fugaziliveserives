import os, re, string, sys, urllib2
from BeautifulSoup import BeautifulSoup
from fugaziLiveSeries import *

"""
Reads shows from Fugazi Live Series
(http://www.dischord.com/fugazi_live_series) and outputs the links to
STDOUT.
"""

LAST_URL_FILE = 'lastUrl.txt'

def saveLastUrl(url):
    with open(LAST_URL_FILE, 'w') as f:
        f.write(url)

def getLastUrl():
    file = LAST_URL_FILE
    if not os.path.exists(file):
        return None
    with open(file, 'r') as f:
        return f.read()
    return None

class FugaziLive:

    def main(self, url):
        self.loop(url)

    def loop(self, url):
        log(url)
        page = urllib2.urlopen(url)
        imgs = []
        soup = BeautifulSoup(page)
        numResults = 0
        for div in soup('td', {'class': 'date'}):
            for a in div.findAll('a'):
                href = str(a['href'])
                if re.match('/fugazi_live_series/', href):
                    print href
                    numResults += 1
        saveLastUrl(url)
        log('Found %d results for %s...' % (numResults, url))

        # Find the next link
        a = soup.find('a', {'class': 'next_page'})
        if a:
            newUrl = 'http://www.dischord.com/' + a['href']
            self.loop(newUrl)

def main(argv):
    prog = argv.pop(0)
    if len(argv) > 0:
        url = argv.pop(0)
    else:
        url = getLastUrl()
        if not url:
            url = 'http://www.dischord.com/fugazi_live_series'
    FugaziLive().main(url)

if __name__ == '__main__':
    main(sys.argv)
