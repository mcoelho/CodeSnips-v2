#!/local/bin/python

import cgi
import cgitb; cgitb.enable()
import dbConnection

class AddToDatabaseCommand:
    def __init__(self, table, columns, values):
        self.table = table
        self.columns = columns
        self.values = values

    def execute(self):
        self()

    def __call__(self):
    	dbConnection.addToDatabase(self.table, self.columns, self.values)

class ReadFromDatabaseCommand:
    def __init__(self, table, where=''):
        self.table = table
        self.where = where

    def execute(self):
        return self()

    def __call__(self):
    	return dbConnection.readFromDatabase(self.table, self.where)

class UpdateOnDatabaseCommand:
    def __init__(self, table, dataToChange, where):
        self.table = table
        self.dataToChange = dataToChange
        self.where = where

    def execute(self):
        self()

    def __call__(self):
    	dbConnection.updateOnDatabase(self.table, self.dataToChange, self.where)

class DeleteFromDatabaseCommand:
    def __init__(self, table, where):
        self.table = table
        self.where = where

    def execute(self):
        self()

    def __call__(self):
    	dbConnection.deleteFromDatabase(self.table, self.where)