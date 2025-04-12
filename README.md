# PF-Anki-Generator

PF-Anki-Generator is a Python project designed to automate the generation of Anki flashcards from PDF exams related to the Polícia Federal (PF) contests. The project utilizes advanced techniques, including LangChain and ChatGPT, to create a comprehensive set of questions based on existing exams and additional online resources.

## Project Structure

```bash
PF-Anki-Generator
├── data
│   ├── provas
│   │   ├── prova1.pdf
│   │   ├── prova2.pdf
│   │   ├── prova3.pdf
│   │   └── edital.txt
├── output
│   ├── direito_constitucional.csv
│   ├── raciocinio_logico.csv
│   ├── direito_penal.csv
│   └── ...
├── scripts
│   ├── extract_pdf.py
│   ├── generate_questions.py
│   ├── classify_questions.py
│   ├── export_to_csv.py
│   └── langchain_integration.py
├── requirements.txt
├── README.md
└── main.py
```

## Features

- **PDF Extraction**: Extracts questions and text from provided PDF exams.
- **Question Generation**: Generates new questions based on extracted content and online resources.
- **Classification**: Classifies questions into categories based on subjects and difficulty levels.
- **CSV Export**: Formats questions into CSV files suitable for Anki import.
- **AI Integration**: Utilizes LangChain and ChatGPT for enhanced question generation.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/yvesoliveira23/PF-Anki-Generator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd PF-Anki-Generator
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your PDF exams in the `data/provas` directory.
2. Update the `edital.txt` file with the latest edital information.
3. Run the main script to start the question generation process:

   ```bash
   python main.py
   ```

## Output

The generated questions will be saved in the `output` directory in CSV format, organized by subject.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you would like to add.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
