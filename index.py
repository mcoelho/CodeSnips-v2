#!/local/bin/python

import os
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-type: text/html\n"
    
print "<html><head><link href='Media/style.css' rel = 'stylesheet' type = 'text/css' media='all'/></head><body>"


print "<div id = 'main'>"
print "<div id = 'container'>"

#put all html code inside mainbody
print "<div id = 'mainbody'>" 

print "<a href=http://web.cs.dal.ca/~coelho/oop/index.py><img src='Media/logo.gif' alt='logo'></a><hr />"

print "<div id = 'navblock'>"
print "<ul>"
print "<li><a style='color:black' href=http://web.cs.dal.ca/~coelho/oop/index.py>Home</a></li>"
print "<li><a href=http://web.cs.dal.ca/~coelho/oop/snippets/view1.py>View Snippets</a></li>"
print "<li><a href=#>View Languages</a></li>"
print "<li><a href=http://web.cs.dal.ca/~coelho/oop/login.py>Log-in</a></li>"
print "</ul>" 
print "</div>"

print "<hr />"


print "<h2>Welcome!</h2>"

print "<p>Welcome to CodeSnips!</p>"

#this is a section break (it has an image to make it look cool):

print "<br />"

print "</div>"
#put all html code above this hashtag (unless you don't want it in the main body)
print "</div>"
print "</div>"

print "</body></html>"