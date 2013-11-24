#!/local/bin/python

import os
import cgi
import cgitb; cgitb.enable()
import sqlite3

con = sqlite3.connect('codesnips.db')

def addToDatabase(table, values):
	with con:
		cur = con.cursor()
		cur.execute("INSERT INTO " + table + " VALUES(" + ")")

def readFromDatabase(table, where=''):
	with con:
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		if where == '':
			cur.execute("SELECT * FROM " + table)
		else:
			cur.execute("SELECT * FROM " + table + " " + where)
		return cur.fetchall()

def updateToDatabase(table, dataToChange, where):
	with con:
		cur = con.cursor()
		cur.execute("UPDATE " + table + " SET " + dataToChange + " WHERE" + where)
		
def deleteFromDatabase(table, where):
	with con:
		cur = con.cursor()
		cur.execute("DELETE FROM " + table + " WHERE " + where)