#!/local/bin/python

import os
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys
pkg = "~/public_html/oop/codesnips/models/languages"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from languages.initializeDBLanguages import *

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-type: text/html\n"
    
print "<html><head></head><body>"
    
print "<h1>Database Setup</h1>"

if 'administrator' in args:
	if args['administrator'] == 'admin123':
		conn = sqlite3.connect(os.path.dirname(os.path.expanduser("~/public_html/oop/codesnips/data/"))+'codesnips.db')

		c = conn.cursor()

		c.execute("DROP TABLE IF EXISTS Language")
		c.execute("DROP TABLE IF EXISTS User")
		c.execute("DROP TABLE IF EXISTS Snippet")
		c.execute("DROP TABLE IF EXISTS Comment")
		c.execute("DROP TABLE IF EXISTS RevisionRequest")
		c.execute("DROP TABLE IF EXISTS UserHistory")

		c.execute('''CREATE TABLE "Language" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "name" TEXT NOT NULL, "version" TEXT NOT NULL, "creator" TEXT NOT NULL, "yearIntroduced" TEXT NOT NULL, "operatingSystem" TEXT, "depFunctions" TEXT, "newFunctions" TEXT, "allFunctions" TEXT, "bugs" TEXT)''')
		c.execute('''CREATE TABLE "User" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "name" TEXT NOT NULL, "email" TEXT NOT NULL UNIQUE, "password" TEXT, "dob" TEXT, "bio" TEXT, "specialization" TEXT, "gravatarLink" TEXT, "permissions" INTEGER NOT NULL DEFAULT 1)''')
		c.execute('''CREATE TABLE "Snippet" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "userId" INTEGER NOT NULL DEFAULT 0, "upvotes" INTEGER NOT NULL DEFAULT 0, "downvotes" INTEGER NOT NULL DEFAULT 0, "lastChanged" TEXT, "title" TEXT NOT NULL, "revisionRequest" INTEGER, "description" TEXT NOT NULL, "code" TEXT NOT NULL, "language" TEXT NOT NULL, "version" TEXT NOT NULL)''')
		c.execute('''CREATE TABLE "Comment" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "userId" INTEGER NOT NULL DEFAULT 0, "upvotes" INTEGER NOT NULL DEFAULT 0, "downvotes" INTEGER NOT NULL DEFAULT 0, "lastChanged" TEXT, "snippetId" INTEGER NOT NULL DEFAULT 0, "message" TEXT)''')
		#c.execute('''CREATE TABLE "RevisionRequest" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "snippetId" INTEGER, "userId" INTEGER NOT NULL DEFAULT 0, "description" TEXT NOT NULL, "dateSent" TEXT, "code" TEXT)''')
		#c.execute('''CREATE TABLE "UserHistory" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "userId" INTEGER NOT NULL DEFAULT 0, "posts" TEXT, "comments" TEXT, "recentlyViewed" TEXT, "timeFrame" INTEGER, "timeFromNow" TEXT)''')
		conn.commit()

		conn.close()
                
		print "<p style='color:green'><strong>Database created sucessfully!</strong></p>"
	else:
		print "<p style='color:red'><strong>Wrong code entered!</strong></p>"
        
initializeLanguages()
print '''<form action="%s" method="get">
<input type="text" name="administrator">
<input type="submit" value="Setup">
</form>''' % sys.argv[0]

print "</body></html>"