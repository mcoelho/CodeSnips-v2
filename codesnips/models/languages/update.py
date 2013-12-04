import os, sys, inspect
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands
import cgi
import cgitb; cgitb.enable()

def updateDepFunctions(languageName, version, newData):
    cmd = dbCommands.UpdateOnDatabaseCommand('Language', 'depFunctions='+newData, 'version='+version+' AND name='+languageName)
    cmd.execute() 
def updateAllFunctions(languageName, version, newData):
    cmd= dbCommands.UpdateOnDatabaseCommand('Language', 'allFunctions='+newData, 'version='+version+' AND name='+languageName)
    cmd.execute() 
def updateNewFunctions(languageName, version, newData): 
    cmd= dbCommands.UpdateOnDatabaseCommand('Language', 'newFunctions='+newData, 'version='+version+' AND name='+languageName)
    cmd.execute()
def updateBugsFunction(languageName, version, newData):
    cmd= dbCommands.UpdateOnDatabaseCommand('Language', 'bugs='+newData, 'version='+version+' AND name='+languageName)
    cmd.execute()           
url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}
if 'newData' in args:
    data = args['newData']
    print data
    if 'versionNumber' in args:
        version = args['versionNumber']
        print version
        if 'languageName' in args:
            language = args['languageName']
            print language
            if 'type' in args:
                if args['type'] == 'dep':
                    updateDepFunctions(language, version, data)
                elif args['type'] == 'all':
                    print 'we enter all'
                    updateAllFunctions(language, version, data)
                elif args['type'] == 'new':
                    updateNewFunctions(language, version, data)
                elif args['type'] == 'bugs':
                    updateBugsFunction(language, version, data)