import pywikibot, re
from collections import Counter
from HTMLParser import HTMLParser

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
    """TODO: Read a list with duplicated references and groups them
    using the name attribute """
    for i, reference in enumerate(refs):
        name = "name=\"autoname" + str(i+1) + "\""
        longref = u"<ref "+ name + u" >" + reference + u"</ref>"
        shortref = u"<ref "+ name + u" />"
        
        global page
        print u"<ref>" + reference + u"</ref>\n"
        print page.text.find(u"<ref>" + reference + u"</ref>")
        page.text = page.text.replace(u"<ref>" + reference + u"</ref>", shortref)
        page.text = page.text.replace(shortref, longref, 1)
        
        #~ print longref + "\n"
        #~ print shortref + "\n"
        #~ parser.feed(refs[i])
    return page
    

def printRefs(refs):
    """Prints a refs list"""
    
    for reference in enumerate(refs):
        print str(reference) + "\n"

site = pywikibot.Site('es', 'wikipedia')
page = pywikibot.Page(site, 'Usuario:CardoBOT/Taller') #just for testing
resul = re.findall("<ref>(.*?)</ref>", page.text)
#~ printRefs(resul)

dupes = list(resul)
dupes = removeNonDupes(dupes)
page = groupRefs(dupes)

print page.text.encode("utf-8")
    
print str(len(resul)) + " references" 
print str(len(dupes)) + " references to group"




#print page.text
#~ parser.feed(page.text)
