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
result['message'] = "User Added Successfully"

columns = ""
values = ""

if u.name is not None:
	columns += "name"
	values += "'" + u.name + "'"
else:
	result['success'] = False
	result['message'] = "User creation failed: you must specify a name"

if u.email is not None:
	row = dbCommands.ReadFromDatabaseCommand("User", "email='"+u.email+"'").execute()
	if not any(row):
		columns += ", email"
		values += ", '" + u.email + "'"
	else:
		result['success'] = False
		result['message'] = "User creation failed: email already in use"
else:
	result['success'] = False
	result['message'] = "User creation failed: you must specify an email"

if u.password is not None:
	columns += ", password"
	values += ", '" + u.password + "'"
else:
	result['success'] = False
	result['message'] = "User creation failed: you must specify a password"

if u.dob is not None:
	columns += ", dob"
	values += ", '" + u.dob + "'"

if u.bio is not None:
	columns += ", bio"
	values += ", '" + u.bio + "'"

if u.specialization is not None:
	columns += ", specialization"
	values += ", '" + u.specialization + "'"

if u.gravatarLink is not None:
	columns += ", gravatarLink"
	values += ", '" + u.gravatarLink + "'"

if u.favorites is not None:
	columns += ", favorites"
	values += ", '" + u.favorites + "'"

if u.permissions is not None:
	columns += ", permissions"
	values += ", '" + str(u.permissions) + "'"
else:
	columns += ", permissions"
	values += ", '1'"

if result['success'] is True:
	cmd = dbCommands.AddToDatabaseCommand("User", columns, values)
	cmd.execute()

print result
