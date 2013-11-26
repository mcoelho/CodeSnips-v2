#!/local/bin/python

import os
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-type: text/html\n"
    
print "<html><head><link href='../Media/style.css' rel = 'stylesheet' type = 'text/css' media='all'/></head><body>"


print "<div id = 'main'>"
print "<div id = 'container'>"

#put all html code inside mainbody
print "<div id = 'mainbody'>" 

print "<h1>New Snippet</h1>"
print "<hr />"

print "<form name='snippetInput' action='push.py' method='post'>"

print "Snippet Title: <input type='text' name='snippetTitle'><br>"
print "Snippet Description: <input type='text' name='snippetDesc'><br>"
print "Snippet Language: <input type='text' name='snippetLang'><br>"
print "Code: <input type='textarea' name='snippetCode'><br>"
print "<input type='submit' value='Submit'>"

print "</form>"

print "<br />"

print "</div>"
#put all html code above this hashtag (unless you don't want it in the main body)
print "</div>"
print "</div>"

print "</body></html>"