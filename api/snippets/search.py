#!/local/bin/python

import os, sys, inspect
import cgi
import cgitb; cgitb.enable()
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands
from codesnips.models.Snippet import *
pkg = "~/public_html/oop/jsonpickle"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
import jsonpickle

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-type: application/json\n"
   
if "id" in args:
	cmd = dbCommands.ReadFromDatabaseCommand("Snippet", "id='"+args['id']+"'")
	rows = cmd.execute()

	if(any(rows)):
		row = rows[0]
		u = Snippet(row['id'], row['userId'], row['upvotes'], row['downvotes'], row['lastChanged'], row['title'], row['description'], row['code'], row['language'], row['version'])
		print jsonpickle.encode(u)
	else:
		u = NullUser()
		print jsonpickle.encode(u)

elif "userId" in args:
	cmd = dbCommands.ReadFromDatabaseCommand("Snippet", "userId='"+args['userId']+"'")
	rows = cmd.execute()

	if(any(rows)):
		result = []
		for row in rows:
			u = Snippet(row['id'], row['userId'], row['upvotes'], row['downvotes'], row['lastChanged'], row['title'], row['description'], row['code'], row['language'], row['version'])
			result.append(u)
		print jsonpickle.encode(result)
	else:
		u = NullUser()
		print jsonpickle.encode(u)
elif "language" in args:
	cmd = dbCommands.ReadFromDatabaseCommand("Snippet", "language='"+args['language']+"'")
	rows = cmd.execute()

	if(any(rows)):
		result = []
		for row in rows:
			u = Snippet(row['id'], row['userId'], row['upvotes'], row['downvotes'], row['lastChanged'], row['title'], row['description'], row['code'], row['language'], row['version'])
			result.append(u)
		print jsonpickle.encode(result)
	else:
		u = NullUser()
		print jsonpickle.encode(u)

else:
	cmd = dbCommands.ReadFromDatabaseCommand("Snippet")
	rows = cmd.execute()

	if(any(rows)):
		result = []
		for row in rows:
			u = Snippet(row['id'], row['userId'], row['upvotes'], row['downvotes'], row['lastChanged'], row['title'], row['description'], row['code'], row['language'], row['version'])
			result.append(u)
		print jsonpickle.encode(result)
	else:
		u = NullUser()
		print jsonpickle.encode(u)