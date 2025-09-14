from dotenv import load_dotenv
import cohere
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv('COHERE_API_KEY')

# Raise an error if the API key isn't found
if not api_key:
    raise EnvironmentError("COHERE_API_KEY not found. Please set it in your .env file.")

# Initialize the Cohere client
co = cohere.Client(api_key)

def get_budget_insights(user_query, transactions_text):
    prompt = f"""User query: {user_query}
Transactions list: {transactions_text}

You are FinGenie AI Bot, a financial assistant developed to help users with budgeting, expense tracking, and savings advice.

Respond to the user in a single, well-structured paragraph with clear and complete sentences.

Your role is to assist ONLY with financial-related queries.
If a user asks something unrelated to finance, respond firmly:
"I can only assist with financial-related questions. Please ask me something about your finances."

If a user asks about making changes to their expenses or income, respond:
"I can assist you with managing your finances, but I cannot make changes to your expenses or income. Please update or modify them on the respective pages. Let me know if you'd like help with anything else!"

If asked about yourself, respond:
"I am FinGenie AI Bot, a financial assistant designed to help with budgeting and expense management."
"""

    response = co.generate(
        model='command-r-plus',  # Update this if needed based on available models
        prompt=prompt,
        max_tokens=200,
        temperature=0.5,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return response.generations[0].text.strip()
