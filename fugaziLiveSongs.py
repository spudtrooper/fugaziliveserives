import os, re, string, sys, urllib2
from BeautifulSoup import BeautifulSoup
from fugaziLiveSeries import *

"""
Reads the files from out/ and prints out histogram of songs:

<fileName>|<title>|<city>|<song-1>| ... |<song-n>
"""

def main(argv):
    for fileName in os.listdir(OUT_DIR):
        try:
            processFile(fileName)
        except UnicodeEncodeError as e:
            log(e)

def processFile(fileName):
    log(fileName)
    with open(os.path.join(OUT_DIR, fileName), 'r') as f:
        page = ''.join(f.readlines())
        soup = BeautifulSoup(page)
        url = 'http://www.dischord.com/fugazi_live_series/%s' % (fileName)
        cite = soup.find('cite').text
        songs = []
        for td in soup('td', {'class': 'track_name'}):
            songs += [td.text.strip()]
        if len(songs) > 1:
            stuff = [fileName,cite]
            stuff += songs
            print SEP.join(stuff)

if __name__ == '__main__':
    main(sys.argv)
