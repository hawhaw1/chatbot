# Simple chatbot program
# It reads user input and replies based on some keywords

import json  # to load responses from a file
import random  # to pick random replies from a list

def load_responses():
    # Open the JSON file and load all the questions and answers
    with open('responses.json', 'r') as file:
        data = json.load(file)
    return data

def get_response(user_input, responses):
    # Change user input to lowercase so matching is easier
    user_input = user_input.lower()

    # Check each intent (like greetings, bye, thanks)
    for intent in responses:
        # Go through all example phrases (patterns) for this intent
        for pattern in responses[intent]['patterns']:
            # If pattern is found in user input
            if pattern in user_input:
                # Pick a random response from the list
                return random.choice(responses[intent]['responses'])
    # If no pattern matched, say you didn't understand
    return "Sorry, I don't get that. Can you say it another way?"

def main():
    print("ChatBot: Hey! Type 'quit' to stop talking.")

    # Load all responses from JSON file once at start
    responses = load_responses()

    while True:
        user_input = input("You: ")

        # If user wants to quit, say bye and stop the program
        if user_input.lower() == 'quit':
            print("ChatBot: Bye! Take care!")
            break

        # Get a response based on what user typed
        reply = get_response(user_input, responses)

        # Print the chatbot reply
        print("ChatBot:", reply)

if __name__ == "__main__":
    main()
