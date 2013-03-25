import fileinput, sys, os, re
from fugaziLiveSeries import *

"""
Reads relative URLs from STDIN and downloads them to out/. All URLs
are relative to http://www.dischord.com.
"""

def download(line):
    url = 'http://www.dischord.com%s' % (line.strip())
    log(url)
    fileName = re.sub(r'.*/', '', url)
    name = os.path.join(OUT_DIR, fileName)
    cmd = 'curl -s %s -o %s' % (url, name)
    #os.system(cmd)

def main(argv):
    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)
    for line in fileinput.input():
        download(line)

if __name__ == '__main__':
    main(sys.argv)
