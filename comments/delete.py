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

uid = args['uid']
cmd = dbCommands.ReadFromDatabaseCommand("Comment", "id="+args['id'])
rows = cmd.execute()



if any(rows):
	cmd = dbCommands.DeleteFromDatabaseCommand("Comment", "id="+args['id'])
	cmd.execute()
		


print '<meta http-equiv="refresh" content="0;url=http://web.cs.dal.ca/~coelho/oop/snippets/details1.py?id='+args['snippetId']+'&uid='+uid+'"/>'