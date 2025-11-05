import io
import re
from typing import Optional
from PyPDF2 import PdfReader
from docx import Document


def load_text_from_pdf(file_bytes: bytes) -> str:
	try:
		reader = PdfReader(io.BytesIO(file_bytes))
		text = []
		for page in reader.pages:
			page_text = page.extract_text() or ""
			text.append(page_text)
		return "\n".join(text).strip()
	except Exception:
		return ""


def load_text_from_docx(file_bytes: bytes) -> str:
	try:
		doc = Document(io.BytesIO(file_bytes))
		text = [p.text for p in doc.paragraphs]
		return "\n".join(text).strip()
	except Exception:
		return ""


def extract_plain_text(filename: str, file_bytes: bytes) -> str:
	name = filename.lower()
	if name.endswith(".pdf"):
		return load_text_from_pdf(file_bytes)
	if name.endswith(".docx"):
		return load_text_from_docx(file_bytes)
	if name.endswith(".txt"):
		try:
			return file_bytes.decode("utf-8", errors="ignore")
		except Exception:
			return ""
	return ""


def clean_text(s: str) -> str:
	s = s.lower()
	s = re.sub(r"[^\w\s#+\-./]", " ", s)
	s = re.sub(r"\s+", " ", s).strip()
	return s