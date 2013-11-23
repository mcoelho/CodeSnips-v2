#!/local/bin/python

import sys

import cgi
import cgitb; cgitb.enable()  # for troubleshooting

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-type: text/html\n"
    
print "<html><head></head><body>"
    
print "<h1>Home Page:</h1><ul>"

print "</body></html>"