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
    data.append({
        'who' : args.get('user',""),
        'when': time.ctime(),
        'what': args.get('comment')
    })
    with open(datafile, "wb") as handle:
        cPickle.dump(data,handle)
    
print "<html><head></head><body>"
if args.get("user",""):
    print "<p>logged as %s</p>" % args["user"]
    print '''<form action="%s" method="get">
    <input type="hidden" name="user" value=""/>
    <input type="submit" value="Log out">
    </form>''' % sys.argv[0]
else:
    print '''<form action="%s" method="get">
    <input type="text" name="user">
    <input type="submit" value="Log in">
    </form>''' % sys.argv[0]
    
print "<h1>Comments:</h1><ul>"

for x in data:
    print "<li><b>%s <em>(%s)</em>:</b> %s</li>" % (x['who'], x['when'], x['what'])
print "</ul>"

print '''<form action="%s" method="get">
<input type="hidden" name="user" value="%s">
<input type="text" name="comment">
<input type="submit" value="Add comment">
</form>''' % (sys.argv[0], args.get("user",""),)

print "</body></html>"
