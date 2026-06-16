# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The website's design was pretty basic but straight forward. When I tried to play the game I recieved multiple errors. I tried to adjust the difficulty which is supposed to change the range of the guesses but it failed. The hints given by the program were inaccurate to your guess. Also, when the user clicks "New Game" it restarts the game but does not allow for any more inputs. There are several issues with this game. 

**Bug Reproduction Log**
Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|   2   |   Go higher             Go lower            38 on Easy
|   3   |  Go higher/lower      Game over...     Game will not restart
|Difficulty| Hard: 1-100      Hard: 1-50 &      The difficulty ranges are swapped
           & Normal 1-50      Normal 1-100    

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Once I figured out some bugs on my own I attempted to fix them on my own to challenge myself before confronting AI. I first used ChatGPT to analyze the code and find any bugs and despite my findings there were several more I missed. ChatGPT gave me a few solutions but before I began to use them I confronted Claude. Claude gave me the same issues and more while also providing more depth to explaining why it was wrong and how to fix it. I definitely liked the way Claude Code explained much better than ChatGPT. ChatGTP missed how wrong guesses could gain points, the win bonus, and an invalid input. I verified this through looking at the code and through Claude.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I would decide if a bug was really fixed if the code made sense through the entire project and if it worked on the local host. I ran a troubleshooting test manually after having Claude look at my code. I didn't feel like I needed to use a pytest but I did try to run one and it did not pass. There were three failures in test_winning_guess, test_guess_too_high, and test_guess_too_low. I allowed Claude to fix it to pass and reviewed what it had to say and it made sense.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit is like a web page that rebuilds itself every time you click something. Everything resets every rerun unless you store it properly. It reruns the script from top to bottom.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I would like to use AI to check my code once I finish and run tests to ensure it works. I thought I was done until I did a pytest and failures were found that I had no idea about and would have had difficulty finding. Also, I want to get better about pushing to Git when necessary. This project changed the way I think about AI generated code because I used to believe that when you AI generate code you would come across a lot of errors or written code that did not make sense. Now I see how useful AI can be for finding bugs, troubleshooting, and learning.