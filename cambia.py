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

def removeNonDupes(refs):
    """Returns a references lists w/o non-duplicated elements"""
    
    repetitions = 0
    for ref1 in refs:
        for ref2 in refs:
            if (ref1 == ref2):
                repetitions = repetitions + 1
        if (repetitions == 1):
            print str(repetitions) + " apariciones. Quitado:" + \
                refs.pop(resul.index(ref2)) + "\n"
        else:
            print str(repetitions) + " apariciones. Manteniendo:" + \
                ref2 + "\n"
        repetitions = 0
    return refs

site = pywikibot.Site('es', 'wikipedia')
page = pywikibot.Page(site, 'Amaral')
resul = re.findall("<ref(.*?)</ref>", page.text)
print len(resul)
for i, reference in enumerate(resul):
    if (resul.count(reference) > 1):
        resul[i] = u"<ref" + reference + u"</ref>" + "\n"
    else:
        resul.remove(reference)

dupes = []
print len(resul)
resul = removeNonDupes(resul)
print len(resul)

#print page.text
#~ parser.feed(page.text)
