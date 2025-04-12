import os
from scripts.extract_pdf import extract_questions_from_provas
from scripts.generate_questions import generate_questions_from_pdf
from scripts.classify_questions import classify_questions
from scripts.export_to_csv import export_questions_to_csv

def find_edital_file(pdf_folder):
    # Search for a file that starts with "Edital" (case-insensitive) and ends with ".pdf"
    for file in os.listdir(pdf_folder):
        if file.lower().startswith("edital") and file.lower().endswith(".pdf"):
            return os.path.join(pdf_folder, file)
    # Log the files in the folder for debugging
    files_in_folder = os.listdir(pdf_folder)
    print(f"Files in folder '{pdf_folder}': {files_in_folder}")
    raise FileNotFoundError("No edital file found in the specified folder.")

def main():
    # Define paths
    pdf_folder = 'data/provas/'
    output_folder = 'output/'

    # Step 1: Extract questions from PDF files
    extracted_questions = extract_questions_from_provas(pdf_folder)

    # Step 2: Filter PDF files based on naming rules
    all_files = os.listdir(pdf_folder)
    print(f"All files in '{pdf_folder}': {all_files}")  # Log all files in the folder

    pdf_files = [
        os.path.join(pdf_folder, f) for f in all_files
        if f.lower().endswith('.pdf') and 
           ('agente' in f.lower() or 'perito' in f.lower()) and 
           'gabarito' not in f.lower()
    ]
    print(f"Filtered PDF files: {pdf_files}")  # Log filtered PDF files

    if not pdf_files:
        raise ValueError("No valid PDF files found to process.")

    # Step 3: Locate the edital file
    edital_file = find_edital_file(pdf_folder)

    # Step 4: Generate new questions based on extracted content and edital
    new_questions = generate_questions_from_pdf(pdf_files, edital_file)

    # Step 5: Classify the generated questions
    classified_questions = classify_questions(new_questions)

    # Step 6: Export classified questions to CSV files
    os.makedirs(output_folder, exist_ok=True)
    for subject, questions in classified_questions.items():
        output_file = os.path.join(output_folder, f"{subject}.csv")
        export_questions_to_csv(questions, output_file)

if __name__ == '__main__':
    main()