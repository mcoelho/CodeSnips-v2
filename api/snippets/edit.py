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

s = jsonpickle.decode(sys.stdin.read())

print "Content-type: application/json\n"

result = {}
result['success'] = True
result['message'] = "Snippet Edited Successfully"

data = ""

if s.id is None:
	result['success'] = False
	result['message'] = "Snippet editing failed: you must specify an id"
else:
	dbCommands.ReadFromDatabaseCommand("Snippet", "id="+str(s.id))
	data += "lastChanged='" + str(datetime.datetime.now()) +"', "
	if s.title is not None:
		data += "title='" + str(s.title) + "',"

	if s.description is not None:
		data += "description='" + str(s.description) + "',"

	if s.code is not None:
		data += "code='" + str(s.code) + "',"

	if s.language is not None:
		data += "language='"+ str(s.language) + "',"

	if s.version is not None:
		data += "version='" + str(s.version) + "',"

	if s.upvotes is not None:
		data += "upvotes='" + str(s.upvotes) + "',"

	if s.downvotes is not None:
		data += "downvotes='" + str(s.downvotes) + "',"

	data = data[:-1]
	cmd = dbCommands.UpdateOnDatabaseCommand("Snippet", data, "id="+str(s.id))
	cmd.execute()

print result
