# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.
I did not use stretch features for this project.
---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked the agent to review my streamlit guessing game and debug any errors. I also asked it to further explain the errors if I didn't fully understand. 

**What did the agent do?**

The agent reviewed the full code base and identified multiple bugs. It explained why each issue happened and how to fix it. It corrected functions and sessions state handling.

**What did you have to verify or fix manually?**

I verified all recommended fixes suggested manually. I also ran tests after each AI suggested fix I implemented. I also had to make sure the changes didn't break the Streamlit rerun behavior.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
|Empty input| What is user submits blank guess?| Ensures blank input does not reduce attempts| Yes|Invalid input stops invalid guesses
|Non-Numeric input| What if user types letters?| Show error without crashing apps| Yes| parse_guess catches exception and returns error message
|Boundary Values| What if guess is lower or higher than range limit?| Should be evaluated| Yes| Comparison logic works for edge numbers
|Max attempts| What happens when attempts run out?| Game should end and lock input| Yes| status changes to lost and prevents further play

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
Review my Streamlit guessing game code and point out errors, bad syntax, and possible improvements.
```

**Linting output before:**

```
I'll take a look at your code. Let me start with the file you have open.

Read c:\Users\alexa\OneDrive\Documents\ai110-module1show-gameglitchinvestigator-starter\app.py
This is the "Game Glitch Investigator" starter — and true to its name, it's got several intentional glitches baked in. Here's what I found, roughly in order of how badly they break the game:

1. The secret gets turned into a string on even attempts (the big one)
app.py:161-164


if st.session_state.attempts % 2 == 0:
    secret = str(st.session_state.secret)   # ← secret becomes a string
else:
    secret = st.session_state.secret
On every even-numbered attempt, the secret is converted to a string and then compared against your integer guess in check_guess. In Python, 5 == "5" is False, so a correct guess on an even attempt never registers as a win. It then hits guess > secret, which raises TypeError (int vs str), gets caught, and falls into the string-comparison branch — where the messages are also backwards (see #2). There's no legitimate reason to stringify the secret; this whole if/else should just be secret = st.session_state.secret.

2. Reversed hint messages in the except branch
app.py:45-47


if g > secret:
    return "Too High", "📈 Go HIGHER!"   # says "Too High" but tells you to go HIGHER
return "Too Low", "📉 Go LOWER!"          # says "Too Low" but tells you to go LOWER
The outcome label and the arrow/text contradict each other. (This branch only runs because of bug #1 — fixing #1 makes it unreachable, but the messages are still wrong.)

3. The range message is hardcoded
app.py:109-112


st.info(f"Guess a number between 1 and 100. ...")
It always says 1 and 100 even though Easy is 1–20 and Normal is 1–50. It should use the actual low and high variables:


f"Guess a number between {low} and {high}. "
4. Wrong guesses can increase your score
app.py:57-60


if outcome == "Too High":
    if attempt_number % 2 == 0:
        return current_score + 5   # rewarding a wrong guess
    return current_score - 5
A "Too High" guess adds 5 points on even attempts but subtracts on odd ones — inconsistent, and "Too Low" only ever subtracts (app.py:62-63). Wrong guesses shouldn't ever gain points.

5. Off-by-one in the win bonus
app.py:52


points = 100 - 10 * (attempt_number + 1)
attempt_number is st.session_state.attempts, which was already incremented at app.py:151 before this runs. So winning on your first guess gives 100 - 10*2 = 80, not 100. The +1 double-counts the attempt — it should likely be 100 - 10 * attempt_number.

6. Invalid input still costs you an attempt
app.py:150-157 — st.session_state.attempts += 1 happens before the guess is validated, so typing "abc" burns one of your limited attempts. The increment should happen only after a successful parse.

A couple of milder things worth a look: Hard mode has the widest range (1–100) but the fewest attempts (5 vs Easy's 6), which may or may not be intentional, and parse_guess silently truncates decimals ("3.9" → 3) at app.py:23.

Bugs 1, 2, and 3 are the ones that visibly break gameplay. Want me to apply the fixes, or would you rather work through them yourself for the assignment?
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

Based on the AI's suggestions, I corrected the attempt counter so that it starts at zero instead of one so players receive the full number of allowed guesses. I also updated the range displayed to the user so it always matches the selected difficulty. I removed the unnecessary conversion of the secret number between integers and strings, which could cause incorrect comparisons. I also fixed the hint because it was originally giving the reverse. Finally, I removed the debug information that displayed the secret number, since it allowed players to bypass the intended gameplay.

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**
I will be comparing ChatGPT and Claude Code. ChatGPT identified some bugs, suggested fixes, provided bullet points on how it affects the outcome. It was really easy to interact with. However, I loved using Claude so much more. Claude went into more depth with its explainations and could pinpoint the exact location of the bugs. It also was able to identify more bugs than ChatGPT did. Claude's explanation was consistently clearer and more concise. 