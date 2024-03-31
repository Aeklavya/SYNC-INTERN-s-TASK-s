import random

# Step 1: Decide what type of chatbot is best for you.
# For simplicity, we'll continue with a rule-based chatbot.

# Step 2: Determine your chatbot key performance indicator.
# For this enhanced chatbot, we'll focus on user engagement and learning, measured by the number of successful interactions and the usefulness of provided information.

# Step 3: Understand user needs.
# Our chatbot will handle basic greetings, provide information about Python concepts, and give example programs.

# Step 4: Give your chatbot a personality.
# We'll maintain the friendly and helpful personality for our chatbot.

# Step 5: Plan your chatbot flow.
# The flow will include greeting the user, responding to their input, providing information about Python concepts, and giving example programs.

# Step 6: Design your chatbot.

def chatbot(message):
    greetings = ["hello", "hi", "hey", "howdy"]
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! What can I do for you?",
        "hey": "Hey! How can I assist you?",
        "howdy": "Howdy! What's on your mind?",
        "what is your name?": "My name is ChatBot. Nice to meet you!",
        "how are you?": "I'm just a bot, but I'm here to help you!",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome!",
        "variables": "In Python, variables are used to store data values. You can create a variable by assigning a value to it. For example:\n\nx = 10\nname = 'Alice'",
        "conditionals": "Conditional statements are used to perform different actions based on different conditions. The 'if' statement is a commonly used conditional statement in Python. For example:\n\nx = 10\nif x > 5:\n    print('x is greater than 5')",
        "loops": "Loops are used to execute a block of code repeatedly. There are two main types of loops in Python: 'for' loops and 'while' loops. For example:\n\n# Example of a for loop\nfor i in range(5):\n    print(i)\n\n# Example of a while loop\nx = 0\nwhile x < 5:\n    print(x)\n    x += 1",
        "functions": "Functions are a block of reusable code that performs a specific task. You can define your own functions in Python using the 'def' keyword. For example:\n\ndef greet(name):\n    print('Hello, ' + name)\n\ngreet('Alice')"
    }
    
    # Convert message to lowercase for case insensitivity
    message = message.lower()
    
    # Check if message is a greeting, has predefined response, or requests Python information
    if message in responses:
        return responses[message]
    elif "bye" in message:
        return responses["bye"]
    elif "thank you" in message:
        return responses["thank you"]
    elif "variables" in message:
        return responses["variables"]
    elif "conditionals" in message:
        return responses["conditionals"]
    elif "loops" in message:
        return responses["loops"]
    elif "functions" in message:
        return responses["functions"]
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

# Step 7: Preview and test your chatbot.
# Let's test the chatbot with some sample inputs.
print(chatbot("hello"))
print(chatbot("What is your name?"))
print(chatbot("How are you?"))
print(chatbot("Goodbye"))
print(chatbot("Thank you"))
print(chatbot("Tell me about variables"))
print(chatbot("Explain conditionals"))
print(chatbot("Show me some loops"))
print(chatbot("Define functions"))

# Step 8: Target your chatbot.
# This chatbot can be used as a learning tool for beginners to understand basic Python concepts.

# Step 9: Measure and optimize chatbot performance.
# Collect user feedback and track interactions to improve the chatbot's responses and add more features.

