#!/local/bin/python

import os, sys, inspect, datetime
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
uid = form.getvalue('uid')

cmd = dbCommands.AddToDatabaseCommand("Snippet", "userId, language, version, title, description, code, lastChanged", "'" + str(uid) + "', '" + str(snippetLang) + "', '" + str(snippetVersion) + "', '" + str(snippetTitle) + "', '" + str(snippetDesc) + "', '" + str(snippetCode) + "', '" + str(datetime.datetime.now()) +"'")
cmd.execute()

print '<meta http-equiv="refresh" content="0;url=http://web.cs.dal.ca/~coelho/oop/snippets/view.py?uid='+uid+'"/>'
