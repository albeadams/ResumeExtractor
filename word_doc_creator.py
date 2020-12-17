# to work with Word docs
#https://python-docx.readthedocs.io/en/latest/


import os
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUTPUT_DIR = "output_resumes"

class WordDocCreator(object):

	def __init__(self, pdf_txt_dict):
		self.pdf_txt_dict = pdf_txt_dict

	def _valid_xml(self, c):
			#https://stackoverflow.com/questions/8733233/filtering-out-certain-bytes-in-python
	    codepoint = ord(c)
	    return (0x20 <= codepoint <= 0xD7FF or
	        		codepoint in (0x9, 0xA, 0xD) or
	        		0xE000 <= codepoint <= 0xFFFD or
	        		0x10000 <= codepoint <= 0x10FFFF)


	def _create_header(self, name):
		header_name = self.document.add_paragraph(name)
		header_name.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER


	def create_documents(self):
		# currently only writes text extracted from pdf to word doc

		for filename, val in self.pdf_txt_dict.items():
			file = os.path.basename(filename)
			name = val[1]
			cleaned_string = ''.join(c for c in val[0] if self._valid_xml(c))
			self.document = Document()
			self._create_header(name)
			self.document.save(os.path.join(OUTPUT_DIR, file[:-4]+'.docx'))


