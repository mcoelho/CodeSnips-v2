'''
@author: Yuming
'''


class StrategyUser:
    """ Inteface / Abstract Class concept for readability. """

    def find(self, user):
        # explicitly set it up so this can't be called directly
        raise NotImplementedError('Exception raised, StrategyUser is supposed to be an interface / abstract class!')

class StrategyUserID(StrategyUser):
    ''' Locates users in userID'''

    def find(self, user):
        # in reality, query ID API for user path
        return "User found, and user can use UserID to log in: " + user


class StrategyUserEmail(StrategyUser):
    ''' Locates users in Email. '''
    def find(self, user):
        #in reality, query Email for user path
        return "User found, and user can use Email to log in: " + user
       
    
if __name__ == "__main__" :
    finderBase = StrategyUser()
    finderID = StrategyUserID()
    finderEmail = StrategyUserEmail()

    try:
        print finderBase.find('Yuming')
    except NotImplementedError as e:
        print "The following exception was expected:"
        print e
        

    print finderID.find('Yuming')
    print finderID.find('Macheal')
    print finderEmail.find('Allen@cs.dal.ca')
    print finderEmail.find('Jack@cs.dal.ca')  