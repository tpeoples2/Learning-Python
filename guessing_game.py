import random

MAX_TRIES = 10
THE_NUMBER = random.randint(1, 100)

def play():
    guesses = []
    count = 0
    while count < MAX_TRIES:
        guess = int(raw_input("Your guess?: "))
        guesses.append(guess)
        count += 1
        if isRight(guess):
            break

    if count == MAX_TRIES:
        print "\nI win"

    print " ".join(str(i) for i in guesses)
    print "The number was", THE_NUMBER

def isRight(guess):
    if guess == THE_NUMBER:
        print "\nYou win"
        return True
    elif guess < THE_NUMBER:
        print "Higher"
    else:
        print "Lower"
    return False

def main():
    play()

if __name__ == "__main__":
    main()
