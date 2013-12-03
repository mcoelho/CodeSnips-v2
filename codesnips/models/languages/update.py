import os, sys, inspect
from dbCommands import *

import cgi
import cgitb; cgitb.enable()

def updateDepFunctions(languageName, version, newData):
    UpdateOnDatabaseCommand('Language', ['depFunctions='newData], 'version='+version+'name='+languageName)

def updateAllFunctions(languageName, version, newData):
    UpdateOnDatabaseCommand('Language', ['allFunctions='newData], 'version='+version+'name='+languageName)

def updateNewFunctions(languageName, version, newData): 
    UpdateOnDatabaseCommand('Language', ['newFunctions='newData], 'version='+version+'name='+languageName)
                
url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}
    
    if 'newData' in args:
        data = args['newData']
        if 'versionNumber' in args:
            version = args['versionNumber']
            if 'languageName' in args:
                language = args['language']
                if 'type' in args:
                    if args['type'] == dep
                        updateDepFunctions(args['language'], args['version'], args[data])
                    elif args['type'] == all
                        updateAllFunctions(args['language'], args['version'], args[data])
                    elif args['type'] == new
                        updateNewFunctions(args['language'], args['version'], args[data])