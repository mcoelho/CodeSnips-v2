#!/local/bin/python

import os, sys, inspect
import cgi
import cgitb; cgitb.enable()
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands

print "Content-type: text/html\n"

form = cgi.FieldStorage()
snippetTitle = form.getvalue('snippetTitle')
snippetDesc = form.getvalue('snippetDesc')
snippetLang = form.getvalue('snippetLang')
snippetVersion = form.getvalue('snippetVersion')
snippetCode = form.getvalue('snippetCode')

cmd = dbCommands.AddToDatabaseCommand("Snippet", "userId, language, version, title, description, code", "1, '" + str(snippetLang) + "', '" + str(snippetVersion) + "', '" + str(snippetTitle) + "', '" + str(snippetDesc) + "', '" + str(snippetCode) + "'")
cmd.execute()
