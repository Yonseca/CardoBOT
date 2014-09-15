import pywikibot, re
#~ from HTMLParser import HTMLParser

#save = 0

#class MyHTMLParser(HTMLParser):

    ##save = 0
    #i = 0
    #refs = []

    #def handle_starttag(self, tag, attrs):
        #if tag in ['ref']:
            ##print "Encountered a start tag:", tag
            #global save, refs, i
            #save = 1
            #for attr in attrs:
                #print "atributo: ", attr

    #def handle_endtag(self, tag):
        ##print "Encountered an end tag :", tag
        #global save
        #save = 0

    #def handle_data(self, data):
        #global save
    #savestatus = save
        ##if savestatus == 1:
            ##print "Encountered some data  :", data


#~ parser = MyHTMLParser()
site = pywikibot.Site('es', 'wikipedia')
page = pywikibot.Page(site, 'Amaral')
resul = re.findall("<ref(.*?)</ref>", page.text)
for reference in resul:
    reference = "<ref" + reference + "</ref>" + "\n"
    print reference

dupes = []
repetitions = 0
for ref1 in resul:
    for ref2 in resul:
        if (ref1 == ref2):
            repetitions = repetitions + 1
    if (repetitions == 1):
        #~ print "Quitado:" + resul.pop(resul.index(ref2)) + "\n"
        repetitions = 0



#print page.text
#~ parser.feed(page.text)
