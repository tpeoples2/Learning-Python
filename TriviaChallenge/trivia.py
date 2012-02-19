# Trivia Challenge

import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file, " + file_name + ". Ending program.\n")
        raw_input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return the next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)

    explanation = next_line(the_file)

    return category, question, answers, correct, explanation

def welcome(title):
    """Welcome the player."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t" + title + "\n")

def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t" + str(i + 1) + "-" + answers[i])
        # get answer
        answer = int(raw_input("What's your answer?: "))
        # check answer
        if answer == int(correct):
            print("\nRight!")
            score += 1
        else:
            print("\nWrong!")
        print(explanation)
        print("Score: " + str(score) + "\n\n")

        # get next block
        category, question, answers, correct, explanation = next_block(trivia_file)
    
    trivia_file.close()
    print("That was the last question!")
    print("Your final score is " + str(score))

main()
raw_input("\n\nPress the enter key to exit.")
