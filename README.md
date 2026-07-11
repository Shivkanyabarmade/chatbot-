# 🤖 Smart Career Assistant — Rule-Based AI Chatbot

**Internship Project 1 — DecodeLabs Industrial Training Kit (Batch 2026)**

A professional, modular, rule-based chatbot built in pure Python that
provides career guidance, interview preparation tips, resume advice,
and learning roadmaps — without using any AI/ML libraries or external
APIs. This project demonstrates that solid **control flow, data
structures, and clean architecture** are the true foundation of any
intelligent system, generative or otherwise.

---

## 📖 Project Overview

Most beginner chatbot projects are a single script full of `if/elif`
chains. This project instead treats the chatbot like a real product:

- **Separation of concerns** — data (`responses.py`), logic
  (`chatbot.py`), and utilities (`utils.py`) each live in their own file.
- **Dictionary-based matching** instead of a long if-elif ladder, for
  O(1) average-case keyword lookups instead of O(n) linear scans.
- **Graceful error handling** for empty/invalid input and Ctrl+C exits.
- **Session features** like chat history, timestamps, a typing
  animation, and a persistent log file — the kind of polish that
  turns a "student assignment" into a portfolio piece.

The chatbot understands natural phrases (not just exact commands) by
scanning your sentence for known keywords — e.g., typing *"what should
I learn for a technical interview?"* still matches `"technical
interview"`.

---

## ✨ Features

### Core (assignment requirements)
- Pure Python — only `if/else`, loops, functions, dictionaries, lists
- Continuous input loop until the user types `exit`
- Case-insensitive & whitespace-tolerant input handling
- Graceful handling of empty/invalid input

### Conversation Topics
| Category | Example Keywords |
|---|---|
| Greetings | hello, hi, hey, good morning, good evening |
| Farewell | exit, quit, bye |
| Identity | who are you, what can you do, help |
| Career Guidance | software engineer, data scientist, AI engineer, web developer, cloud engineer, cybersecurity |
| Programming Languages | python, java, c++, javascript |
| Interview Preparation | HR interview, technical interview, aptitude, coding interview |
| Resume Tips | resume, projects, skills, internships |
| Learning Roadmaps | AI roadmap, Data Science roadmap, MERN roadmap, Python roadmap |
| Motivation | motivate me, confidence, study tips |
| College Help | placement, CGPA, internship |

### Extra Engineering Features
- ⌨️ Typing animation for bot responses
- 🕒 Timestamps on every message
- 📜 In-session conversation history (`history` command)
- 🔢 Chat counter shown at the end of the session
- 🗂️ `menu` command for browsing topic categories
- ❓ `help` command for usage guidance
- 🧹 `clear` command to reset the console view
- 💾 Automatic saving of chat history to `history.txt` on exit
- 🧩 Fully modular functions, one responsibility each
- 🎨 Clean, emoji-enhanced console UI

---

## 🛠️ Technologies Used

- **Language:** Python 3.8+
- **Libraries:** Only the standard library — `os`, `sys`, `time`, `datetime`
- **No ML/AI libraries, no external APIs** (by design — see "Future Scope")

---

## 📁 Folder Structure

```
career_chatbot/
│
├── chatbot.py          # Main entry point — the conversation loop
├── responses.py        # Knowledge base (dictionaries) + matching engine
├── utils.py             # Helper functions (timestamp, typing effect, etc.)
├── history.txt          # Saved conversation logs (auto-generated/appended)
├── README.md            # This file
├── requirements.txt      # Dependencies (none — stdlib only)
└── DOCUMENTATION.md      # Algorithm, flowchart, interview/viva Q&A, complexity analysis
```

---

## ▶️ How to Run

1. Make sure Python 3.8+ is installed:
   ```bash
   python3 --version
   ```
2. Navigate into the project folder:
   ```bash
   cd career_chatbot
   ```
3. Run the chatbot:
   ```bash
   python3 chatbot.py
   ```
4. Chat away! Type `help` or `menu` any time, and `exit` when done.

No installation of extra packages is required.

---

## 💬 Sample Output

```
╔══════════════════════════════════════════════════════════════╗
║             🤖  SMART CAREER ASSISTANT  🤖                     ║
║        Your Rule-Based AI Companion for Career Growth          ║
╠══════════════════════════════════════════════════════════════╣
║  Type 'help'  -> see what I can do                              ║
║  Type 'menu'  -> see topic categories                           ║
║  Type 'clear' -> clear the screen                                ║
║  Type 'exit'  -> end the conversation                            ║
╚══════════════════════════════════════════════════════════════╝

You: hello
Bot: Hello! 👋 I'm your Smart Career Assistant. How can I help your career journey today?

You: I want to become a data scientist
Bot: A Data Scientist extracts insights from data using statistics, Python, and ML.
     Start with Python, SQL, statistics, and pandas/numpy.

You: any tips for a technical interview?
Bot: For technical interviews, revise DSA, practice explaining your thought process
     out loud, and be ready to write clean, working code on a whiteboard/editor.

You: exit
Bot: Goodbye! 👋 Wishing you success in your career journey. Come back anytime!

📊 Total exchanges this session: 3
💾 Chat history saved to 'history.txt'.
```

---

## 🚀 Future Scope

This project is intentionally built with clean architecture so it can
evolve step by step into more advanced systems:

1. **NLP Chatbot** — Replace exact/substring keyword matching with
   tokenization, stemming/lemmatization, and intent classification
   (e.g., using `nltk` or `spaCy`) so it understands phrasing it has
   never seen before.
2. **Machine Learning Chatbot** — Train a text classifier (e.g.,
   Naive Bayes, SVM, or a small neural network) on labeled
   question–intent pairs so new phrasings are handled automatically
   instead of requiring new dictionary entries.
3. **LLM Chatbot** — Wrap a Large Language Model (like Claude) behind
   this same interface, using the rule-based layer as a fast,
   deterministic **guardrail** — exactly like the NVIDIA NeMo /
   Llama Guard pattern: rules catch known cases instantly, the LLM
   handles everything else (see the hybrid architecture diagram in
   the original briefing).
4. **Voice Assistant** — Add speech-to-text (e.g., `speech_recognition`)
   and text-to-speech (`pyttsx3`) so the same response engine can be
   driven by voice.
5. **Web Application** — Wrap the chatbot logic in a Flask/FastAPI
   backend with a simple HTML/JS or React frontend, turning it into
   a browser-based assistant.
6. **Mobile Application** — Expose the backend via a REST API and
   build a Flutter or React Native front-end for on-the-go access.

The key engineering insight carried through all of these upgrades:
**`responses.py` (the knowledge/data layer) can keep evolving —
from static dictionaries, to vector embeddings, to an LLM call —
without the surrounding architecture in `chatbot.py` needing to change.**

---

## 📬 Contact

Built as part of the DecodeLabs AI Internship — Project 1.
