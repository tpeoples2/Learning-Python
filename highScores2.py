# High Scores 2.0

scores = []
choice = None
while choice != 0:
    print(
    """
    High Scores 2.0

    0 - quit
    1 - list scores
    2 - add a score
    """
    )

    choice = int(raw_input("Choice: "))
    print()

    # exit
    if choice == 0:
        print("Good-bye")

    # display high score table
    elif choice == 1:
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    # add a score
    elif choice == 2:
        name = raw_input("What is the player's name?: ")
        score = int(raw_input("What score did the player get?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]     # keep only the top five scores
    
    # unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")

