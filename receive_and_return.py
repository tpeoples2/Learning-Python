# Receive and Return

def display(message):
    print(message)

def give_me_five():
    five = 5
    return five

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = raw_input(question).lower()
    return response

# main
display("Here's a message for you.\n")

number = give_me_five()
print("give_me_five() returns:\t" + str(number))

answer = ask_yes_no("\nPlease enter 'y' or 'n':\t")
print("Thanks for answering with " + answer)

raw_input("\nPress the enter key to exit.")

