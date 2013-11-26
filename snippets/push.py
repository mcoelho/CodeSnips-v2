#!/local/bin/python

import os
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys

form = cgi.FieldStorage();

snippetTitle = form.getvalue('snippetTitle')
snippetDesc = form.getvalue('snippetDesc')
snippetLang = form.getvalue('snippetLang')
snippetCode = form.getvalue('snippetCode')

cmd = dbCommands.AddToDatabaseCommand("Snippet", "language, name, description, code" )
rows = cmd.execute()
