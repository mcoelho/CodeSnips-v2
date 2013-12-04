#!/local/bin/python

import os
import cgi
import cgitb; cgitb.enable()
import sys

pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

uid = args['uid']

cmd = dbCommands.ReadFromDatabaseCommand("Snippet", "id='"+args['id']+"'")
rows = cmd.execute()

cmd = dbCommands.ReadFromDatabaseCommand("Comment", "snippetId='"+args['id']+"'")
rows2 = cmd.execute()

cmd = dbCommands.ReadFromDatabaseCommand("User", "id='"+uid+"'")
loggedInUser = cmd.execute()

permissionsL = 0
if any(loggedInUser):
	loggedInUser = loggedInUser[0]
	permissionsL = loggedInUser['permissions']

if any(rows):
	row = rows[0]
	print "Content-type: text/html\n"
	    
	print "<html><head><link href='../Media/style.css' rel = 'stylesheet' type = 'text/css' media='all'/></head><body>"


	print "<div id = 'main'>"
	print "<div id = 'container'>"

	#put all html code inside mainbody
	print "<div id = 'mainbody'>"

	print "<img src='../Media/logo.gif' alt='logo'>"

	print "<div id = 'navblock'>"
	print "<ul>"
	print "<li><a style='color:black' href=http://web.cs.dal.ca/~coelho/oop/index1.py?uid=" + uid + ">Home</a></li>"
	print "<li><a href=http://web.cs.dal.ca/~coelho/oop/snippets/view.py?uid=" + uid + ">View Snippets</a></li>"
	print "<li><a href=http://web.cs.dal.ca/~coelho/oop/snippets/create.py?uid=" + uid + ">Create Snippet</a></li>"
	print "<li><a href=#>View Languages</a></li>"
	print "<li><a href=http://web.cs.dal.ca/~coelho/oop/logout.py>Log-out</a></li>"
	print "</ul>" 
	print "</div>"

	print "<hr />" 

	print "<h2>Snippet Details</h2>"

	print "<h2>Snippet Title:</h2>"
	print "<p>" + row['title'] + "</p><br>"
	print "<h2>Snippet Description</h2>"
	print "<p>" + row['description'] + "</p><br>"
	print "<h2>Langauge and Version</h2>"
	print "<p>" + row['language'] + " " + row['version'] + "</p><br>"
	print "<h2>Code</h2>"
	print "<code>" + row['code'] + "</code><br><hr />"
	print "<p><i>Last Changed: "+ row['lastChanged'] +"</i></p>"
	print "<div id = buttons>"
	if (permissionsL > 1):
		print "<a href='edit.py?id="+str(row['id'])+"&uid=" + uid + "'>Edit snippet</a>"
	print "<span> <a href='upvote.py?id="+str(row['id'])+ "&votes=" + str(row['upvotes']) + "&uid=" + uid + "'>" + str(row['upvotes']) + " - Upvote Snippet</a>  <a href='downvote.py?id="+str(row['id'])+"&votes=" + str(row['downvotes']) + "&uid=" + uid + "'>" + str(row['downvotes']) + " - Downvote Snippet</a></span>"
	print "<br />"

	print "<h2>Comments</h2>"
	print "<form name='leaveComment' action='../comments/add.py' method='post'>"
	print "<textarea name='snippetComment'>Add your code here!</textarea><br>"
	print "<input type='hidden' name='snippetID' value='"+str(row['id'])+"'>"
	print "<input type='hidden' name='uid' value='"+uid+"'>"
	print "<input type='submit' value='Submit'>"
	print "</form>"

	for row2 in rows2:
		cmd = dbCommands.ReadFromDatabaseCommand("User", "id='"+str(row2['userId'])+"'")
		userinfo = cmd.execute()
		if any(userinfo):
			userinfo = userinfo[0]
			nameL = userinfo['name']
		else:
			nameL = "NO USERNAME"
		print "<p>"+ str(nameL) + ": " + str(row2['message']) + "</p>"
		print "<p><i>Last Changed: "+ str(row2['lastChanged']) +"</i></p>"
		if (permissionsL > 1 or (str(uid) == str(row2['userId']))):
			print "<a href='../comments/delete.py?id="+str(row2['id'])+"&uid="+uid+"&snippetId="+str(row2['snippetId'])+"'>Delete comment</a>"
		print "<hr />"
	#print "<a href=../comments/add.py?id="+str(row['id'])+"'>Add Comment</a>"
	print "</div>"
	print "</div>"
	#put all html code above this hashtag (unless you don't want it in the main body)
	print "</div>"
	print "</div>"

	print "</body></html>"

else:
	print "Content-type: text/html\n"
	    
	print "<html><head><link href='../Media/style.css' rel = 'stylesheet' type = 'text/css' media='all'/></head><body>"


	print "<div id = 'main'>"
	print "<div id = 'container'>"

	#put all html code inside mainbody
	print "<div id = 'mainbody'>" 

	print "<h1>View Snippets</h1>"
	print "<hr />"
	print "<p>Could not find snippet!</p>"
	print "<br />"

	print "</div>"
	#put all html code above this hashtag (unless you don't want it in the main body)
	print "</div>"
	print "</div>"

	print "</body></html>"
