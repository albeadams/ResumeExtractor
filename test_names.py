import unittest
import os

from resume_extractor import ResumeExtractor
from info_extrator import InfoExtractor

TEST_DIR = 'test_resumes'

class TestStringMethods(unittest.TestCase):

	def _valid_xml(self, c):
			#https://stackoverflow.com/questions/8733233/filtering-out-certain-bytes-in-python
	    codepoint = ord(c)
	    return (0x20 <= codepoint <= 0xD7FF or
	        		codepoint in (0x9, 0xA, 0xD) or
	        		0xE000 <= codepoint <= 0xFFFD or
	        		0x10000 <= codepoint <= 0x10FFFF)

	def setUp(self):
		self.test_pdfs = {}

		self.i = InfoExtractor
		path_pdfs = [f for f in os.listdir(TEST_DIR) if os.path.isfile(os.path.join(TEST_DIR, f))]

		r = ResumeExtractor(path_pdfs)
		r.convert_to_text()

		for filename, val in r.pdf_txt.items():
			cleaned_string = ''.join(c for c in val if self._valid_xml(c))
			i.extract_info(cleaned_string)
			self.test_pdfs[filename] = (i.name, i.email, i.phone)

		correct_vals = {
			'1.pdf': ('Damien Smith', 'email@example.com', '(890) 555-0401')
			'2.pdf':
			'3.pdf':
			'4.pdf':
			'5.pdf':
			'6.pdf':
			'7.pdf':
			'8.pdf':
			'9.pdf':
			'10.pdf':
			'11.pdf':
			'12.pdf':
			'13.pdf':
			'14.pdf':
			'15.pdf':
		}

	def test_name_phone_emai(self):
		for filename, resume_vals in self.test_pdfs.items():

		#TODO finish actual pdf values and test case to check


if __name__ == '__main__':
	unittest.main()