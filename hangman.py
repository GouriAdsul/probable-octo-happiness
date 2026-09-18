import random

# Random words with hints
words = {
    "apple": "A fruit",
    "tiger": "A wild animal",
    "computer": "An electronic machine",
    "school": "A place where students study",
    "flower": "A beautiful part of a plant"
}

score = 0

print("===== WELCOME TO HANGMAN GAME =====")

while True:

    # Random word
    word = random.choice(list(words.keys()))
    hint = words[word]

    guessed_letters = []
    attempts = 6

    print("\nHint:", hint)
    print("You have", attempts, "attempts.")

    # Display blanks
    display = ["_"] * len(word)

    while attempts > 0 and "_" in display:

        print("\nWord:", " ".join(display))
        print("Attempts left:", attempts)
        print("Score:", score)

        guess = input("Guess a letter: ").lower()

        # Check valid input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        # Already guessed
        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        guessed_letters.append(guess)

        # Correct guess
        if guess in word:
            print("Correct guess! 🎉")

            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess

            score += 10

        # Wrong guess
        else:
            print("Wrong guess! ❌")
            attempts -= 1
            score -= 2

    # Win / Lose
    if "_" not in display:
        print("\n🎉 YOU WON!")
        print("The word was:", word)
        print("Your score:", score)

    else:
        print("\n😢 GAME OVER!")
        print("The word was:", word)
        print("Your score:", score)

    # Replay option
    replay = input("\nDo you want to play again? (yes/no): ").lower()

    if replay != "yes":
        print("\nThank you for playing! 😊")
        print("Final Score:", score)
        break
