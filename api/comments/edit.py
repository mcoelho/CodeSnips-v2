#!/local/bin/python

import os, sys, inspect, datetime
import cgi
import cgitb; cgitb.enable()
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands
from codesnips.models.Snippet import *
pkg = "~/public_html/oop/jsonpickle"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
import jsonpickle

c = jsonpickle.decode(sys.stdin.read())

print "Content-type: application/json\n"

result = {}
result['success'] = True
result['message'] = "Comment Edited Successfully"

data = ""

if c.id is None:
	result['success'] = False
	result['message'] = "Comment editing failed: you must specify an id"
else:
	data += "lastChanged='" + str(datetime.datetime.now()) +"', "
	if c.message is not None:
		data += "message='" + str(c.message) + "',"

	if c.upvotes is not None:
		data += "upvotes='" + str(c.upvotes) + "',"

	if c.downvotes is not None:
		data += "downvotes='" + str(c.downvotes) + "',"

	data = data[:-1]
	cmd = dbCommands.UpdateOnDatabaseCommand("Comment", data, "id="+str(c.id))
	cmd.execute()

print result
