'''
Created on 2013-11-26

@author: Cameron Sieffert
@return Array of int values indicating the start position in the string of each deprecated function found.
'''

class DeprecatedFxScanner(object):
    
    @staticmethod
    def scanSnippet(snippet, depFunctions):
        i = 0;
        result = []
        for i in depFunctions:
            found = snippet.find(i)
            beginning = found+1
            end = len(snippet)
            while(found != -1):
                result.append(found)
                found = snippet.find(i, beginning, end)
                beginning = found+1
        return result