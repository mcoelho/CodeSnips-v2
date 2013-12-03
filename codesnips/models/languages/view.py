#!/local/bin/python
import cgi
import cgitb; cgitb.enable()
from AbstractLanguageFactory import AbstractLanguageFactory

def view(languageName, versionNumber):
    
    factory = AbstractLanguageFactory()
    language = factory.createLanguage(languageName, versionNumber)
    
    print "Language name:" + language.name
    print "Creator: " + language.creator
    print "Year introduced:" + language.yearIntroduced
    print "Operating system:" + language.operatingSystem
    print "Version:" + language.versionNumber
    print "Deprecated Functions:" 
    print  language.version.depFunctions
    print "New functions:"
    print  language.version.newFunctions
    print  "All functions:"
    print  language.version.allFunctions

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}
if 'languageName' in args:
    if 'versionNumber' in args:

        print "Content-type: text/html\n"
    
        print "<html><head></head><body>"
        
        print "<h1>View Test</h1>"
        print args['languageName']
        print args['versionNumber']
        view(args['languageName'], args['versionNumber'])

        print "</body></html>"
