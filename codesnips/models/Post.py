class Post(object):
	def __init__(self, id, userId, upvotes, downvotes, lastChanged):
		self.id = id
		self.userId = userId
		self.upvotes = upvotes
		self.downvotes = downvotes
		self.lastChanged = lastChanged