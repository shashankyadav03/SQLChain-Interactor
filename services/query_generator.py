import json
import requests
import os
from dotenv import load_dotenv
import hashlib
import logging

log = logging.getLogger(__name__)

def call_openai_api(prompt, api_key):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        'messages': prompt,
        'max_tokens': 100,
        'model': 'gpt-4o-mini',
        'temperature': 0
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        if "Unauthorized" in response.text:
            return f"Error: Unauthorized"
        return response.json()
    elif response.status_code == 400:
        return f"Error: Bad request"
    elif response.status_code == 404:
        return f"Error: Not found"
    elif response.status_code == 429:
        return f"Error: Rate limit exceeded"
    elif response.status_code == 401:
        return f"Error: Unauthorized"
    elif response.status_code == 403:
        return f"Error: Forbidden"
    else:
        return f"Error: {response.status_code}, {response.text}"

# Get API key from .env file from openai tag
def get_api_key():
    # Load environment variables from the .env file from main directory
    load_dotenv("../.env")
    return os.getenv("OPENAI_API_KEY")
    

def get_prompt(prompt_content,system_message):
    prompt = [
        {'role': 'user', 'content': prompt_content},
        {'role': 'system', 'content': system_message}
    ]
    return prompt

def write_response_to_cache(prompt_hash, response):
    cache_dir = 'utilities/cache'
    os.makedirs(cache_dir, exist_ok=True)
    cache_path = os.path.join(cache_dir, f'{prompt_hash}.json')
    with open(cache_path, 'w') as outfile:
        json.dump(response, outfile)

def read_response_from_cache(prompt_hash):
    cache_path = os.path.join('utilities/cache', f'{prompt_hash}.json')
    if os.path.exists(cache_path):
        with open(cache_path) as json_file:
            return json.load(json_file)
    return None

def hash_prompt(prompt_content):
    return hashlib.md5(prompt_content.encode()).hexdigest()

def get_message_content(data):
    print(data)
    return data['choices'][0]['message']['content']

# Test OpenAI API
def openai_api(prompt_content,system_message):
    api_key = get_api_key()
    prompt = get_prompt(prompt_content,system_message)
    prompt_hash = hash_prompt(prompt_content)
    
    # Check cache first
    cached_response = read_response_from_cache(prompt_hash)
    if cached_response:
        print("Cache hit. Returning cached response.")
        data = cached_response
    else:
        print("Cache miss. Calling API.")
        result = call_openai_api(prompt, api_key)
        write_response_to_cache(prompt_hash, result)
        data = result

    message_content = get_message_content(data)
    print(message_content)
    return message_content

def run_openai_api(prompt_content,system_message):
    log.info(f"Prompt: {prompt_content}")
    message_content = openai_api(prompt_content,system_message)
    return message_content

def generate_sql_query(natural_language_query, schema):
    """
    Generate an SQL query from a natural language query and schema using OpenAI's API

    Parameters:
        natural_language_query (str): The natural language query to convert.

    Returns:
        str: The generated SQL query.
    """
    system_message = "Give only SQL query. Nothing else, no markdown, no code, no comments."
    base_prompt = f"Convert the following natural language query into an SQL query using the given schema:\n\nQuery: {natural_language_query}\n\nSchema:\n{schema}"
    sql_query = run_openai_api(base_prompt, system_message)
    return sql_query

