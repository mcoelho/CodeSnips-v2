#!/local/bin/python

import os
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys

pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

form = cgi.FieldStorage()

cmd = dbCommands.ReadFromDatabaseCommand("Snippet")
rows = cmd.execute()


print "Content-type: text/html\n"
    
print "<html><head><link href='../Media/style.css' rel = 'stylesheet' type = 'text/css' media='all'/></head><body>"


print "<div id = 'main'>"
print "<div id = 'container'>"

#put all html code inside mainbody
print "<div id = 'mainbody'>" 

print "<h1>View Snippets</h1>"
print "<hr />"

for row in rows:
	print "<h2>Snippet Title:</h2>"
	print "<p>" + row['title'] + "</p><br>"
	print "<h2>Snippet Description</h2>"
	print "<p>" + row['description'] + "</p><br>"
	print "<h2>Langauge and Version</h2>"
	print "<p>" + row['language'] + " " + row['version'] + "</p><br>"
	print "<h2>Code</h2>"
	print "<code>" + row['code'] + "</code><br>"
	print "<button type='submit' formaction='update.py'>Edit</button>"

	print "<hr />" 

print "<br />"

print "</div>"
#put all html code above this hashtag (unless you don't want it in the main body)
print "</div>"
print "</div>"

print "</body></html>"