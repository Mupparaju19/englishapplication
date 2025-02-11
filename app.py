import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    print("Error: OPENAI_API_KEY is missing. Please check your .env file.")
    exit(1)

def get_correction(user_input):
    """Corrects grammar mistakes in the user's sentence and explains errors."""
    prompt = f"Correct the grammar in this sentence and explain the mistakes: \nUser: {user_input}\nBot:"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an English tutor. Help users improve their grammar."},
                      {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error processing request: {e}"

def get_vocab_explanation(word):
    """Explains the meaning of a given word in simple English."""
    prompt = f"Explain the meaning of the word '{word}' in simple English with an example sentence."
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an English tutor."},
                      {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error processing request: {e}"

def get_conversation_response(user_input):
    """Generates a natural English conversation response."""
    prompt = f"Respond naturally to this message in a friendly and engaging way: {user_input}"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a friendly chatbot helping people practice English."},
                      {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error processing request: {e}"

def main():
    print("Welcome to the English Learning Chatbot! Type 'exit' to stop.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye! Keep practicing your English!")
            break
        
        # Check for special commands
        if user_input.startswith("define "):  # Example: "define ubiquitous"
            word = user_input.split(" ", 1)[1]
            response = get_vocab_explanation(word)
        elif user_input.startswith("correct "):  # Example: "correct I has a apple"
            sentence = user_input.split(" ", 1)[1]
            response = get_correction(sentence)
        else:
            response = get_conversation_response(user_input)
        
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
