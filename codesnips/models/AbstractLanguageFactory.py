


from JavaLanguage import JavaLanguage
from PhpLanguage import PhpLanguage
from PythonLanguage import PythonLanguage

class AbstractLanguageFactory(object):
    count = 0
    def __init__(self):
        AbstractLanguageFactory.count += 1
            
    def createLanguage(self, languageName, versionNumber):
        languageName = languageName.upper().strip()
        if(languageName == 'JAVA'):
            return JavaLanguage(versionNumber)
        elif(languageName == 'PHP'):
            return PhpLanguage(versionNumber)
        elif(languageName == 'PYTHON'):
            return PythonLanguage(versionNumber)
        else:
            return 'The language entered is not recognized'
