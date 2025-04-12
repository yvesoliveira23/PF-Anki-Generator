import csv

def classify_questions(questions):
    classified = {}

    for question in questions:
        # Access the text of the question
        question_text = question['question'].lower()

        # Example classification logic
        if 'certo' in question_text:
            subject = 'General Knowledge'
        elif 'direito' in question_text:
            subject = 'Law'
        else:
            subject = 'Other'

        # Add the question to the appropriate category
        if subject not in classified:
            classified[subject] = []
        classified[subject].append(question)

    return classified

def save_classified_questions(classified_questions, output_file):
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Pergunta', 'Classificação'])
        for classification, questions in classified_questions.items():
            for question in questions:
                writer.writerow([question, classification])

if __name__ == "__main__":
    # Example usage
    questions = [
        "A Constituição é a lei suprema do Brasil. Certo.",
        "O Brasil é uma monarquia. Errado.",
        "O direito à vida é garantido pela Constituição. Certo.",
        "A pena de morte é permitida no Brasil. Errado."
    ]

    classified = classify_questions(questions)
    save_classified_questions(classified, '../output/classified_questions.csv')