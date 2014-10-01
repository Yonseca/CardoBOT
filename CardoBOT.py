#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
So this is CardoBOT: a bot for the Spanish Wikipedia.

CardoBOT looks for duplicated references and groups them. On this first
version, it just looks if two refs are the same, but reading the whole
reference (this means, including the <ref> tags). If a duplicated reference
is found, we generate an automatic name, and set it as a 'name' attribute
into the tag.

And that's it.
"""
#
# (C) Pywikibot team, 2006-2014
#
# Distributed under the terms of the MIT license.
#
__version__ = '$Id: 99f83f10f39545a8c0f82a62a702803c5510b86c $'
#

import pywikibot, re
from pywikibot import pagegenerators
from pywikibot import i18n

# This is required for the text that is shown when you run this script
# with the parameter -help.
docuReplacements = {
    '&params;': pagegenerators.parameterHelp
}

class Reference:
    """ Saves all data from a reference """
    def __init__(self, name, group, data):
        self.name = name
        self.group = group
        self.data = data

class BasicBot:

    """An incomplete sample bot."""

    # Edit summary message that should be used is placed on /i18n subdirectory.
    # The file containing these messages should have the same name as the caller
    # script (i.e. basic.py in this case)

    def __init__(self, generator, dry):
        """
        Constructor.

        Parameters:
            @param generator: The page generator that determines on which pages
                              to work.
            @type generator: generator.
            @param dry: If True, doesn't do any real changes, but only shows
                        what would have been changed.
            @type dry: boolean.
        """
        self.generator = generator
        self.dry = dry

        # Set the edit summary message
        site = pywikibot.Site()
        #self.summary = i18n.twtranslate(site, 'basic-changing')
        self.summary = u'¡[[Usuario:CardoBOT|CardoBOT]] en pruebas! Eliminando referencias duplicadas.'


    def run(self):
        """ Process each page from the generator. """
        for page in self.generator:
            self.treat(page)

    def removeNonDupes(self, refs):
        """Returns a list containing all distinct duplicated references"""
        
        # If a reference appears more than once, delete it
        for reference in refs[:]:
            if (refs.count(reference) <= 1):
                print  "Eliminado (" + str(refs.count(reference)) + "): " + reference.encode("utf-8") 
                refs.remove(reference)
            else:
                print  "Manteniendo (" + str(refs.count(reference)) + "): " + reference.encode("utf-8")

        # Transform the list into a set, and then back to a list.
        # This will remove duplicities.
        return list(set(refs))
        
    def groupRefs(self, refs, text):
        """ Groups the references by setting a name and replacing long with
        short references, excepting the first one. """
        for i, reference in enumerate(refs):
            name = "name=\"autoname" + str(i+1) + "\""
            longref = u"<ref "+ name + u" >" + reference + u"</ref>"
            shortref = u"<ref "+ name + u" />"
            
            #print u"<ref>" + reference.encode("utf-8") + u"</ref>\n"
            print text.find(u"<ref>" + reference + u"</ref>")
            text = text.replace(u"<ref>" + reference + u"</ref>", shortref)
            text = text.replace(shortref, longref, 1)
        return text

    def printRefs(self, refs):
        """Prints a refs list"""
        
        for reference in refs[:]:
            print str(reference) + "\n"

    def treat(self, page):
        """ Load the given page, does some changes, and saves it. """
        text = self.load(page)
        if not text:
            return
        
        resul = re.findall("<ref>(.*?)</ref>", text)
        print str(len(resul)) + " references" 
        dupes = self.removeNonDupes(list(resul))
        print str(len(dupes)) + " references to group"
        text = self.groupRefs(dupes, text)
        #print page.text.encode("utf-8")

        # Done!
        if not self.save(text, page, self.summary):
            pywikibot.output(u'Page %s not saved.' % page.title(asLink=True))

    def load(self, page):
        """ Load the text of the given page. """
        try:
            # Load the page
            text = page.get()
        except pywikibot.NoPage:
            pywikibot.output(u"Page %s does not exist; skipping."
                             % page.title(asLink=True))
        except pywikibot.IsRedirectPage:
            pywikibot.output(u"Page %s is a redirect; skipping."
                             % page.title(asLink=True))
        else:
            return text
        return None

    def save(self, text, page, comment=None, minorEdit=True,
             botflag=True):
        """ Update the given page with new text. """
        # only save if something was changed
        if text != page.get():
            # Show the title of the page we're working on.
            # Highlight the title in purple.
            pywikibot.output(u"\n\n>>> \03{lightpurple}%s\03{default} <<<"
                             % page.title())
            # show what was changed
            pywikibot.showDiff(page.get(), text)
            pywikibot.output(u'Comment: %s' % comment)
            if not self.dry:
                choice = pywikibot.inputChoice(
                    u'Do you want to accept these changes?',
                    ['Yes', 'No'], ['y', 'N'], 'N')
                if choice == 'y':
                    try:
                        page.text = text
                        # Save the page
                        page.save(comment=comment or self.comment,
                                  minor=minorEdit, botflag=botflag)
                    except pywikibot.LockedPage:
                        pywikibot.output(u"Page %s is locked; skipping."
                                         % page.title(asLink=True))
                    except pywikibot.EditConflict:
                        pywikibot.output(
                            u'Skipping %s because of edit conflict'
                            % (page.title()))
                    except pywikibot.SpamfilterError as error:
                        pywikibot.output(
                            u'Cannot change %s because of spam blacklist entry %s'
                            % (page.title(), error.url))
                    else:
                        return True
        return False


def main():
    """ Process command line arguments and invoke BasicBot. """
    # Process global arguments to determine desired site
    local_args = pywikibot.handleArgs()

    # This factory is responsible for processing command line arguments
    # that are also used by other scripts and that determine on which pages
    # to work on.
    genFactory = pagegenerators.GeneratorFactory()
    # The generator gives the pages that should be worked upon.
    gen = None
    # If dry is True, doesn't do any real changes, but only show
    # what would have been changed.
    dry = False

    # Parse command line arguments
    for arg in local_args:
        if arg.startswith("-dry"):
            dry = True
        else:
            genFactory.handleArg(arg)

    if not gen:
        gen = genFactory.getCombinedGenerator()
    if gen:
        # The preloading generator is responsible for downloading multiple
        # pages from the wiki simultaneously.
        gen = pagegenerators.PreloadingGenerator(gen)
        bot = BasicBot(gen, dry)
        bot.run()
    else:
        pywikibot.showHelp()

if __name__ == "__main__":
    main()
