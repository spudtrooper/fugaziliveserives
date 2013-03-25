import fileinput, sys

"""
Reads from STDIN and outputs all the songs.
"""

def main(argv):
    for line in fileinput.input():
        line = line.strip()
        parts = line.split(SEP)
        fileName = parts.pop(0)
        title = parts.pop(0)
        for song in parts:
            print song

if __name__ == '__main__':
    main(sys.argv)
