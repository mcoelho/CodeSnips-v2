'''
Created on 2013-11-26

@author: Cameron
'''
from Version import Version
from Language import Language

class PythonLanguage(Language):
    
    def __init__(self, versionNumber):
        super(PythonLanguage, self).__init__()
        self.name = 'Python'
        self.creator = 'Guido van Rossum'
        self.yearIntroduced = '1991'
        self.operatingSystem = 'Cross-Platform'
        self.versionNumber = self.versionNumber
        self.version = self.versionFactory(versionNumber)
    
    '''
       creates the different versions of the code depending on the version number indicated, we can replace the statically coded values with the
       approprite database queries to populate the parameter fields for the call to the version constructor.
    '''    
    def versionFactory(self, versionNumber):
        if versionNumber=='1.0':
            depFunctions = ['pyFunction1', 'pyFunction2', 'pyFunction3', 'pyFunction4']
            newFunctions = ['pyFunction11', 'pyFunction12']
            allFunctions = ['pyFunction11', 'pyFunction12', 'pyFunction10', 'pyFunction 9']
            knownBugs = ['had a single week to develop code']
            return Version(versionNumber, depFunctions, newFunctions, allFunctions, knownBugs);
        elif versionNumber == '2.0':
            depFunctions = ['pyFunction1', 'pyFunction2', 'pyFunction3', 'pyFunction4']
            newFunctions = ['pyFunction11', 'pyFunction12']
            allFunctions = ['pyFunction11', 'pyFunction12', 'pyFunction10', 'pyFunction 9']
            knownBugs = ['had a single week to develop code']
            return Version(versionNumber, depFunctions, newFunctions, allFunctions, knownBugs);
        
        elif versionNumber == '3.0':
            depFunctions = ['pyFunction1', 'pyFunction2', 'pyFunction3', 'pyFunction4']
            newFunctions = ['pyFunction11', 'pyFunction12']
            allFunctions = ['pyFunction11', 'pyFunction12', 'pyFunction10', 'pyFunction 9']
            knownBugs = ['had a single week to develop code']
            return Version(versionNumber, depFunctions, newFunctions, allFunctions, knownBugs);
        else:
            print 'Invalid version' 
            return