'''
Created on 2013-11-26
@author: Cameron
'''

class Language(object):
    count = 0
    listOfLanguages = ['JAVA', 'PHP', 'PYTHON']
    
    def __init__(self, versionNumber=0):
        Language.count += 1
        self.version = self.createVersion()
        self.versionNumber = self.versionNumber
        
    def createVersion(self):
        return 'Base class version'
    
    def view(self):
        print "Language name: " + self.name
        print "Creator: " + self.creator
        print "Year introduced: " + self.yearIntroduced
        print "Operating system: " + self.operatingSystem
        print "Version: " + self.versionNumber