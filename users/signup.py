#!/local/bin/python

import os, sys, inspect
import cgi
import cgitb; cgitb.enable()
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-type: text/html\n" 
print "<html><head></head><body>"
print "<h1>Homepage</h1>"


if 'name' in args and 'email' in args and 'pass' in args and 'dob' in args and 'bio' in args and 'spec' in args and 'grav' in args:
	name = args['name']
	email = args['email']
	passw = args['pass']
	dob = args['dob']
	bio = args['bio']
	spec = args['spec']
	grav = args['grav']
	
	cmd = dbCommands.AddToDatabaseCommand("User", "name,email,password, dob, bio, specialization, gravatarLink", "'"+str(name) + "', '" + str(email) + "', '" + str(passw) + "', '" + str(dob) + "','" + str(bio) + "', '" + str(spec) + "', '" + str(grav) + "'")
	cmd.execute()
	
	
	print '<meta http-equiv="refresh" content="1;url=http://web.cs.dal.ca/~coelho/oop/login.py" />'
	
else:
	print '''<form action="http://web.cs.dal.ca/~coelho/oop/users/signup.py" method="get">
		<br>Name:</br><input type="text" name="name">
		<br>Email:</br><input type="text" name="email">
		<br>Password:</br><input type="password" name="pass">
		<br>Date of birth:</br><input type="text" name="dob">
		<br>Bio:</br><input type="text" name="bio">
		<br>Specialization:</br><input type="text" name="spec">
		<br>Gravatar Link:</br><input type="text" name="grav">
		<input type="submit" value="Confirm">
		</form>'''
	print "</body></html>"
	


	
	


