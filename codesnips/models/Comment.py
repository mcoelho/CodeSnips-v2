import os,sys,inspect
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from Post import *

class Comment(Post):
	def __init__(self, id, userId, upvotes, downvotes, lastChanged, snippetId, message):
		Post.__init__(self, id, userId, upvotes, downvotes, lastChanged)
		self.snippetId = snippetId
		self.message = message