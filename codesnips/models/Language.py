'''
Created on 2013-11-26
@author: Cameron
'''

class Language(object):
    count = 0
    listOfLanguages = ['JAVA', 'PHP', 'PYTHON']
    
    def __init__(self):
        Language.count += 1
        