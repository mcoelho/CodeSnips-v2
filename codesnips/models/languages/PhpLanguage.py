'''
Created on 2013-11-26

@author: Cameron
'''
from Version import Version
from Language import Language

class PhpLanguage(Language):
    
    def __init__(self, versionNumber):
        super(PhpLanguage, self).__init__()
        self.name = 'PHP'
        self.creator = 'Rasmus Lerdorf'
        self.yearIntroduced = '1995'
        self.operatingSystem = 'Cross-Platform'
        self.versionNumber = versionNumber
        self.version = self.versionFactory(versionNumber)
    
    '''
       creates the different versions of the code depending on the version number indicated, we can replace the statically coded values with the
       approprite database queries to populate the parameter fields for the call to the version constructor.
    '''    
    def versionFactory(self, versionNumber):
        if versionNumber=='1.0':
            depfunctions = ['phpphpfunction1', 'phpfunction2', 'phpfunction3', 'phpfunction4']
            newfunctions = ['phpfunction11', 'phpfunction12']
            allfunctions = ['phpfunction11', 'phpfunction12', 'phpfunction10', 'phpfunction9']
            knownBugs = ['had a single week to develop code']
            return Version(versionNumber, depfunctions, newfunctions, allfunctions, knownBugs);
        elif versionNumber == '2.0':
            depfunctions = ['phpfunction1', 'phpfunction2', 'phpfunction3', 'phpfunction4']
            newfunctions = ['phpfunction11', 'phpfunction12']
            allfunctions = ['phpfunction11', 'phpfunction12', 'phpfunction10', 'phpfunction9']
            knownBugs = ['had a single week to develop code']
            return Version(versionNumber, depfunctions, newfunctions, allfunctions, knownBugs);
        
        elif versionNumber == '3.0':
            depfunctions = ['phpfunction1', 'phpfunction2', 'phpfunction3', 'phpfunction4']
            newfunctions = ['phpfunction11', 'phpfunction12']
            allfunctions = ['phpfunction11', 'phpfunction12', 'phpfunction10', 'phpfunction9']
            knownBugs = ['had a single week to develop code']
            return Version(versionNumber, depfunctions, newfunctions, allfunctions, knownBugs);
        else:
            print 'Invalid version' 
            return