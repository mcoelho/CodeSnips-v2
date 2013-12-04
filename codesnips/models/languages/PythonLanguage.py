'''
Created on 2013-11-26

@author: Cameron
'''
import os, sys, inspect
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands 
from Version import Version
from Language import Language

class PythonLanguage(Language):
    
    def __init__(self, versionNumber):
        super(PythonLanguage, self).__init__()
        self.name = 'Python'
        self.creator = 'Guido van Rossum'
        self.yearIntroduced = '1991'
        self.operatingSystem = 'Cross-Platform'
        self.versionNumber = versionNumber
        self.version = self.versionFactory(self.versionNumber)
    
    '''
       creates the different versions of the code depending on the version number indicated, we can replace the statically coded values with the
       approprite database queries to populate the parameter fields for the call to the version constructor.
    '''    
    def versionFactory(self, versionNumber):
        if versionNumber=='1.0':
            cmd = dbCommands.ReadFromDatabaseCommand('Language', "name='PYTHON' AND version='1.0'")
            rows = cmd.execute()
            row = rows[0]
            depFunctions = row['depFunctions']
            newFunctions = row['newFunctions']
            allFunctions = row['allFunctions']
            knownBugs = row['bugs']
            return Version(versionNumber, depFunctions, newFunctions, allFunctions, knownBugs);
        elif versionNumber == '2.0':
            cmd = dbCommands.ReadFromDatabaseCommand('Language', "name='PYTHON' AND version='2.0'")
            rows = cmd.execute()
            row = rows[0]
            depFunctions = row['depFunctions']
            newFunctions = row['newFunctions']
            allFunctions = row['allFunctions']
            knownBugs = row['bugs']
            return Version(versionNumber, depFunctions, newFunctions, allFunctions, knownBugs);
        
        elif versionNumber == '3.0':
            cmd = dbCommands.ReadFromDatabaseCommand('Language', "name='PYTHON' AND version='3.0'")
            rows = cmd.execute()
            row = rows[0]
            depFunctions = row['depFunctions']
            newFunctions = row['newFunctions']
            allFunctions = row['allFunctions']
            knownBugs = row['bugs']
            return Version(versionNumber, depFunctions, newFunctions, allFunctions, knownBugs);
        else:
            print 'Invalid version' 
            return