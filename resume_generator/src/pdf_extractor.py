import os
import fitz  # PyMuPDF

# Extract text from PDFs using PyMuPDF
def extract_text_from_pdf(pdf_path):
    try:
        with fitz.open(pdf_path) as pdf_file:
            text = ""
            for page_num in range(len(pdf_file)):
                page = pdf_file.load_page(page_num)
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

# Process all PDFs with dynamic input and output directories
def extract_all_pdfs(input_dir, output_dir):
    # Ensure text output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for pdf_file in os.listdir(input_dir):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, pdf_file)
            text = extract_text_from_pdf(pdf_path)
            if text:
                text_filename = os.path.join(output_dir, f"{os.path.splitext(pdf_file)[0]}.txt")
                with open(text_filename, 'w', encoding='utf-8') as f:
                    f.write(text)
                print(f"Extracted text from {pdf_file} and saved to {text_filename}")
