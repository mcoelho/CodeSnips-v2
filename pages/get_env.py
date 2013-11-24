#!/local/bin/python

import os
import cgi
import cgitb; cgitb.enable()

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-type: text/html\n"

print "<html><head></head><body>"
print "<h1>Comments:</h1>"
print "<p>Environment</p>"

print "</body></html>"