#!/local/bin/python

import os, sys, inspect
import cgi
import cgitb; cgitb.enable()
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands
from codesnips.models.User import *
import json

print "Content-type: application/json\n"

result = {}
result['success'] = True
result['message'] = "Comment Deleted Successfully"

data = json.loads(sys.stdin.read())


cmd = dbCommands.DeleteFromDatabaseCommand("Comment", "id="+str(data['commentId']))
cmd.execute()

print result
