resume_generator/
│
├── data/
│   ├── pdfs/                 # Folder containing the raw PDF resumes from the dataset
│   ├── text_resumes/          # Folder for storing extracted text from PDF resumes
│   └── job_descriptions/      # Folder for storing job descriptions
│
├── src/
│   ├── pdf_extractor.py       # Script to extract text from PDFs
│   ├── custom_nlp.py          # Fine-tuned NLP using LLaMA3.1 for tailoring resumes to job descriptions
│   ├── data_importer.py       # Imports and preprocesses resume data for the NLP pipeline
│   ├── latex_formatter.py     # Formats the tailored resume to a LaTeX template
│   ├── compile_latex.py       # Compiles the LaTeX resume into PDF format
│   └── llama_finetune.py      # Script to fine-tune LLaMA3.1 with resume data
│
├── results/
│   ├── generated_resumes/     # Output folder for generated LaTeX resumes and PDFs
│
├── main.py                    # Main entry point for the project
├── README.md                  # Project overview and instructions
├── requirements.txt           # Project dependencies



+------------------------------------------+
|              PDF Resume Data             |
+------------------------------------------+
                  |
                  v
       +---------------------------+
       |    Text Extraction (PDFs)  |
       +---------------------------+
                  |
                  v
       +---------------------------+
       |   Preprocessing (Cleaning) |
       +---------------------------+
                  |
                  v
       +-----------------------------------------------+
       |        Custom NLP Model (LLaMA3.1 + SpaCy)     |
       |  Tailoring Resume Text to Job Descriptions     |
       +-----------------------------------------------+
                  |
                  v
      +-----------------------------------+
      | LaTeX Formatter (Resume Sections) |
      +-----------------------------------+
                  |
                  v
      +-----------------------------+
      |  Compile LaTeX into PDF      |
      +-----------------------------+
                  |
                  v
      +-----------------------------+
      |    Final PDF Resume Output   |
      +-----------------------------+


