
# pdfmind docs:
#https://pdfminersix.readthedocs.io/en/latest/

import os, sys
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

class ResumeExtractor(object):

	def __init__(self, pdf_lst):
		# initialize with list of paths to PDFs
		self.pdf_lst = pdf_lst

		self.pdf_txt = {}


	def convert_to_text(self):
		#self.txt_files = []

		for file in self.pdf_lst:
			out_string = StringIO()

			with open(file, 'rb') as f:
				parser = PDFParser(f)
				doc = PDFDocument(parser)
				rsrcmgr = PDFResourceManager()
				device = TextConverter(rsrcmgr, out_string, codec='utf-8', laparams=LAParams())
				interpreter = PDFPageInterpreter(rsrcmgr, device)
				for page in PDFPage.create_pages(doc):
					interpreter.process_page(page)

			temp_text = ""
			for line in out_string.getvalue().split('\n'):
				temp_word = ""
				for word in line.split():
					if word.isupper():
						temp_word += word.capitalize() + ' '
					else:
						temp_word += word + ' '
				temp_text += temp_word + '\n'

			#self.txt_files.append(temp_text)
			self.pdf_txt[file] = temp_text