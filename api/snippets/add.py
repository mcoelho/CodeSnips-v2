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
result['message'] = "Snippet Added Successfully"

columns = "lastChanged, "
values = "'"+str(datetime.datetime.now())+"', "

if s.userId is not None:
	columns += "userId"
	values += "'" + str(s.userId) + "'"
else:
	result['success'] = False
	result['message'] = "Snippet creation failed: you must specify a user id"

if s.title is not None:
	columns += ", title"
	values += ", '" + s.title + "'"
else:
	result['success'] = False
	result['message'] = "Snippet creation failed: you must specify a title"

if s.description is not None:
	columns += ", description"
	values += ", '" + s.description + "'"
else:
	result['success'] = False
	result['message'] = "Snippet creation failed: you must specify a description"

if s.code is not None:
	columns += ", code"
	values += ", '" + str(s.code) + "'"
else:
	result['success'] = False
	result['message'] = "Snippet creation failed: you must specify code"

if s.language is not None:
	columns += ", language"
	values += ", '" + s.language + "'"
else:
	result['success'] = False
	result['message'] = "Snippet creation failed: you must specify a language"

if s.version is not None:
	columns += ", version"
	values += ", '" + s.version + "'"
else:
	result['success'] = False
	result['message'] = "Snippet creation failed: you must specify a version"

if result['success'] is True:
	cmd = dbCommands.AddToDatabaseCommand("Snippet", columns, values)
	cmd.execute()

print result
