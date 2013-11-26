#!/local/bin/python

import os
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands
from codesnips.models import Snippet

form = cgi.FieldStorage();

snippetTitle = form.getvalue('snippetTitle')
snippetDesc = form.getvalue('snippetDesc')
snippetLang = form.getvalue('snippetLang')
snippetCode = form.getvalue('snippetCode')

cmd = dbCommands.AddToDatabaseCommand("Snippet", "user, language, name, description, code", "'1','" + snippetLang + "','" + snippetTitle + "','" + snippetDesc + "','" + snippetCode + "'")
cmd.execute() 
