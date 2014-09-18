import pywikibot, re
from collections import Counter
#~ from HTMLParser import HTMLParser

#save = 0

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag in ['ref']:
            print "Encountered a start tag:", tag
            for attr in attrs:
                #print "atributo: ", attr

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
        global save

    def handle_data(self, data):


parser = MyHTMLParser()

def removeNonDupes(refs):
    """Returns a set containing all distinct duplicated references"""
    
    for i, reference in enumerate(refs):
        if (refs.count(reference) <= 1): #if it appears more than once...
            del refs[i]
    return set(refs)
    
def groupRefs(refs):
    """TODO: Read a list with duplicated references and groups them using
    the name attribute """
    for i, reference in refs:
        longref = u"<ref>" + reference + u"</ref>"
        parser.treat(longref)
    

def printRefs(refs):
    """Prints a refs list"""
    
    for reference in enumerate(refs):
        print str(reference) + "\n"

site = pywikibot.Site('es', 'wikipedia')
page = pywikibot.Page(site, 'Amaral') #just for testing
resul = re.findall("<ref(.*?)</ref>", page.text)
print str(len(resul)) + " references"
#~ printRefs(resul)

# Removes non-duplicated references and converts the result into a set
# This will show all distinct duplicated references.
dupes = removeNonDupes(resul)

groupRefs(dupes)

    
printRefs(dupes)
print str(len(dupes)) + " references to group"




#print page.text
#~ parser.feed(page.text)
