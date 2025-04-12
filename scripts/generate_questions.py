import os
import pandas as pd
from scripts.extract_pdf import extract_text_from_pdf
import PyPDF2  # Adicionado para processar arquivos PDF

def generate_questions_from_edital(edital_content, sample_questions):
    """
    Generate questions based on the content of the edital and the style of sample questions.
    """
    questions = []
    # Split the edital content into topics (assuming each line represents a topic)
    topics = [line.strip() for line in edital_content.split('\n') if len(line.strip()) > 0]

    for topic in topics:
        # Use the style of sample questions to generate new questions
        for sample in sample_questions:
            if "É verdadeiro ou falso que" in sample['question']:
                question = {
                    "question": f"É verdadeiro ou falso que: {topic}?",
                    "answer": "Certo"  # Default answer
                }
            else:
                question = {
                    "question": f"Com base no tópico '{topic}', assinale a alternativa correta.",
                    "answer": "Certo"  # Default answer
                }
            questions.append(question)

    return questions

def generate_questions_from_pdf(pdf_files, edital_file):
    questions = []
    
    # Extract text from each PDF file
    for pdf_file in pdf_files:
        text = extract_text_from_pdf(pdf_file)
        questions += generate_questions_from_text(text)

    # Generate additional questions based on the edital
    if os.path.exists(edital_file):
        with open(edital_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            edital_content = ""
            for page in reader.pages:
                edital_content += page.extract_text()
        
        # Use the content of the edital to generate questions
        sample_questions = generate_questions_from_text(edital_content)
        questions += generate_questions_from_edital(edital_content, sample_questions)
    else:
        raise FileNotFoundError(f"Edital file not found: {edital_file}")

    return questions

def generate_questions_from_text(text):
    # Generate questions based on simple rules
    questions = []
    sentences = text.split('.')
    
    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) > 20:  # Only consider meaningful sentences
            question = {
                "question": f"É verdadeiro ou falso que: {sentence}?",
                "answer": "Certo"  # Default answer
            }
            questions.append(question)
    
    return questions
    # Generate questions based on simple rules
    questions = []
    sentences = text.split('.')
    
    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) > 20:  # Only consider meaningful sentences
            question = {
                "question": f"É verdadeiro ou falso que: {sentence}?",
                "answer": "Certo"  # Default answer
            }
            questions.append(question)
    
    return questions

def save_questions_to_csv(questions, output_file):
    df = pd.DataFrame(questions, columns=["Question"])
    df['Answer'] = 'Certo'  # Default answer for true/false questions
    df.to_csv(output_file, index=False)