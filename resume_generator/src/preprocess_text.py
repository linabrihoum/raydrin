import os
import re

def preprocess_text(text):
    """
    Cleans the raw text extracted from the resume PDF.
    Args:
        text (str): The raw text extracted from a resume.
    Returns:
        str: Cleaned and preprocessed text.
    """
    # Cleaning steps
    text = re.sub(r'\n+', '\n', text)  # Replace multiple newlines with a single newline
    text = re.sub(r'\t+', ' ', text)  # Replace tabs with a space
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = re.sub(r'[^a-zA-Z0-9,.?!\-()&%\s]', '', text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\s([,.?!])', r'\1', text)  # Standardize spacing after punctuation
    
    return text

def save_cleaned_text(file_path, cleaned_text, output_dir):
    """
    Saves cleaned text into a specified output directory.
    Args:
        file_path (str): The original file path of the resume.
        cleaned_text (str): The cleaned and preprocessed text.
        output_dir (str): The directory to save cleaned resumes.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Get the filename from the original file path
    file_name = os.path.basename(file_path)
    
    # Create the output file path
    cleaned_file_path = os.path.join(output_dir, file_name)
    
    # Write the cleaned text to the output directory
    with open(cleaned_file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_text)
    
    print(f"Cleaned text saved to: {cleaned_file_path}")

def process_all_resumes(input_dir, output_dir):
    """
    Processes all resumes from the input directory, cleans them, and saves the cleaned versions.
    Args:
        input_dir (str): Directory containing the raw resume text files.
        output_dir (str): Directory to save the cleaned resume text files.
    """
    # Loop through each file in the input directory
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        
        # Read the raw text
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_text = f.read()
        
        # Clean the text
        cleaned_text = preprocess_text(raw_text)
        
        # Save the cleaned text to the output directory
        save_cleaned_text(file_path, cleaned_text, output_dir)

# Example usage:
process_all_resumes('data/resumes_raw', 'data/resumes_clean')
