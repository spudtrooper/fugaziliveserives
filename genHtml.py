import fileinput, sys
from collections import OrderedDict
from fugaziLiveSeries import *

"""
Reads from STDIN and outputs HTML.  Input is in the form:

<url>|<song-1>|...|<song-2>

And should be created from fugaziLiveSongs.py

"""

def main(argv):
    songs = []
    titles = []
    titles2fileNames = {}
    titles2songs = {}
    for line in fileinput.input():
        line = line.strip()
        parts = line.split(SEP)
        fileName = parts.pop(0)
        title = parts.pop(0)
        titles2songs[title] = parts
        titles2fileNames[title] = fileName
        titles += [title]
        for song in parts:
            if song not in songs:
                songs += [song]

    songs.sort()
    titles.sort()

    print "<html>"
    print "<head>"
    print "<link rel='stylesheet' type='text/css' href='fugaziLiveSeries.css' />"
    print "</head>"
    print "<body>"

    print "<table>"
    print "<tr>"
        
    print "<th class='c'>Show / Song</th>"
    
    for song in songs:
        print "<th class='d'><p class='dd'>%s</p></th>" % (song)
    print "</tr>"

    for title in titles:
        songList = titles2songs[title]
        print '<tr>'
        url = 'http://www.dischord.com/fugazi_live_series/%s' % (
            titles2fileNames[title])
        print "<td class='show'><a href='%s'>%s</a> (%d)</td>" % (
            url, title, len(songList))
        for song in songs:
            cls = 'b'
            ans = 'No'
            if song in songList:
                cls = 'a'
                ans = 'Yes'
            alt = '%s @ %s: %s' % (song, title, ans)
            print "<td class='%s' title='%s'></td>" % (cls, alt)
        print '</tr>'

    print "</table>"
    
    print "<div><a href='http://www.dischord.com/fugazi_live_series'>Source</a> | <a href='https://github.com/spudtrooper/fugaziliveserives'>github</a></div>"

if __name__ == '__main__':
    main(sys.argv)
