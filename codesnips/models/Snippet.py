import Post


class Snippet(Post):
	def __init__(self, id, userId, upvotes, downvotes, lastChanged, title, revisionRequest, description, code, language, version):
		Post.__init__(self, id, userId, upvotes, downvotes, lastChanged)
		self.id = id
		self.title = title
		self.revisionRequest = revisionRequest
		self.description = description
		self.code = code
		self.language = language
		self.version = version
