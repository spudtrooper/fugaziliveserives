= Overview

Reads shows from http://www.dischord.com//fugazi_live_series and
creates a grid showing the songs in every show. The Makefile describes
things but basically...

- Create list of urls:

	% python fugaizeLiveUrls.py # make urls.txt
	
- Download all the urls in urls.txt:

	% python downloadAll.py < urls.txt
	
- Create list of songs from downloaded files:

	% python fugaziLiveSongs.py
	
- Create html file 'fugaziLiveSeries.html':

	% uniq songs.txt | sort | python genHtml.py > fugaziLiveSeries.html
	
= Example

http://jeffpalm.com/fugaziLiveSeries.html
