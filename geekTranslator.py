# Geek Translator

geek = {"404": "clueless. From the web error message 404, meaning page not found.",
        "Googling": "searching the internet for background information on a person.",
        "Keyboard Plaque": "the collection of debris found in computer keyboards.",
        "Link Rot": "the process by which web page links become obsolete.",
        "Percussive Maintenance": "the act of striking an electronic device to make it work.",
        "Uninstalled": "being fired. Especially popular during the dot-bomb era."}

choice = None
while choice != 0:
    print(
    """
    Geek Translator

    0 - quit
    1 - look up a geek term
    2 - add a geek term
    3 - redefine a geek term
    4 - delete a geek term
    """
    )

    choice = int(raw_input("Choice: "))
    print()

    # exit
    if choice == 0:
        print("Good bye")

    # look up a term
    elif choice == 1:
        term = raw_input("Enter the term to look up: ")
        print(geek.get(term, str(term) + " is not defined in our dictionary."))

    # add a geek term
    elif choice == 2:
        term = raw_input("Enter the term: ")
        if term in geek:
            print(term + " is already defined in our dictionary, try option 3.")
        else:
            definition = raw_input("Enter the definition: ")
            geek[term] = definition

    # redefine a geek term
    elif choice == 3:
        term = raw_input("Enter the term to redefine: ")
        if term not in geek:
            print(term + " is not defined in our dictionary, try option 2.")
        else:
            definition = raw_input("Enter your new definition: ")
            geek[term] = definition

    # delete a geek term
    elif choice == 4:
        term = raw_input("Enter the term to delete: ")
        if term in geek:
            del geek[term]
            print(term + " was deleted.")
        else:
            print(term + " is not even defined in the dictionary.")
    
    # unknown choice
    else:
        print("Unknown choice. Try again.")

print("\n\nPress the enter key to exit.")



















