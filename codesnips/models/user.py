class User(object):
	# id
	# userHistory
	# name
	# email
	# password
	# dob
	# bio
	# specialization
	# gravatarLink
	# favorites
	# permissions

	def __init__(self, id, userHistory,	name, email, password, dob, bio, specialization, gravatarLink, favorites, permissions):
		self.id = id
		self.userHistory = userHistory
		self.name = name
		self.email = email
		self.password = password
		self.dob = dob
		self.bio = bio
		self.specialization = specialization
		self.gravatarLink = gravatarLink
		self.favorites = favorites
		self.permissions = permissions