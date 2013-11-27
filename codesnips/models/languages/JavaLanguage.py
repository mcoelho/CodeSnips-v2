'''
Created on 2013-11-26

@author: Cameron
'''

from Version import Version
from Language import Language

class JavaLanguage(Language):
    
    def __init__(self, versionNumber):
        super(JavaLanguage, self).__init__()
        self.name = 'Java'
        self.creator = 'James Gosling'
        self.yearIntroduced = '1995'
        self.operatingSystem = 'Cross-Platform'
        self.versioNumber = self.versionNumber
        self.version = self.versionFactory(versionNumber)
    '''
       creates the different versions of the code depending on the version number indicated, we can replace the statically coded values with the
       approprite database queries to populate the parameter fields for the call to the version constructor.
    '''    
    def versionFactory(self, versionNumber):
        if versionNumber=='1.0':
            depFunctions = ['javaFunction1', 'javaFunction2', 'javaFunction3', 'javaFunction4']
            newFunctions = ['javaFunction11', 'javaFunction12']
            allFunctions = ['javaFunction11', 'javaFunction12', 'javaFunction10', 'javaFunction 9']
            knownBugs = ['had a single week to develop code']
            return Version(versionNumber, depFunctions, newFunctions, allFunctions, knownBugs);
        elif versionNumber == '2.0':
            depFunctions = ['javaFunction1', 'javaFunction2', 'javaFunction3', 'javaFunction4']
            newFunctions = ['javaFunction11', 'javaFunction12']
            allFunctions = ['javaFunction11', 'javaFunction12', 'javaFunction10', 'javaFunction 9']
            knownBugs = ['had a single week to develop code']
            return Version(versionNumber, depFunctions, newFunctions, allFunctions, knownBugs);
        
        elif versionNumber == '3.0':
            depFunctions = ['javaFunction1', 'javaFunction2', 'javaFunction3', 'javaFunction4']
            newFunctions = ['javaFunction11', 'javaFunction12']
            allFunctions = ['javaFunction11', 'javaFunction12', 'javaFunction10', 'javaFunction 9']
            knownBugs = ['had a single week to develop code']
            return Version(versionNumber, depFunctions, newFunctions, allFunctions, knownBugs);
        else:
            print 'Invalid version' 
            return