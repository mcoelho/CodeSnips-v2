#!/local/bin/python

import os, sys, inspect, datetime
import cgi
import cgitb; cgitb.enable()
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands

print "Content-type: text/html\n"

form = cgi.FieldStorage()
snippetId = form.getvalue('sId')
snippetTitle = form.getvalue('snippetTitle')
snippetDesc = form.getvalue('snippetDesc')
snippetLang = form.getvalue('snippetLang')
snippetVersion = form.getvalue('snippetVersion')
snippetCode = form.getvalue('snippetCode')

cmd = dbCommands.UpdateOnDatabaseCommand("Snippet", "language='"+snippetLang+"', version='"+snippetVersion+"', title='"+snippetTitle+"', description='"+snippetDesc+"', code='"+snippetCode+"', lastChanged='" + str(datetime.datetime.now()) +"'", "id="+snippetId)
cmd.execute()

print '<meta http-equiv="refresh" content="0;url=http://web.cs.dal.ca/~coelho/oop/snippets/view.py" />'