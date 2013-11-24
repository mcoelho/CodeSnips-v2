#!/local/bin/python

import os
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-type: text/html\n"
    
print "<html><head></head><body>"
    
print "<h1>Database Setup</h1>"

if 'administrator' in args:
	if args['administrator'] == 'admin123':
		conn = sqlite3.connect('codesnips.db')

		c = conn.cursor()

		c.execute("DROP TABLE IF EXISTS Language")
		c.execute("DROP TABLE IF EXISTS User")
		c.execute("DROP TABLE IF EXISTS Snippet")
		c.execute("DROP TABLE IF EXISTS Comment")
		c.execute("DROP TABLE IF EXISTS RevisionRequest")
		c.execute("DROP TABLE IF EXISTS UserHistory")

		c.execute('''CREATE TABLE "Language" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "name" TEXT NOT NULL, "version" TEXT NOT NULL, "category" TEXT NOT NULL, "description" TEXT, "deprecatedKeywords" TEXT)''')
		c.execute('''CREATE TABLE "User" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "userHistory" INTEGER REFERENCES "UserHistory" ("id") ON DELETE CASCADE ON UPDATE CASCADE, "name" TEXT NOT NULL, "email" TEXT NOT NULL UNIQUE, "password" TEXT, "dob" TEXT, "bio" TEXT, "specialization" TEXT, "gravatarLink" TEXT, "favorites" TEXT, "permissions" INTEGER NOT NULL DEFAULT 0)''')
		c.execute('''CREATE TABLE "Snippet" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "user" INTEGER NOT NULL, "language" INTEGER NOT NULL REFERENCES "Language" ("id"), "name" TEXT NOT NULL, "description" TEXT NOT NULL, "code" TEXT NOT NULL)''')
		c.execute('''CREATE TABLE "Comment" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "userId" INTEGER NOT NULL REFERENCES "User" ("id"), "snippetId" INTEGER NOT NULL DEFAULT 0 REFERENCES "Snippet" ("id"), "message" TEXT, "upvotes" INTEGER NOT NULL DEFAULT 0, "downvotes" INTEGER NOT NULL DEFAULT 0, "lastChanged" TEXT)''')
		c.execute('''CREATE TABLE "RevisionRequest" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "snippetId" INTEGER NOT NULL REFERENCES "Snippet" ("id"), "userId" INTEGER NOT NULL REFERENCES "User" ("id"), "description" TEXT NOT NULL, "dateSent" TEXT, "code" TEXT)''')
		c.execute('''CREATE TABLE "UserHistory" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "userId" INTEGER NOT NULL REFERENCES "User" ("id"), "posts" TEXT, "comments" TEXT, "recentlyViewed" TEXT, "timeFrame" INTEGER, "timeFromNow" TEXT)''')

		# Save (commit) the changes
		conn.commit()

		# We can also close the connection if we are done with it.
		# Just be sure any changes have been committed or they will be lost.
		conn.close()
		print "<p style='color:green'><strong>Database created sucessfully!</strong></p>"
	else:
		print "<p style='color:red'><strong>Wrong code entered!</strong></p>"

print '''<form action="%s" method="get">
<input type="text" name="administrator">
<input type="submit" value="Setup">
</form>''' % sys.argv[0]

print "</body></html>"