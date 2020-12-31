
import os

from resume_extractor import ResumeExtractor
from word_doc_creator import WordDocCreator

INPUT_DIR = "input_resumes"
OUTPUT_DIR = "output_resumes"

def load_pdfs():
	# Loads .pdf in INPUT_DIR, returns list
	pdf_files = [f for f in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, f))]
	pdfs = []
	for filename in pdf_files:
		if filename[-4:] == '.pdf':
			pdfs.append(os.path.join(INPUT_DIR, filename))
	return pdfs


if __name__ == "__main__":
	path_pdfs = load_pdfs()
	r = ResumeExtractor(path_pdfs)
	r.convert_to_text()

	d = WordDocCreator(r.pdf_txt)
	d.create_documents()