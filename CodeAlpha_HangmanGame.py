import random

def play_hangman():
    # 1. Predefined word list (5 words)
    word_bank = ["python", "internship", "developer", "cyber", "program"]
    
    # Randomly select a secret word and convert it to lowercase
    secret_word = random.choice(word_bank).lower()
    
    # Track guessed letters using a set for fast lookup
    guessed_letters = set()
    
    # Game rules configuration
    max_incorrect_guesses = 6
    incorrect_guesses_made = 0

    print("=======================================")
    print("   Welcome to CodeAlpha Hangman Game!  ")
    print("=======================================")
    print(f"I am thinking of a word. You have {max_incorrect_guesses} incorrect guesses allowed.")
    print("Let's begin!\n")

    # Main game loop
    while incorrect_guesses_made < max_incorrect_guesses:
        # Display the current state of the word (e.g., p _ t h o n)
        displayed_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                displayed_word.append(letter)
            else:
                displayed_word.append("_")
        
        current_progress = " ".join(displayed_word)
        print(f"Word progress: {current_progress}")
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses_made}")
        print(f"Guistered letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Check if the player has guessed all the letters
        if "_" not in displayed_word:
            print("\n🎉 Congratulations! You guessed the word correctly! 🎉")
            print(f"The word was indeed: {secret_word.upper()}")
            break

        # Get user input and handle validation
        guess = input("\nGuess a letter: ").strip().lower()

        # Input Validation: Must be exactly one alphabetical character
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Please enter a single alphabetical letter.")
            print("-" * 40)
            continue
            
        # Input Validation: Check if letter was already guessed
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter!")
            print("-" * 40)
            continue

        # Add the valid guess to our tracked set
        guessed_letters.add(guess)

        # Process the guess
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            incorrect_guesses_made += 1
            
        print("-" * 40)

    # If the loop finishes because they ran out of guesses
    else:
        print("\n💥 Game Over! You've run out of guesses. 💥")
        print(f"The correct word was: {secret_word.upper()}")

if __name__ == "__main__":
    play_hangman()