import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

def generate_sql_query(natural_language_query):
    """
    Generate an SQL query from a natural language query using OpenAI's API.

    Parameters:
        natural_language_query (str): The natural language query to convert.

    Returns:
        str: The generated SQL query.
    """
    prompt = (
        "Convert the following natural language query into an SQL query for a PostgreSQL database:\n\n"
        f"Natural Language Query: {natural_language_query}\n"
        "SQL Query:"
    )

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=[";", "\n"]
        )
        sql_query = response.choices[0].text.strip()
        return sql_query
    except Exception as e:
        print(f"Error generating SQL query: {e}")
        return ""

