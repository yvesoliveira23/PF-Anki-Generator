import csv
import os

def export_questions_to_csv(questions, output_file):
    """Exports a list of questions to a CSV file in Anki format."""
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for question in questions:
            writer.writerow([question['question'], question['answer']])

def main():
    # Example questions for demonstration purposes
    questions = [
        {'question': 'O Brasil é uma república federativa?', 'answer': 'Certo'},
        {'question': 'A Constituição de 1988 é a primeira do Brasil?', 'answer': 'Errado'},
        # Add more questions as needed
    ]

    # Define output directory and ensure it exists
    output_dir = '../output'
    os.makedirs(output_dir, exist_ok=True)

    # Export questions to CSV files for each subject
    export_questions_to_csv(questions, os.path.join(output_dir, 'direito_constitucional.csv'))
    export_questions_to_csv(questions, os.path.join(output_dir, 'raciocinio_logico.csv'))
    export_questions_to_csv(questions, os.path.join(output_dir, 'direito_penal.csv'))

if __name__ == '__main__':
    main()