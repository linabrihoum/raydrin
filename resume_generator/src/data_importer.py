import os

# Path to the text resumes
text_resume_dir = os.path.join('..', 'data', 'text_resumes')

# Function to load and preprocess text resumes
def load_text_resumes():
    resume_data = []
    for text_file in os.listdir(text_resume_dir):
        if text_file.endswith('.txt'):
            file_path = os.path.join(text_resume_dir, text_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                resume_text = f.read()
                resume_data.append(resume_text)
    return resume_data

# Preprocess the loaded text resumes (if necessary)
def preprocess_resumes(resume_data):
    # Example preprocessing steps: lowercasing, removing special characters, etc.
    cleaned_resumes = []
    for resume in resume_data:
        resume = resume.lower()  # Lowercase the text
        resume = ''.join([char for char in resume if char.isalnum() or char.isspace()])  # Remove special characters
        cleaned_resumes.append(resume)
    return cleaned_resumes

if __name__ == "__main__":
    resumes = load_text_resumes()
    cleaned_resumes = preprocess_resumes(resumes)
    print(f"Loaded and cleaned {len(cleaned_resumes)} resumes.")
