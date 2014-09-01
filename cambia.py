import pywikibot, re
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):

    save = 0
    i = 0
    refs = []

    def handle_starttag(self, tag, attrs):
        if tag in ['ref']:
            print "Encountered a start tag:", tag
            global save, refs, i
            save = 1

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
        global save
        save = 0

    def handle_data(self, data):
        global save
        if save == 1:
            print "Encountered some data  :", data


parser = MyHTMLParser()
site = pywikibot.Site('es', 'wikipedia')
page = pywikibot.Page(site, 'Amaral')
#print page.text
parser.feed(page.text)
