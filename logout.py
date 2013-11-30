#!/local/bin/python

import os, sys, time, cPickle
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-type: text/html\n"

if 'comment' in args:
    data.append({
        'who' : args.get('user',"") and args.get("password",""),
        'when': time.ctime(),
        'what': args.get('comment')
    })
    with open(datafile, "wb") as handle:
        cPickle.dump(data,handle)
    
print "<html><head><link href='Media/style.css' rel = 'stylesheet' type = 'text/css' media='all'/></head><body>"
print "<div id = 'main'>"
print "<div id = 'container'>"

#put all html code inside mainbody
print "<div id = 'mainbody'>" 
print "<a href=http://web.cs.dal.ca/~coleho/oop/index1.py><img src='Media/logo.gif' alt='logo'></a><hr />"

print "<p>Log-out successfully!</p>"
print "<p>Thank you for using CodeSnips!</p>"
print "<p>See you!</p>"
print '''<form action="%s" method="get">
<a href="index.py">Go back to Login page</a>
</form>''' % sys.argv[0]
		
		

print "<br>"
print "</div>"
#put all html code above this hashtag (unless you don't want it in the main body)
print "</div>"
print "</div>"
	
print "</body></html>"

