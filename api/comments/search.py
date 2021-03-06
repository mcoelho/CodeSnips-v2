#!/local/bin/python

import os, sys, inspect
import cgi
import cgitb; cgitb.enable()
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands
from codesnips.models.Comment import *
pkg = "~/public_html/oop/jsonpickle"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
import jsonpickle

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-type: application/json\n"

if "id" in args:
	cmd = dbCommands.ReadFromDatabaseCommand("Comment", "id='"+args['id']+"'")
	rows = cmd.execute()

	if(any(rows)):
		row = rows[0]
		u = Comment(row['id'], row['userId'], row['upvotes'], row['downvotes'], row['lastChanged'], row['snippetId'], row['message'])
		print jsonpickle.encode(u)
	else:
		u = NullComment()
		print jsonpickle.encode(u)

elif "snippetId" in args:
	cmd = dbCommands.ReadFromDatabaseCommand("Comment", "snippetId='"+args['snippetId']+"'")
	rows = cmd.execute()

	if(any(rows)):
		result = []
		for row in rows:
			u = Comment(row['id'], row['userId'], row['upvotes'], row['downvotes'], row['lastChanged'], row['snippetId'], row['message'])
			result.append(u)
		print jsonpickle.encode(result)
	else:
		u = NullComment()
		print jsonpickle.encode(u)

else:
	cmd = dbCommands.ReadFromDatabaseCommand("Comment")
	rows = cmd.execute()

	if(any(rows)):
		result = []
		for row in rows:
			u = Comment(row['id'], row['userId'], row['upvotes'], row['downvotes'], row['lastChanged'], row['snippetId'], row['message'])
			result.append(u)
		print jsonpickle.encode(result)
	else:
		u = NullComment()
		print jsonpickle.encode(u)