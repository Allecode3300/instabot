class User():
	def __init__(self, username):
		self.username = username

class PersonalUser(User):
	def __init__(self, username, password, coocki):
		self.username = username
		self.coocki = coocki
		self.password = password

class photo():
	def __init__(self, description, history, hastags, url):
		self.description = description # Descripción de la foto
		self.history = history # Si es una historia o una publicación
		self.hastags = hastags # Los hastags que tendra
		self.url = url # La url de donde esta guradada la imagen
