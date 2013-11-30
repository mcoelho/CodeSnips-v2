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

print "<a href=http://web.cs.dal.ca/~yzhang/oop/index1.py><img src='Media/logo.gif' alt='logo'></a><hr />"

print "<div id = 'navblock'>"
print "<ul>"
print "<li><a style='color:black' href=http://web.cs.dal.ca/~yzhang/oop/index.py>Home</a></li>"
print "<li><a href=http://web.cs.dal.ca/~yzhang/oop/snippets/view.py>View Snippets</a></li>"
print "<li><a href=http://web.cs.dal.ca/~yzhang/oop/snippets/create.py>Create Snippet</a></li>"
print "<li><a href=#>View Languages</a></li>"
print "<li><a href=http://web.cs.dal.ca/~yzhang/oop/logout.py>Log-out</a></li>"
print "</ul>" 
print "</div>"

print "<hr />"


print "<h2>Welcome!</h2>"

print "<p>Now enjoy CodeSnips!</p>"
print "<p>You can view snippets, create snippet or view different languages!</p>"

#this is a section break (it has an image to make it look cool):

print "<br />"

print "</div>"
#put all html code above this hashtag (unless you don't want it in the main body)
print "</div>"
print "</div>"

print "</body></html>"