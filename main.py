import os
import csv
from scripts.extract_edital import extract_edital_content
from scripts.generate_questions import generate_questions_from_programmatic_content

def main():
    # Define paths
    pdf_folder = 'data/provas/'
    output_folder = 'output/'
    edital_file = 'data/provas/EDITAL2021.pdf'

    # Step 1: Extract programmatic content from the edital
    programmatic_content = extract_edital_content(edital_file)

    if not programmatic_content:
        print("Nenhum conteúdo programático foi encontrado no edital.")
        return

    # Step 2: Generate questions based on the programmatic content
    questions = generate_questions_from_programmatic_content(programmatic_content)

    # Step 3: Export questions to CSV
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, "programmatic_questions.csv")
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Pergunta", "Resposta"])
        for question in questions:
            writer.writerow([question["question"], question["answer"]])

    print(f"Total de questões geradas: {len(questions)}")

if __name__ == "__main__":
    main()