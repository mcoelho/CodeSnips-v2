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

u = jsonpickle.decode(sys.stdin.read())

print "Content-type: application/json\n"

result = {}
result['success'] = True
result['message'] = "User Edited Successfully"

data = ""

if u.id is None:
	result['success'] = False
	result['message'] = "User editing failed: you must specify an id"
else:
	dbCommands.ReadFromDatabaseCommand("User", "id="+str(u.id))
	if u.name is not None:
		data += "name='" + u.name + "',"

	if u.password is not None:
		data += "password='" + u.password + "',"

	if u.dob is not None:
		data += "dob='" + u.dob + "',"

	if u.bio is not None:
		data += "bio='"+ u.bio + "',"

	if u.specialization is not None:
		data += "specialization='" + u.specialization + "',"

	if u.gravatarLink is not None:
		data += "gravatarLink='" + u.gravatarLink + "',"

	if u.permissions is not None:
		data += "permissions='" + str(u.permissions) + "',"
	else:
		data += "permissions='1',"

	data = data[:-1]
	cmd = dbCommands.UpdateOnDatabaseCommand("User", data, "id="+str(u.id))
	cmd.execute()

print result
