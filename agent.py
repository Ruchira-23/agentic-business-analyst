from dotenv import load_dotenv
from google import genai
from google.genai import types
from datatools import get_revenue
from analytics import percent_change
import os

load_dotenv()
api_key=os.getenv('GEMINI_API_KEY')

if not api_key:
    raise ValueError('GEMINI_API_KEY is missing')

client= genai.Client(api_key=api_key)

