"""
utils.py
--------
Utility/helper functions for the Smart Career Assistant chatbot.

This module contains all the "supporting" functions that are not
directly related to conversation logic — things like printing the
banner, simulating a typing animation, generating timestamps,
clearing the console, and saving the chat history to a file.

Keeping these functions separate from chatbot.py and responses.py
follows the Single Responsibility Principle: each file has one job.
"""

import os
import sys
import time
from datetime import datetime

# ---------------------------------------------------------------
# CONSTANTS
# ---------------------------------------------------------------
HISTORY_FILE = "history.txt"
TYPING_SPEED = 0.015  # seconds delay per character (typing animation)


def get_timestamp():
    """
    Return the current time as a formatted string.

    Returns:
        str: Current time in HH:MM:SS format.
    """
    return datetime.now().strftime("%H:%M:%S")


def get_full_datetime():
    """
    Return the current date and time (used when saving history to file).

    Returns:
        str: Current date and time, e.g. '2026-07-06 14:32:10'.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def clear_screen():
    """
    Clear the console screen.

    Works on both Windows ('cls') and Unix/Linux/Mac ('clear').
    """
    os.system("cls" if os.name == "nt" else "clear")


def typing_effect(text, delay=TYPING_SPEED):
    """
    Print text character-by-character to simulate a "typing" animation,
    similar to how modern chat assistants render responses.

    Args:
        text (str): The text to display.
        delay (float): Delay in seconds between each character.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # move to next line after the message is fully "typed"


def print_banner():
    """
    Print the welcome banner shown when the chatbot starts.
    """
    banner = """
╔══════════════════════════════════════════════════════════════╗
║             🤖  SMART CAREER ASSISTANT  🤖                     ║
║        Your Rule-Based AI Companion for Career Growth          ║
╠══════════════════════════════════════════════════════════════╣
║  Type 'help'  -> see what I can do                              ║
║  Type 'menu'  -> see topic categories                           ║
║  Type 'clear' -> clear the screen                                ║
║  Type 'exit'  -> end the conversation                            ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)


def print_help():
    """
    Print a help message describing the chatbot's capabilities.
    """
    help_text = """
📌 HERE'S WHAT I CAN HELP YOU WITH:

  1. Career Guidance      -> "software engineer", "data scientist", "AI engineer"
  2. Programming Roadmaps -> "python roadmap", "AI roadmap", "MERN roadmap"
  3. Interview Prep        -> "HR interview", "technical interview", "aptitude"
  4. Resume Tips           -> "resume", "projects", "skills", "internships"
  5. Motivation            -> "motivate me", "confidence", "study tips"
  6. College/Placement     -> "placement", "CGPA", "internship"
  7. General Commands      -> "menu", "help", "clear", "history", "exit"

Just type naturally — I'll pick up on the keywords in your message!
"""
    print(help_text)


def print_menu():
    """
    Print a categorized menu of topics the chatbot understands.
    """
    menu_text = """
🗂️  TOPIC MENU

  [1] Career Roles        (e.g. "cloud engineer")
  [2] Programming Langs   (e.g. "java", "c++")
  [3] Interview Prep       (e.g. "coding interview")
  [4] Resume & Portfolio   (e.g. "resume tips")
  [5] Roadmaps             (e.g. "data science roadmap")
  [6] Motivation           (e.g. "motivate me")
  [7] College & Placement  (e.g. "CGPA")

Type any related keyword to get started!
"""
    print(menu_text)


def save_history(chat_log, filename=HISTORY_FILE):
    """
    Save the full conversation log to a text file.

    Args:
        chat_log (list): A list of strings, each representing one
                          line of the conversation (user or bot).
        filename (str): Destination file path.
    """
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"\n----- Session started: {get_full_datetime()} -----\n")
            for line in chat_log:
                file.write(line + "\n")
            file.write(f"----- Session ended: {get_full_datetime()} -----\n")
        print(f"💾 Chat history saved to '{filename}'.")
    except OSError as error:
        # Graceful handling instead of crashing the program
        print(f"⚠️  Could not save chat history: {error}")


def show_history(chat_log):
    """
    Display the current session's conversation history in the console.

    Args:
        chat_log (list): List of conversation lines for this session.
    """
    if not chat_log:
        print("📭 No conversation history yet in this session.")
        return

    print("\n📜 CONVERSATION HISTORY (this session)")
    print("-" * 55)
    for line in chat_log:
        print(line)
    print("-" * 55)
