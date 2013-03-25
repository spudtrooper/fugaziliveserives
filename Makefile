all: fugaziLiveSeries.html

songs.txt:
	python fugaziLiveSongs.py >> $@

urls.txt:
	python fugaziLiveUrls.py >> urls.txt

download: urls.txt
	python downloadAll.py < urls.txt

fugaziLiveSeries.html: songs.txt
	uniq $< | sort | python genHtml.py > $@

clean:
	rm -f *~