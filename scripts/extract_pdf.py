import PyPDF2
import os
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def extract_questions_from_provas(provas_directory):
    questions = []
    for filename in os.listdir(provas_directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(provas_directory, filename)
            text = extract_text_from_pdf(pdf_path)
            
            # Extract questions from the text
            extracted_questions = identify_questions(text)
            
            # Add filename to each question
            for q in extracted_questions:
                q["filename"] = filename
                questions.append(q)
    
    return questions

def identify_questions(text):
    questions = []
    
    # Look for patterns like "1." or "Questão 1" that typically start questions
    question_pattern = re.compile(r'(?:^|\n)\s*(?:(\d+)[\.\)]\s*|[Qq]uest[ãa]o\s+(\d+)[\s:\-]*)(.*?)(?=\n\s*(?:\d+[\.\)]|[Qq]uest[ãa]o\s+\d+)|$)', re.DOTALL)
    
    for match in question_pattern.finditer(text):
        # Get question number (from group 1 or 2)
        question_num = match.group(1) if match.group(1) else match.group(2)
        
        # Get question text
        question_text = match.group(3).strip()
        
        questions.append({
            "question_number": question_num,
            "text": question_text
        })
    
    return questions

if __name__ == "__main__":
    provas_directory = "../data/provas"
    extracted_questions = extract_questions_from_provas(provas_directory)
    
    # Print or save the extracted questions as needed
    for question in extracted_questions:
        print(f"From {question['filename']}:\n{question['text']}\n")