#!/local/bin/python

import sys
import cgi
import cgitb; cgitb.enable()

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-Type: text/html"
print

print "<TITLE>CGI script output</TITLE>"
print "<H1>This is my first CGI script</H1>"
print "Hello, world!"