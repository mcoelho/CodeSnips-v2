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
print "<img src='Media/logo.gif' alt='logo'><hr />"

print "<h2>Login page</h2>"	

if 'email' in args and 'password' in args:
	where = "email='"+args['email']+"' AND password='"+args['password']+"'"
	cmd = dbCommands.ReadFromDatabaseCommand("User", where)
	rows = cmd.execute()
	if any(rows):
		row = rows[0]
		if row["email"] == args["email"] and row["password"] == args["password"]:
			print "<p>logged as %s</p>" % args["email"]
			print '<meta http-equiv="refresh" content="0;url=http://web.cs.dal.ca/~coelho/oop/index.py" />'
			print '''<form action="%s" method="get">
			<input type="hidden" name="email" value=""/>
			<input type="submit" value="Log out">
			</form>''' % sys.argv[0]
			
	else:
		print "<p>%s does not exist</p>" % args["email"]
		print '''<form action="%s" method="get">
		<input type="submit" value="Go back to Login page">
		</form>''' % sys.argv[0]
		
		
elif 'name' in args and 'password' in args:
	where = "name='"+args['name']+"' AND password='"+args['password']+"'"
	cmd = dbCommands.ReadFromDatabaseCommand("User", where)
	rows = cmd.execute()
	if any(rows):
		row = rows[0]
		if row["name"] == args["name"] and row["password"] == args["password"]:
			print "<p>logged as %s</p>" % args["name"]
			print "<a href=http://web.cs.dal.ca/~coelho/oop/snippets/view.py>Go back</a>"
			print '''<form action="%s" method="get">
			<input type="hidden" name="name" value=""/>
			<input type="submit" value="Log out">
			</form>''' % sys.argv[0]	
	else:
		print "<p>%s does not exist</p>" % args["name"]
		print '''<form action="%s" method="get">
		<input type="submit" value="Go back to Login page">
		</form>''' % sys.argv[0]
	
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
	
print "<br>"
print "</div>"
#put all html code above this hashtag (unless you don't want it in the main body)
print "</div>"
print "</div>"
	
print "</body></html>"

