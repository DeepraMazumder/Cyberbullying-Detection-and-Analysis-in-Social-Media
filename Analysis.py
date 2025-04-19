
from dotenv import load_dotenv
import google.generativeai as genai
import os
import re

# Load the API key from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure the API key for Google Generative AI
genai.configure(api_key=api_key)

# Initialize the Generative Model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Function to count words in the input text
def count_words(text):
    return len(text.split())

# Define the prompt function
def analyze_cyberbullying(text):
    total_words = count_words(text)
    prompt = (
        "Classify the given sentence into one of the following cyberbullying CATEGORIES: Race/Ethnicity, Gender/Sexual, Religion, Harassment, Flaming/Trolling, Dissing;"
        "IF the CATEGORY is Race/Ethnicity, Gender/Sexual or Religion, then write the TYPE as Identity-based;"
        "IF the CATEGORY is Harassment, Flaming/Trolling, or Dissing, then write the TYPE as Behavioral-based;"
        "Write CATEGORY first, then SUB CATEGORY on separate lines;"
        "If the sentence is not cyberbullying, respond with 'Not cyberbullying';"
        "SUGGESTED ALTERNATIVES: Suggest only 2 neutral/safer ways to express the sentence - no yapping;"
        "HARMFUL CONTENT IDENTIFICATION: Display only the individual harmful words from the sentence as a list, each marked with ⚠️. Do not include phrases, explanations, or additional text;"
        f"TOTAL WORDS: {total_words};"
        "FLAGGED PERCENTAGE: Display the percentage along with the breakdown like this: 20% (2 Harmful Words / 10 Total Words);"
        "REASON: Briefly justify why the message was flagged and its cyberbullying category - no yapping;"
        f"Sentence: {text}"
    )

    response = model.generate_content([prompt])
    cleaned_output = re.sub(r'\*\*|\*|## |"', '', response.text)
    return cleaned_output.strip()
