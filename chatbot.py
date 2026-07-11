"""
chatbot.py
----------
Smart Career Assistant — Rule-Based AI Chatbot
Main entry point of the application.

Run this file to start the chatbot:
    python chatbot.py

Architecture:
    chatbot.py    -> Main loop & conversation control (this file)
    responses.py  -> Knowledge base + keyword-matching engine
    utils.py      -> Helper functions (timestamps, typing effect, etc.)

This keeps the project modular: data, logic, and utilities each live
in their own file, which mirrors how production Python projects are
structured.
"""

from responses import get_response, FAREWELLS
from utils import (
    get_timestamp,
    clear_screen,
    typing_effect,
    print_banner,
    print_help,
    print_menu,
    save_history,
    show_history,
)

# Exit keywords are checked explicitly (not via the knowledge base)
# so the loop can `break` immediately and reliably.
EXIT_COMMANDS = {"exit", "quit", "bye"}


def sanitize_input(raw_text):
    """
    Clean up raw user input before matching it against the knowledge base.

    Steps:
        1. Convert to lowercase (so "Hello" == "hello" == "HELLO").
        2. Strip leading/trailing whitespace.

    Args:
        raw_text (str): The raw string typed by the user.

    Returns:
        str: The sanitized (lowercase, stripped) input.
    """
    return raw_text.lower().strip()


def handle_special_commands(clean_input, chat_log, chat_counter):
    """
    Handle non-conversational "system" commands: help, menu, clear, history.

    Args:
        clean_input (str): Sanitized user input.
        chat_log (list): The running conversation log for this session.
        chat_counter (int): Number of exchanges so far.

    Returns:
        bool: True if a special command was handled (caller should
              `continue` the loop), False otherwise.
    """
    if clean_input == "help":
        print_help()
        return True

    if clean_input == "menu":
        print_menu()
        return True

    if clean_input == "clear":
        clear_screen()
        print_banner()
        return True

    if clean_input == "history":
        show_history(chat_log)
        return True

    return False


def run_chatbot():
    """
    Main conversation loop.

    Continuously accepts user input, sanitizes it, checks for exit
    commands and special commands, otherwise passes it to the
    knowledge base for a response — until the user decides to exit.
    """
    clear_screen()
    print_banner()

    chat_log = []       # stores full conversation for this session
    chat_counter = 0     # counts number of user messages

    while True:
        try:
            raw_input_text = input("You: ")
        except (KeyboardInterrupt, EOFError):
            # Graceful handling if user force-quits with Ctrl+C / Ctrl+D
            print("\n\n⚠️  Session interrupted. Saving history before exit...")
            save_history(chat_log)
            break

        clean_input = sanitize_input(raw_input_text)

        # Ignore empty input gracefully instead of crashing or matching wrongly
        if clean_input == "":
            print("Bot: 🙂 I didn't catch that — could you type something?")
            continue

        chat_counter += 1
        timestamp = get_timestamp()
        chat_log.append(f"[{timestamp}] You: {raw_input_text}")

        # 1. Check exit commands first
        if clean_input in EXIT_COMMANDS:
            farewell = FAREWELLS.get(clean_input, "Goodbye! 👋")
            typing_effect(f"Bot: {farewell}")
            chat_log.append(f"[{timestamp}] Bot: {farewell}")
            print(f"\n📊 Total exchanges this session: {chat_counter}")
            save_history(chat_log)
            break

        # 2. Check special system commands (help/menu/clear/history)
        if handle_special_commands(clean_input, chat_log, chat_counter):
            continue

        # 3. Fall back to the rule-based knowledge base
        response = get_response(clean_input)

        # "help" keyword inside knowledge base maps to None -> show help menu
        if response is None:
            print_help()
            continue

        typing_effect(f"Bot: {response}")
        chat_log.append(f"[{timestamp}] Bot: {response}")


if __name__ == "__main__":
    run_chatbot()
