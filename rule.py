import re

class Route:

	def __init__(self, path, func, request_methods):
		'''parses out parameters in url'''
		self.path = ''
		self.endpoint = func
		self.args = []
		self.methods = request_methods
		tokens = path.split('/')
		for token in tokens:
			if re.match('<\w+>', token):
				self.args.append(token.strip('<').strip('>'))
			elif token != '': #because splitting the string will include a ''
				self.path += '/' + token + '/'
		print 'self.path: ', self.path

	def get_args(self):
		return self.args

	def get_methods(self):
		return self.methods


