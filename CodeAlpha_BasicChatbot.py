def get_bot_response(user_message):
    """
    An expanded rule-based mapping function using clean if-elif logic
    to handle comprehensive user conversational intents.
    """
    # Normalize user input to lowercase and remove extra spacing
    processed_message = user_message.strip().lower()

    # --- STANDARD GREETINGS ---
    if processed_message in ["hello", "hi", "hey", "sup", "yo"]:
        return "Hi there! How can I help you today?"
        
    elif processed_message in ["how are you", "how's it going", "how are you doing"]:
        return "I'm doing great, thank you for asking! How are you?"

    # --- NEW DATA: EMOTION & WELLBEING FAQS ---
    elif processed_message in ["i am good", "i'm fine", "doing well", "good"]:
        return "Awesome! Glad to hear that. What are we working on today?"
        
    elif processed_message in ["i am bored", "bored"]:
        return "Bored? Let's fix that! You can ask me to tell you a joke or a programming fact."

    # --- NEW DATA: PROJECT & INTERNSHIP SCOPE ---
    elif processed_message in ["what is this project", "project scope"]:
        return "This is Task 4 for the CodeAlpha Python Internship, demonstrating a rule-based AI system."
        
    elif processed_message in ["what language are you written in", "what is python"]:
        return "I am written entirely in Python 3! It is an amazing language for automation and AI development."

    # --- NEW DATA: UTILITY & FUN COMMANDS ---
    elif processed_message in ["tell me a joke", "joke"]:
        return "Why do programmers wear glasses? Because they can't C#! 😂"
        
    elif processed_message in ["programming fact", "fact"]:
        return "Fun Fact: The first computer bug was an actual real moth found trapped in a relay by Grace Hopper in 1947!"

    # --- STANDARD ASSISTANCE & IDENTITY ---
    elif processed_message in ["what is your name", "who are you"]:
        return "I am the CodeAlpha Automation Assistant, your friendly rule-based chatbot."
        
    elif processed_message in ["help", "tasks", "commands"]:
        return ("You can talk to me using various phrases! Try asking: 'joke', 'programming fact', "
                "'project scope', 'how are you', or 'bye'.")

    # --- CLOSING GREETINGS ---
    elif processed_message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a fantastic day ahead!"
        
    # Fallback option if the message doesn't match any rules
    else:
        return "I'm sorry, I'm a basic rule-based bot and didn't quite catch that. Try saying 'help' to see what I can do!"

def run_chatbot():
    """
    Main function containing the application loop and handling console input/output.
    """
    print("=======================================")
    print("      CodeAlpha Basic Chatbot UI       ")
    print("=======================================")
    print("System: Booting up...")
    print("Bot: Hello! Type your message below to chat.")
    print("     (Type 'bye' or 'exit' to leave the chat)")
    print("---------------------------------------")

    # Continuous application loop
    while True:
        # Capture input from the user
        user_input = input("You: ")
        
        # Check if the input is completely empty
        if not user_input.strip():
            print("Bot: Please type something so I can respond!")
            print("-" * 40)
            continue
            
        # Get response using our rule function
        bot_reply = get_bot_response(user_input)
        
        # Print the chatbot's output response
        print(f"Bot: {bot_reply}")
        print("-" * 40)
        
        # Break out of the loop safely if the user wants to end the conversation
        if user_input.strip().lower() in ["bye", "goodbye", "exit", "quit"]:
            break

if __name__ == "__main__":
    run_chatbot()