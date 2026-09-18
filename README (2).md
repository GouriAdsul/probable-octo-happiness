# 🎮 Hangman Game (Python)

A simple command-line **Hangman game** written in Python. The game picks a random word, gives you a hint, and you try to guess the word letter by letter before you run out of attempts.

## 📋 Features

- Random word selection from a predefined word list
- Hints provided for each word
- Score tracking (+10 for correct guess, -2 for wrong guess)
- Input validation (only single alphabet letters allowed)
- Prevents guessing the same letter twice
- Replay option after each round
- Final score displayed at the end

## 🗂️ Word List

The game currently includes the following words with hints:

| Word     | Hint                              |
|----------|------------------------------------|
| apple    | A fruit                            |
| tiger    | A wild animal                      |
| computer | An electronic machine              |
| school   | A place where students study       |
| flower   | A beautiful part of a plant        |

You can easily add more words by editing the `words` dictionary in the code.

## ⚙️ Requirements

- Python 3.x (no external libraries needed — uses only the built-in `random` module)

## ▶️ How to Run

1. Save the code in a file, e.g. `hangman.py`
2. Open a terminal in the same folder
3. Run:
   ```bash
   python hangman.py
   ```

## 🕹️ How to Play

1. A hint will be shown for the hidden word.
2. You have **6 attempts** to guess the word correctly.
3. Enter one letter at a time:
   - ✅ Correct guess → letter is revealed, score **+10**
   - ❌ Wrong guess → one attempt is lost, score **-2**
4. Win by revealing the full word before attempts run out.
5. After each round, choose whether to play again (`yes`/`no`).

## 🧮 Scoring

| Action          | Score Change |
|------------------|--------------|
| Correct letter   | +10          |
| Wrong letter     | -2           |

Your score carries over across rounds until you choose to stop.

## 📌 Notes / Possible Improvements

- Add more words to the `words` dictionary for variety
- Add a visual hangman drawing that updates with wrong guesses
- Add difficulty levels (shorter/longer words, fewer attempts)
- Save high scores to a file

## 📄 License

Free to use and modify for personal or educational purposes.
