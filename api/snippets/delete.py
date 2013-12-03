#!/local/bin/python

import os, sys, inspect
import cgi
import cgitb; cgitb.enable()
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands
import json

print "Content-type: application/json\n"

result = {}
result['success'] = True
result['message'] = "Snippet Deleted Successfully"

data = json.loads(sys.stdin.read())


cmd = dbCommands.DeleteFromDatabaseCommand("Snippet", "id="+str(data['snippetId']))
cmd.execute()

print result
