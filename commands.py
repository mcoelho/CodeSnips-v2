#!/local/bin/python

import cgi
import cgitb; cgitb.enable()
import dataConnection

class AddToDatabaseCommand:
    def __init__(self, table, columns, values):
        self.table = table
        self.columns = columns
        self.values = values

    def execute(self):
        self()

    def __call__(self):
    	dataConnection.addToDatabase(self.table, self.columns, self.values)

class ReadFromDatabaseCommand:
    def __init__(self, table, where=''):
        self.table = table
        self.where = where

    def execute(self):
        return self()

    def __call__(self):
    	return dataConnection.readFromDatabase(self.table, self.where)

class UpdateOnDatabaseCommand:
    def __init__(self, table, dataToChange, where):
        self.table = table
        self.dataToChange = dataToChange
        self.where = where

    def execute(self):
        self()

    def __call__(self):
    	dataConnection.updateOnDatabase(self.table, self.dataToChange, self.where)

class DeleteFromDatabaseCommand:
    def __init__(self, table, where):
        self.table = table
        self.where = where

    def execute(self):
        self()

    def __call__(self):
    	dataConnection.deleteFromDatabase(self.table, self.where)