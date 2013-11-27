1#!/local/bin/python

import os, sys, time, cPickle
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands
from codesnips.models.User import *
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}


#print "Set-Cookie:UserID=XYZ;\r\n"
#print "Set-Cookie:Password=XYZ123;\r\n"
#print "Set-Cookie:Expires=Tuesday, 31-Dec-2007 23:12:40 GMT;\r\n"
#print "Set-Cookie:Domain=www.web.cs.dal.ca/~tlin/CSCI3132/signup.cgi;\r\n"
#print "Set-Cookie:Path=/perl;\n"

print "Content-type: text/html\n"

datafile = sys.argv[0]+'.data'

if not os.path.exists(datafile):
    with open(datafile, "wb") as handle:
        cPickle.dump([],handle)

with open(datafile, "rb") as handle:
    data = cPickle.load(handle)

if 'comment' in args:
    data.append({
        'who' : args.get('user',"") and args.get("password",""),
        'when': time.ctime(),
        'what': args.get('comment')
    })
    with open(datafile, "wb") as handle:
        cPickle.dump(data,handle)
    
print "<html><head></head><body>"
print "<h1>Homepage</h1>"
if args.get("user","") and args.get("password",""):
    print "<p>logged as %s</p>" % args["user"]
    print '''<form action="%s" method="get">
    <input type="hidden" name="user" value=""/>
    <input type="submit" value="Log out">
    </form>''' % sys.argv[0]
else:
    print '''<form action="%s" method="get">
	<br>Name:</br><input type="text" name="Name">
	<br>Email:</br><input type="text" name="Email">
	<br>Password:</br><input type="password" name="Password">
	<br>Date of birth:</br><input type="text" name="DateofBirth">
	<br>Bio:</br><input type="text" name="DateofBirth">
	<br>Specialization:</br><input type="text" name="Specialization">
	<br>Gravatar Link:</br><input type="text" name="GravatarLink">
	<br>Favorites:</br><input type="text" name="Favorites">	
    <input type="submit" value="Confirm">
    </form>''' % sys.argv[0]
    
dbCommands.AddtoDatabaseCommand("User","name,email,password,dob,bio,specialization,gravatarLink,favorites","'"+form["name"].value+"','"+form["email"].value+"','"+form["password"].value+"','"+form["dob"].value+"','"+form["bio"].value+"','"+form["specialization"].value+"','"+form["gravatarLink"].value+"','"+form["favorites"].value+"'").execute()

for x in data:
    print "<li><b>%s <em>(%s)</em>:</b> %s</li>" % (x['who'], x['when'], x['what'])


print "</body></html>"

