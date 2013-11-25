#!/local/bin/python

import os, sys, time, cPickle

import cgi
import cgitb; cgitb.enable()  # for troubleshooting

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-type: text/html\n"

datafile = sys.argv[0]+'.data'

if not os.path.exists(datafile):
    with open(datafile, "wb") as handle:
        cPickle.dump([],handle)

with open(datafile, "rb") as handle:
    data = cPickle.load(handle)

if 'comment' in args:
    data.append({ 'when': time.ctime(), 'what': args.get('comment') })
    with open(datafile, "wb") as handle:
        cPickle.dump(data,handle)
    
print "<html><head></head><body>"
    
print "<h1>Comments:</h1><ul>"
for x in data:
    print "<li><b>%s:</b> %s</li>" % (x['when'], x['what'])
print "</ul>"

print '''<form action="%s" method="get">
<input type="text" name="comment">
<input type="submit" value="Add comment">
</form>''' % sys.argv[0]

print "</body></html>"

