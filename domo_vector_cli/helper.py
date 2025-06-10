# PDF extraction using Fitz (PyMuPDF)
import fitz  # PyMuPDF
from document_models import ExtractedDocument


def extract_pdf_text_and_metadata(pdf_path):
    """
    Extracts all text and metadata from a PDF file using PyMuPDF (Fitz).
    Returns a standardized document dict with keys:
      - 'text': full text content (str)
      - 'file_path': the path to the PDF file (str)
      - 'metadata': dict of PDF metadata (dict)
      - 'source_type': always 'pdf' for this extractor (str)
    """
    doc = fitz.open(pdf_path)
    metadata = doc.metadata
    text = "\n".join(page.get_text() for page in doc)
    doc.close()
    return ExtractedDocument(
        text=text,
        file_path=pdf_path,
        metadata=metadata,
        source_type="pdf",
    )
