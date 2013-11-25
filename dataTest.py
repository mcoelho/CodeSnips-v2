#!/local/bin/python

import cgi
import cgitb; cgitb.enable()
import commands

cmdlist = []
cmdlist.append(commands.AddToDatabaseCommand("User", "name, email, password, permissions", "'Matthew Coelho', 'mcoelho@northrock.bm', 'password', '3'"))
cmdlist.append(commands.AddToDatabaseCommand("User", "name, email, password, permissions", "'John Doe', 'jd@northrock.bm', 'password', '3'"))
cmdlist.append(commands.AddToDatabaseCommand("User", "name, email, password, permissions", "'Mary Sue', 'ms@northrock.bm', 'password', '3'"))
cmdlist.append(commands.AddToDatabaseCommand("User", "name, email, password, permissions", "'Mark Smith', 'msmith@northrock.bm', 'password', '3'"))

print "Content-type: text/html\n"
    
print "<html><head></head><body>"
    
print "<h1>Database Test</h1>"
cmd = commands.DeleteFromDatabaseCommand("USER", "password='password'")
cmd.execute()

for command in cmdlist:
	command.execute()

cmd = commands.ReadFromDatabaseCommand("User")
rows = cmd.execute()

for row in rows:
	print "<p>" + row['name'] + " " + row['email'] + " " + row['password'] + "</p>"

cmd = commands.ReadFromDatabaseCommand("USER", "email='mcoelho@northrock.bm'")
rows = cmd.execute()
for row in rows:
	print "<p>" + row['name'] + " " + row['email'] + " " + row['password'] + "</p>"

print "</body></html>"