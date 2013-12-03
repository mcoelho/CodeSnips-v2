#!/local/bin/python

import os, sys, inspect, datetime
import cgi
import cgitb; cgitb.enable()
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands
from codesnips.models.Comment import *
pkg = "~/public_html/oop/jsonpickle"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
import jsonpickle

c = jsonpickle.decode(sys.stdin.read())

print "Content-type: application/json\n"

result = {}
result['success'] = True
result['message'] = "Snippet Added Successfully"

columns = "lastChanged, "
values = "'"+str(datetime.datetime.now())+"', "

if c.userId is not None:
	columns += "userId"
	values += "'" + str(c.userId) + "'"
else:
	result['success'] = False
	result['message'] = "comment creation failed: you must specify a user id"

if c.snippetId is not None:
	columns += ", snippetId"
	values += ", '" + str(c.snippetId) + "'"
else:
	result['success'] = False
	result['message'] = "Comment creation failed: you must specify a snippet id"

if c.message is not None:
	columns += ", message"
	values += ", '" + c.message + "'"
else:
	result['success'] = False
	result['message'] = "Comment creation failed: you must specify a message"

if result['success'] is True:
	cmd = dbCommands.AddToDatabaseCommand("Comment", columns, values)
	cmd.execute()

print result
