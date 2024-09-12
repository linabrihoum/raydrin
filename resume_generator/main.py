from src import pdf_extractor, preprocess_text

def main():
    # Step 1: Extract PDFs to raw text with dynamic folder paths
    input_pdf_dir = 'resume_generator/data/resumes_raw/pdf_resumes'
    output_text_dir = 'resume_generator/data/resumes_raw/text_resumes'
    pdf_extractor.extract_all_pdfs(input_dir=input_pdf_dir, output_dir=output_text_dir)
    
    # Step 2: Clean the extracted text
    preprocess_text.process_all_resumes(input_dir=output_text_dir, output_dir='resume_generator/data/resumes_clean')

if __name__ == "__main__":
    main()
