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

uid = args['uid']

cmd = dbCommands.ReadFromDatabaseCommand("User", "id='"+uid+"'")
loggedInUser = cmd.execute()

permissionsL = 0
nameL = "NOUSERNAME"
if any(loggedInUser):
	loggedInUser = loggedInUser[0]
	nameL = loggedInUser['name']




print "Content-type: text/html\n"
    
print "<html><head><link href='Media/style.css' rel = 'stylesheet' type = 'text/css' media='all'/></head><body>"


print "<div id = 'main'>"
print "<div id = 'container'>"

#put all html code inside mainbody
print "<div id = 'mainbody'>" 

print "<a href=http://web.cs.dal.ca/~coelho/oop/index1.py?uid=" + uid + "><img src='Media/logo.gif' alt='logo'></a><hr />"

print "<div id = 'navblock'>"
print "<ul>"
print "<li><a style='color:black' href=http://web.cs.dal.ca/~coelho/oop/index1.py?uid=" + uid + ">Home</a></li>"
print "<li><a href=http://web.cs.dal.ca/~coelho/oop/snippets/view.py?uid=" + uid + ">View Snippets</a></li>"
print "<li><a href=http://web.cs.dal.ca/~coelho/oop/snippets/create.py?uid=" + uid + ">Create Snippet</a></li>"
print "<li><a href=#>View Languages</a></li>"
print "<li><a href=http://web.cs.dal.ca/~coelho/oop/logout.py>Log-out</a></li>"
print "</ul>" 
print "</div>"

print "<hr />"


print "<h2>Welcome, " + str(nameL) +"!</h2>"

print "<p>Now enjoy CodeSnips!</p>"
print "<p>You can view snippets, create snippet or view different languages!</p>"

#this is a section break (it has an image to make it look cool):

print "<br />"

print "</div>"
#put all html code above this hashtag (unless you don't want it in the main body)
print "</div>"
print "</div>"

print "</body></html>"