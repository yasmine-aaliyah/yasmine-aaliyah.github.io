import random

# === ASCII HANGMAN STAGES ===
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

# === LOAD WORDS ===
def load_words(filename="hangmanwords.txt"):
    try:
        with open(filename, "r") as f:
            words = [line.strip().lower() for line in f if line.strip()]
        if not words:
            raise ValueError("words.txt is empty bro!!")
        return words
    except FileNotFoundError:
        print("yo words.txt not found!! using fallback word list.")
        return ["python", "hangman", "keyboard", "monitor", "function", "variable"]

# === DISPLAY FUNCTIONS ===
def display_state(wrong_guesses, word, guessed_letters):
    print(HANGMAN_STAGES[wrong_guesses])
    print("\nWord: ", end="")
    print(" ".join(letter if letter in guessed_letters else "_" for letter in word))
    print(f"\nWrong guesses ({wrong_guesses}/6): {', '.join(sorted(guessed_letters - set(word))) or 'none'}")

# === CHECK WIN ===
def all_letters_revealed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# === MAIN GAME ===
def play_game(word):
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("\n🎮 NEW GAME STARTED!")
    print(f"The word has {len(word)} letters. good luck lol\n")

    while True:
        # Display current state
        display_state(wrong_guesses, word, guessed_letters)

        # Player input
        guess = input("\nGuess a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  one letter only bro, cmon.")
            continue

        # Already guessed?
        if guess in guessed_letters:
            print(f"⚠️  you already guessed '{guess}', pay attention!!")
            continue

        # In the word?
        if guess in word:
            guessed_letters.add(guess)
            print(f"✅ nice!! '{guess}' is in the word!")

            # All letters revealed? → WIN
            if all_letters_revealed(word, guessed_letters):
                display_state(wrong_guesses, word, guessed_letters)
                print(f"\n🎉 YOU WON!! the word was '{word}'. you absolute legend!!")
                return True

        else:
            # Not in word → wrong_guesses + 1
            guessed_letters.add(guess)
            wrong_guesses += 1
            print(f"❌ nope!! '{guess}' is not in the word.")

            # Wrong guesses == 6? → LOSE
            if wrong_guesses == max_wrong:
                display_state(wrong_guesses, word, guessed_letters)
                print(f"\n💀 YOU LOST!! the word was '{word}'. rip bestie.")
                return False

# === MAIN PROGRAM ===
def main():
    words = load_words()

    while True:
        # Pick random word
        word = random.choice(words).lower()
        play_game(word)

        # Play again?
        again = input("\nplay again? (y/n): ").strip().lower()
        if again == "y":
            print("let's gooo!! restarting with a new word...\n")
            continue
        else:
            print("\n👋 peace out!! thanks for playing!!")
            break

if __name__ == "__main__":
    main()