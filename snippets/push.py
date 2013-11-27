#!/local/bin/python

import os
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands
#from codesnips.models.Post import *
#from codesnips.models.Snippet import *

form = cgi.FieldStorage()

snippetTitle = form.getvalue('snippetTitle')
snippetDesc = form.getvalue('snippetDesc')
snippetLang = form.getvalue('snippetLang')
snippetCode = form.getvalue('snippetCode')
snippetVersion = form.getvalue('snippetVersion')

cmd = dbCommands.AddToDatabaseCommand("Snippet", "userId, language, version, title, description, code","1,'" + snippetLang + "','" + snippetVersion + "','" + snippetTitle + "','" + snippetDesc + "','" + snippetCode + "'")
cmd.execute() 

print "Content-type: text/html\n"
print "success"
