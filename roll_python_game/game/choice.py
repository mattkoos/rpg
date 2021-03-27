#!/usr/bin/env python3
from roll_python_game.resources.console import console

def get_display_options(options):
    return [f"[{num}] {options[num]}" for num in sorted(options.keys())]

def clean_selection(selection):
    try:
        return int(selection)
    except ValueError:
        return 99

def prompt_choice(options, choice_text):
    # expects a dictionary int(choice_num): "choice" and a string choice_text imperative statement
    # returns an int (key)
    #print(options) # handy for debugging
    selection = 99
    count = 0
    while selection not in range(1, len(options)+1):
        insert = f"{','*count}{' again'*bool(count)}"
        print(choice_text[:-1] + insert + choice_text[-1] + "\n")
        for display_option in get_display_options(options): print(display_option)
        selection = clean_selection(input("\n" + "-"*count + "---> "))
        count += 1
    return selection