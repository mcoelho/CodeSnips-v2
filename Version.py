'''
Created on 2013-11-26

@author: Cameron
@summary: Class describing the version of a given language object
'''
class Version(object):
    
    '''Constructor to create the various version objects for each language'''
    def __init__(self, versionNumber, depFunctions, newFunctions, allFunctions, knownBugs):
        self.depFunctions = depFunctions
        self.versionNumber = versionNumber 
        self.newFunctions = newFunctions
        self.allFunctions = allFunctions
        self.knownBugs = knownBugs   