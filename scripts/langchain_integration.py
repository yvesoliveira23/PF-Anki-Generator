from langchain import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

# Load your OpenAI API key from an environment variable or directly
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI model
llm = OpenAI(api_key=OPENAI_API_KEY)

# Define a prompt template for generating questions
prompt_template = PromptTemplate(
    input_variables=["content"],
    template="Generate a true or false question based on the following content: {content}"
)

# Create a chain for generating questions
question_chain = LLMChain(llm=llm, prompt=prompt_template)

def generate_questions_from_content(content):
    """
    Generate a list of true or false questions from the provided content.
    
    Args:
        content (str): The content to generate questions from.
        
    Returns:
        list: A list of generated questions.
    """
    questions = []
    for paragraph in content.split('\n'):
        if paragraph.strip():  # Avoid empty lines
            question = question_chain.run(paragraph)
            questions.append(question)
    return questions

if __name__ == "__main__":
    # Example usage
    sample_content = "The Constitution of Brazil was enacted in 1988. It is the supreme law of the country."
    generated_questions = generate_questions_from_content(sample_content)
    for q in generated_questions:
        print(q)