#!/local/bin/python

import os
import cgi
import cgitb; cgitb.enable()
import sys

pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

cmd = dbCommands.ReadFromDatabaseCommand("Snippet", "id='"+args['id']+"'")
rows = cmd.execute()
row = rows[0]

uid = args['uid']

print "Content-type: text/html\n"
    
print "<html><head><link href='../Media/style.css' rel = 'stylesheet' type = 'text/css' media='all'/></head><body>"

print "<div id = 'main'>"
print "<div id = 'container'>"

#put all html code inside mainbody
print "<div id = 'mainbody'>"

print "<img src='../Media/logo.gif' alt='logo'>"

print "<div id = 'navblock'>"
print "<ul>"
print "<li><a href=http://web.cs.dal.ca/~coelho/oop/index.py?uid=" + uid + ">Home</a></li>"
print "<li><a href=http://web.cs.dal.ca/~coelho/oop/snippets/view.py?uid=" + uid + ">View Snippets</a></li>"
print "<li><a style='color:black' href=http://web.cs.dal.ca/~coelho/oop/snippets/create.py?uid=" + uid + ">Create Snippet</a></li>"
print "<li><a href=#>View Langauges</a></li>"
print "<li><a href=http://web.cs.dal.ca/~coelho/oop/login.py>Log-in/Log-out</a></li>"
print "</ul>" 
print "</div>"

print "<hr />"

print "<h2>New Snippet</h2>"

print "<form name='snippetInput' action='processUpdate.py' method='post'>"
print "<input type='hidden' name='sId' value='"+args['id']+"'>"
print "Snippet Title: <input type='text' name='snippetTitle' value='"+row['title']+"'><br>"
print "Snippet Description: <input type='text' name='snippetDesc' value='"+row['description']+"'><br>"
print "Snippet Language: <input type='text' name='snippetLang' value='"+row['language']+"'><br>"
print "Language Version: <input type='text' name='snippetVersion' value='"+row['version']+"'><br>"
print "Code: <textarea name='snippetCode'>"+row['code']+"</textarea><br>"
print "<input type='hidden' name='uid' value='"+uid+"'>"
print "<input type='submit' value='Submit'>"

print "</form>"

print "<br />"

print "</div>"
#put all html code above this hashtag (unless you don't want it in the main body)
print "</div>"
print "</div>"

print "</body></html>"