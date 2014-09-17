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
    for i, reference in enumerate(refs):
        if (refs.count(reference) > 1): #if it appears more than once...
            refs[i] = u"<ref" + reference + u"</ref>" + "\n"
            print str(refs.count(reference)) + ":" + refs[i]
        else: 
            refs.remove(reference)
    return refs

site = pywikibot.Site('es', 'wikipedia')
page = pywikibot.Page(site, 'Amaral') #just for testing
resul = re.findall("<ref(.*?)</ref>", page.text)

print str(len(resul)) + " referencias"
dupes = []
print str(len(resul)) + " referencias"
resul = removeNonDupes(resul)
print str(len(resul)) + " referencias"

#print page.text
#~ parser.feed(page.text)
