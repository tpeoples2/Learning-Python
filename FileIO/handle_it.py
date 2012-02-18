# Handle It

try:
    num = float(raw_input("\nEnter a number: "))
except ValueError as e:
    print("That was not a number!")
    print(e)
else:
    print("Congrats, you know how to type a number.")

# handle multiple exception types
print("\n")
for value in (None, "Hi!"):
    try:
        print("Attempting to convert " + value + "--> " + float(value))
    except TypeError:
        print("I can only convert a string or a number!")
    except ValueError:
        print("I can only convert a string of digits!")

