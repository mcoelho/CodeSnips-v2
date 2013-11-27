#!/local/bin/python

import os
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys

pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands

form = cgi.FieldStorage()

cmd = dbCommands.ReadFromDatabaseCommand("Snippet")
rows = cmd.execute()


print "Content-type: text/html\n"
    
print "<html><head><link href='../Media/style.css' rel = 'stylesheet' type = 'text/css' media='all'/></head><body>"


print "<div id = 'main'>"
print "<div id = 'container'>"

#put all html code inside mainbody
print "<div id = 'mainbody'>"

print "<img src='../Media/logo.gif' alt='logo'>"

print "<div id = 'navblock'>"
print "<ul>"
print "<li><a href=http://web.cs.dal.ca/~coelho/oop/index.py>Home</a></li>"
print "<li><a href=http://web.cs.dal.ca/~coelho/oop/snippets/view.py>View Snippets</a></li>"
print "<li><a href=http://web.cs.dal.ca/~coelho/oop/snippets/create.py>Create Snippet</a></li>"
print "<li><a href=#>View Langauges</a></li>"
print "<li><a href=http://web.cs.dal.ca/~coelho/oop/login.py>Log-in/Log-out</a></li>"
print "</ul>" 
print "</div>"

print "<hr />" 

print "<h2>View Snippets</h2>"

for row in rows:
	print "<a href='details.py?id="+ str(row['id'])+"'>" + str(row['title']) + "</a><br>"
	print "<h2>Langauge and Version</h2>"
	print "<p>" + row['language'] + " " + row['version'] + "</p><br>"

print "<br />"

print "</div>"
#put all html code above this hashtag (unless you don't want it in the main body)
print "</div>"
print "</div>"

print "</body></html>"