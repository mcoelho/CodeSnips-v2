#!/usr/bin/python



class Permission(object):
    
    def state(self):
        return self.status


class admin(Permission):
    
    def __init__(self):
        self.status = "3"


class normalUser(Permission):
    
    def __init__(self):
        self.status = "1"


class moderator(Permission):
    
    def __init__(self):
        self.status = "2"


class multiState(object):

    def __init__(self, permission):
        self.statuses = {
            "admin": "3",
            "normalUser": "1",
            "moderator": "2"
            }
        self.permission = permission

    def state(self):
        print(self.statuses[self.permission])


if (__name__ == "__main__"):

    # Admin
    stateChecker = multiState("admin")
    stateChecker.state()

    # Normal User
    stateChecker.permission = "normalUser"
    stateChecker.state()

    # Moderator
    stateChecker.permission = "moderator"    
    stateChecker.state()
