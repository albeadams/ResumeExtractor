
import sys, re
import spacy


class InfoExtractor(object):

	def __init__(self):

		#https://spacy.io/usage/linguistic-features#section-named-entities
		self.nlp = spacy.load('en_core_web_sm')
		self.name = ''


	def _name_extractor(self, txt):
		entities = (self.nlp(txt)).ents
		names = []
		for token in entities:
			if token.label_ == 'PERSON':
				name = token.text.strip()
				if name.count(' ') > 0: # more than 1 name
					names.append(name)

		if len(names) == 0:
			return 'NAME NOT FOUND'

		return names[0]   # first name is the resume owner


	def extract_info(self, txt):

		self.name = self._name_extractor(txt)
		self.email = ''
		self.phone = ''

		emailRegex = '^[a-z0-9]+[\._]?[a-z0-9]+[\._]?[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
		phoneRegex = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)[-\.\s]??\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
		email = ''
		phone = ''
		for line in txt.split('\n'):
			for word in line.split():
				if(re.search(emailRegex,word)) and email == '':
					self.email = word

			if not email == '' and email in line:
				line = line.replace(email, '')

			if not phone:
				try:
				    line = line.replace(' ', '')
				    line = line.replace('·', '-')
				    phone = re.search(phoneRegex,line)[0]
				    phone = re.sub('[^0-9]', '', phone)
				    self.phone = '(' + phone[:3] + ') ' + phone[3:6] + '-' + phone[6:]
				except TypeError:
				    pass

		if self.email == '':
			self.email = 'NO EMAIL'
		if self.phone == '':
			self.phone = 'NO PHONE'
		# print(self.name)
		# print(self.email)
		# print(self.phone)
		# sys.exit()