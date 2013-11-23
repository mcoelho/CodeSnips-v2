#!/local/bin/python

import sys
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-type: text/html\n"
    
print "<html><head></head><body>"
    
print "<h1>Comments:</h1><ul>"
if 'comment' in args:
    print "<li>%s</li>" % args['comment']
print "</ul>"

print '''<form action="%s" method="get">
<input type="text" name="comment">
<input type="submit" value="Add comment">
</form>''' % sys.argv[0]

print "</body></html>"
