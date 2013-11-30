#!/local/bin/python

import os, sys, inspect
import cgi
import cgitb; cgitb.enable()
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands

print "Content-type: text/html\n"

form = cgi.FieldStorage()
comment = form.getvalue('snippetComment')
snippetID = form.getvalue('snippetID')

cmd = dbCommands.AddToDatabaseCommand("Comment", "userId, snippetId, message", "1, '" + str(snippetID) + "', '" + str(comment) + "'")
cmd.execute()
print '<meta http-equiv="refresh" content="0;url=http://web.cs.dal.ca/~coelho/oop/snippets/details.py?id='+str(snippetID)+'"/>'