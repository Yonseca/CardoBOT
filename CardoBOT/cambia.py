import pywikibot, re
from HTMLParser import HTMLParser

save = 0
i = 0
refs = []

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
    	global save, refs
        if tag in ['ref']:
            print "Encountered a start tag:", tag
            save = 1

    def handle_endtag(self, tag):
    	global save, refs
        print "Encountered an end tag :", tag
        save = 0

    def handle_data(self, data):
    	#global save, i, refs
        if save == 1:
            print "Encountered some data  :", data


parser = MyHTMLParser()
site = pywikibot.Site('es', 'wikipedia')
page = pywikibot.Page(site, 'Amaral')
#print page.text
parser.feed(page.text)

