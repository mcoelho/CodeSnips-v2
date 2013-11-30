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
	cmd = dbCommands.ReadFromDatabaseCommand("User", "id="+args['user'])
	users = cmd.execute()
	if any(users):
		if users[0]['permissions'] == 2 or users[0]['permissions'] == 3:
			cmd = dbCommands.DeleteFromDatabaseCommand("Comment", "id="+args['id'])
			cmd.execute()


print '<meta http-equiv="refresh" content="0;url=http://web.cs.dal.ca/~coelho/oop/snippets/details.py?id='+args['snippetId']+'"/>'