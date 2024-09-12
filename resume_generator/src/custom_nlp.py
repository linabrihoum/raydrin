from scripts.data_importer import load_text_resumes, preprocess_resumes
from your_nlp_model import nlp

# Load and preprocess resumes
raw_resumes = load_text_resumes()
cleaned_resumes = preprocess_resumes(raw_resumes)

# Apply NLP model to each resume
for resume in cleaned_resumes:
    result = nlp(resume)  # Use your custom NLP model here
    print(result)
