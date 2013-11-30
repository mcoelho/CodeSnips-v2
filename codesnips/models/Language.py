'''
Created on 2013-11-26
@author: Cameron
'''

class Language(object):
    
    def __init__(self):
        Language.count += 1
        self.version = self.createVersion()

        
        