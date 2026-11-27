from dotenv import load_dotenv
from google import genai
from google.genai import types
from datatools import get_revenue
from analytics import percent_change
import os

load_dotenv() #load env variables
api_key=os.getenv('GEMINI_API_KEY')  #load the key from env variable

if not api_key:
    raise ValueError('GEMINI_API_KEY is missing') #checking if key value is captured or not

client = genai.Client( 
    #this function is to handle attempts and timeframe for trial
    api_key=api_key,
    http_options=types.HttpOptions(
        timeout=30000, #HTTP request timeout in milliseconds
        retry_options=types.HttpRetryOptions(
            attempts=1 #so that SDK does not attemp more than 1 retries
        )
    )
)

config= types.GenerateContentConfig(
        tools=[get_revenue, percent_change]  #registered get_revenue and percent_change as a tool in Gemini SDK 
)
    
try:
    chat = client.chats.create(
        model="gemini-3.5-flash-lite", #selected this model after gemini-2.5-flash-lite, gemini-3.8-flash
        config=config
    )

    while True:  #adding a while loop to make it an interactive chat bot situation
        user_input = input("Ask your Business Analyst a question:")

        if not user_input.strip():
         print("Please enter a valid question")
        
        elif user_input.strip().lower()=='exit':
            break

        else:
            response = chat.send_message(user_input)
            print(response.text)
    

except Exception as e:
    print(f"Agent request failed: {e}")
