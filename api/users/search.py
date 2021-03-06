#!/local/bin/python

import os, sys, inspect
import cgi
import cgitb; cgitb.enable()
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands
from codesnips.models.User import *
pkg = "~/public_html/oop/jsonpickle"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
import jsonpickle

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-type: application/json\n"
   
if "id" in args:
	cmd = dbCommands.ReadFromDatabaseCommand("User", "id='"+args['id']+"'")
	rows = cmd.execute()

	if(any(rows)):
		row = rows[0]
		u = User(row['id'], row['name'], row['email'], row['password'], row['dob'], row['bio'], row['specialization'], row['gravatarLink'], row['permissions'])
		print jsonpickle.encode(u)
	else:
		u = NullUser()
		print jsonpickle.encode(u)

elif "permissions" in args:
	cmd = dbCommands.ReadFromDatabaseCommand("User", "permissions='"+args['permissions']+"'")
	rows = cmd.execute()

	if(any(rows)):
		result = []
		for row in rows:
			u = User(row['id'], row['name'], row['email'], row['password'], row['dob'], row['bio'], row['specialization'], row['gravatarLink'], row['permissions'])
			result.append(u)
		print jsonpickle.encode(result)
	else:
		u = NullUser()
		print jsonpickle.encode(u)

else:
	cmd = dbCommands.ReadFromDatabaseCommand("User")
	rows = cmd.execute()

	if(any(rows)):
		result = []
		for row in rows:
			u = User(row['id'], row['name'], row['email'], row['password'], row['dob'], row['bio'], row['specialization'], row['gravatarLink'], row['permissions'])
			result.append(u)
		print jsonpickle.encode(result)
	else:
		u = NullUser()
		print jsonpickle.encode(u)