# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

This is all listed in reflection.md. Please refer to this file for the answer to these questions.

Please refer to the github repo for the screenshot of winning under image.png.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Open the app to load
2. Select player difficulty on the left.
3. Player must enter a numerical guess.
4. Player must submit the guess and the game will check the guess.
5. The score will update based on outcome.
6. The game will check the win condition and will update the status.
7. If the game is still active and the player has not lost or won then attempt another guess.
8. Once the game is finished then click New Game and it will reset the game.


## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
4 passed in 0.04s
tests/test_game_logic.py::test_winning_guess                          PASSED
tests/test_game_logic.py::test_guess_too_high                         PASSED
tests/test_game_logic.py::test_guess_too_low                          PASSED
tests/test_game_logic.py::test_hint_message_direction_matches_outcome PASSED


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
