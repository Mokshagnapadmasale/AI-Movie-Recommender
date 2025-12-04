import os 
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HUGGING_API_KEY_TOKEN = os.getenv('HUGGING_API_KEY')

OPENAI_MODEL_NAME = 'gpt-5-nano'
GROQ_MODEL_NAME = 'llama-3.3-70b-versatile'

OPENAI_EMBEDDING_MODEL_NAME = 'text-embedding-3-large'
COHERE_EMBEDDING_MODEL_NAME = 'embed-v4.0'
HUGGING_EMBEDDING_MODEL_NAME = 'Qwen/Qwen3-Embedding-8B'