class User(object):
	def __init__(self, id, name, email, password, dob, bio, specialization, gravatarLink, permissions):
		self.id = id
		self.name = name
		self.email = email
		self.password = password
		self.dob = dob
		self.bio = bio
		self.specialization = specialization
		self.gravatarLink = gravatarLink
		self.permissions = permissions
		

class NullUser(object):
	def __init__(self):
		self.isNull = True
		