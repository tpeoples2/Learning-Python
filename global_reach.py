# Global Reach

def read_global():
    print("From inside the local scope of read_global(), value is: " + str(value))

def shadow_global():
    value = -10
    print("From inside the local scope of shadow_global(), value is: " + str(value))

def change_global():
    global value
    value = -10
    print("From inside the local scope of change_global(), value is: " + str(value))

# main
value = 10
print("In the global scope, value has been set to: " + str(value) + "\n")

read_global()
print("Back in the global scope, value is still: " + str(value) + "\n")

shadow_global()
print("Back in the global scope, value is still: " + str(value) + "\n")

change_global()
print("Back in the global scope, value has changed to: " + str(value) + "\n")


