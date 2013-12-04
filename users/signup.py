#!/local/bin/python

import os, sys, time, cPickle,urllib,urllib2
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands

import cgi
import cgitb; cgitb.enable()  # for troubleshooting

print "Content-type: text/html\n" 
print "<html><head></head><body>"
print "<h1>Homepage</h1>"


print '''<form action="http://web.cs.dal.ca/~coelho/oop/login.py" method="post">
	<br>Email:</br><input type="text" name="Email">
	<br>Password:</br><input type="password" name="pass">
	<br>Date of birth:</br><input type="text" name="dob">
	<br>Bio:</br><input type="text" name="bio">
	<br>Specialization:</br><input type="text" name="spec">
	<br>Gravatar Link:</br><input type="text" name="grav">
    <input type="submit" value="Confirm">
    </form>'''
	
	
	
print "</body></html>"

