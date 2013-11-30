#!/local/bin/python

import os, sys, inspect
import cgi
import cgitb; cgitb.enable()
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands

print "Content-type: text/html\n"

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

if 'user' in args:
	user = dbCommands.ReadFromDatabaseCommand("user", 'id='+args['user']).execute()
	if any(user):
		if user['permissions'] == 2 || user['permissions'] == 3
			cmd = dbCommands.DeleteFromDatabaseCommand("Snippet", "id="+str(1+int(args['id'])))
			cmd.execute()

print '<meta http-equiv="refresh" content="0;url=http://web.cs.dal.ca/~coelho/oop/snippets/view.py'" />'