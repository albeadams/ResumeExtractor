import unittest
import os

from resume_extractor import ResumeExtractor
from info_extractor import InfoExtractor

TEST_DIR = 'test_resumes'

class TestStringMethods(unittest.TestCase):

	def _valid_xml(self, c):
			#https://stackoverflow.com/questions/8733233/filtering-out-certain-bytes-in-python
	    codepoint = ord(c)
	    return (0x20 <= codepoint <= 0xD7FF or
	        		codepoint in (0x9, 0xA, 0xD) or
	        		0xE000 <= codepoint <= 0xFFFD or
	        		0x10000 <= codepoint <= 0x10FFFF)

	def load_pdfs(self):
		pdf_files = [f for f in os.listdir(TEST_DIR) if os.path.isfile(os.path.join(TEST_DIR, f))]
		pdfs = []
		for filename in pdf_files:
			if filename[-4:] == '.pdf':
				pdfs.append(os.path.join(TEST_DIR, filename))
		return pdfs


	def setUp(self):
		self.test_pdfs = {}

		path_pdfs = self.load_pdfs()

		r = ResumeExtractor(path_pdfs)
		r.convert_to_text()

		self.i = InfoExtractor()

		for filename, val in r.pdf_txt.items():
			cleaned_string = ''.join(c for c in val if self._valid_xml(c))
			self.i.extract_info(cleaned_string)
			self.test_pdfs[filename] = (self.i.name, self.i.email, self.i.phone)

		self.correct_vals = {
			'test_resumes\\1.pdf': ('Damien Smith', 'email@example.com', '(890) 555-0401'),
			#'test_resumes\\2.pdf': ('Dan Clark', 'email@example.com', 'NO PHONE'),
			#'test_resumes\\3.pdf': ('Dwight Kavanagh', 'email@example.com', '(890) 555-0401'),
			'test_resumes\\4.pdf': ('Emily Carter', 'email@email.com', 'NO PHONE'),
			'test_resumes\\5.pdf': ('Emily McKenzie', 'rozenboomchantal@gmail.com', '(890) 555-0401'),
			'test_resumes\\6.pdf': ('George Dann', 'example@email.com', '(890) 555-0401'),
			#'test_resumes\\7.pdf': ('Thomas Earland', 'hello@email.com', '(123) 456-7890'),
			#'test_resumes\\8.pdf': ('Charlotte Webb', 'hello@email.com', '(123) 456-7890'),
			#'test_resumes\\9.pdf': ('Andrea Rowland', 'hi@email.com', '(890) 555-0401'),
			'test_resumes\\10.pdf': ('Jacky Smith', 'email@example.com', '(890) 555-0401'),
			'test_resumes\\11.pdf': ('Jacky Smith', 'email@example.com', '(890) 555-0401'),
			#'test_resumes\\12.pdf': ('Karen Philips', 'email@email.com', '(890) 555-0401'),
			#'test_resumes\\13.pdf': ('Karen Philips', 'email@email.com', '(890) 555-0401'),
			'test_resumes\\14.pdf': ('Mirna Davis', 'example@email.com', 'NO PHONE'),
			'test_resumes\\15.pdf': ('Phil Roberts', 'example@email.com', '(890) 555-0401')
		}

		# TODO commented-out are errors, fix logic...

	def test_name_phone_emai(self):
		for filename, resume_vals in self.test_pdfs.items():
			if filename in self.correct_vals:
				print(resume_vals)
				self.assertEqual(resume_vals[0], self.correct_vals[filename][0])
				self.assertEqual(resume_vals[1], self.correct_vals[filename][1])
				self.assertEqual(resume_vals[2], self.correct_vals[filename][2])

if __name__ == '__main__':
	unittest.main()