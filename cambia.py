import pywikibot, re
from collections import Counter
from HTMLParser import HTMLParser

#save = 0

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        name = ''
        group = ''
        if tag in ['ref']:
            print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
        global save

    #def handle_data(self, data):


parser = MyHTMLParser()

def removeNonDupes(refs):
    """Returns a list containing all distinct duplicated references"""
    
    # If a reference appears more than once, delete it
    for i, reference in enumerate(refs):
        if (refs.count(refs[i]) <= 1):
            print  "Eliminado: " + refs[i].encode("utf-8")
        del refs[i]

    # Transform the list into a set, and then back to a list.
    # This will remove duplicities.
    return list(set(refs))
    
def groupRefs(refs):
    """TODO: Read a list with duplicated references and groups them using
    the name attribute """
    for i, reference in enumerate(refs):
        name = "name=\"autoname" + str(i+1) + "\""
        refs[i] = u"<ref "+ name + " >" + reference + u"</ref>"
        print refs[i].encode("utf-8")
        parser.feed(refs[i])
    

def printRefs(refs):
    """Prints a refs list"""
    
    for reference in enumerate(refs):
        print str(reference) + "\n"

site = pywikibot.Site('es', 'wikipedia')
page = pywikibot.Page(site, 'Barack Obama') #just for testing
resul = re.findall("<ref>(.*?)</ref>", page.text)
#~ printRefs(resul)

dupes = list(resul)
dupes = removeNonDupes(dupes)
groupRefs(dupes)
    
print str(len(resul)) + " references" 
print str(len(dupes)) + " references to group"




#print page.text
#~ parser.feed(page.text)
