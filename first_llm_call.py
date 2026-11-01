from dotenv import load_dotenv
from google import genai
import os
import time

load_dotenv()

api_key= os.getenv('GEMINI_API_KEY')

if api_key is not None:
    print('API key found!')
    client= genai.Client(api_key=api_key)
    start_time= time.perf_counter()
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents= 'Explain the difference between revenue and profit in two sentences'
    )
    end_time= time.perf_counter()
    print(response.text)
    print(response.usage_metadata)
    elapsed_time = end_time-start_time
    print(f"Gemini response time: {elapsed_time:.2f}")
else:
    print('API key not found')


