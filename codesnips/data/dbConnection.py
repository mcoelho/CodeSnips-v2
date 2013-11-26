#!/local/bin/python

import cgi
import cgitb; cgitb.enable()
import sqlite3, os

con = sqlite3.connect(os.path.dirname(os.path.expanduser("~/public_html/oop/codesnips/data/"))+'codesnips.db')

def addToDatabase(table, columns, values):
	with con:
		cur = con.cursor()
		cur.execute("INSERT INTO " + table + "(" + columns + ") VALUES(" + values + ")")

def readFromDatabase(table, where):
	with con:
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		if where == '':
			cur.execute("SELECT * FROM " + table)
		else:
			cur.execute("SELECT * FROM " + table + " WHERE " + where)
		return cur.fetchall()

def updateOnDatabase(table, dataToChange, where):
	with con:
		cur = con.cursor()
		cur.execute("UPDATE " + table + " SET " + dataToChange + " WHERE " + where)

def deleteFromDatabase(table, where):
	with con:
		cur = con.cursor()
		cur.execute("DELETE FROM " + table + " WHERE " + where)