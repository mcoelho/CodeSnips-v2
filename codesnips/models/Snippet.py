import os,sys,inspect
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from Post import *

class Snippet(Post):
	def __init__(self, id, userId, upvotes, downvotes, lastChanged, title, description, code, language, version):
		
		Post.__init__(self, id, userId, upvotes, downvotes, lastChanged)
		self.title = title
		self.description = description
		self.code = code
		self.language = language
		self.version = version

class NullSnippet(object):
	def __init__(self):
		self.isNull = True