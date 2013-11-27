#!/local/bin/python

import os, sys, time, cPickle
import commands
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
    
print "<html><head></head><body>"
print "<h1>Homepage</h1>"

if 'user' in args and 'password' in args:
	where = "email='"+args['email']+"' AND password='"+args['password']+","
	cmd = commands.ReadFromDatabaseCommand("User", where)
	rows = cmd.execute()
	if "user" in cmd and "password" in cmd:
		print "<p>logged as %s</p>" % args["user"]
		print '''<form action="%s" method="get">
		<input type="hidden" name="user" value=""/>
		<input type="submit" value="Log out">
		</form>''' % sys.argv[0]
	else:
		#print "<p>%s does not exist</p>" % args["email"]
		print "test"
else:
    print '''<form action="%s" method="get">
	UserID:
    <input type="text" name="email">
	<p></p>
	Password:
	<input type="password" name="password">
    <input type="submit" value="Log in">
	<a href="signup.cgi">Dont't have account?</a>
    </form>''' % sys.argv[0]
	
print "</body></html>"

