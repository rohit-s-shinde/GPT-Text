# OpenAI API
import openai
# Regular expressions
import re

# Set the OpenAI API key
openai.api_key = open("key.txt", "r").read().strip("\n")

# Function to generate a chat response using the OpenAI API
def chat(input, message_history, role="user"):
    message_history.append({"role": role, "content": f"{input}"})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )

    reply_content = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": f"{reply_content}"})
    return reply_content, message_history

# Initialize the message history
message_history = [{"role": "user", "content": """You are an interactive story game bot that proposes some hypothetical fantastical situation where the user needs to pick from 2-4 options that you provide. Once the user picks one of those options, you will then state what happens next and present new options, and this then repeats. If you understand, say, OK, and begin when I say "begin." When you present the story and options, present just the story and start immediately with the story, no further commentary, and then options like "Option 1:" "Option 2:" ...etc."""},
                   {"role": "assistant", "content": f"""OK, I understand. Begin when you're ready."""}]

# Generate a chat response with an initial message ("Begin")
reply_content, message_history = chat("begin", message_history)

# Repeat until user enters 'exit'
while True:
    print(reply_content)
    next_input = input("Enter your response: ")
    
    if next_input.lower()=="exit": break

    # Generate a chat response with the new input
    reply_content, message_history = chat(next_input, message_history)
