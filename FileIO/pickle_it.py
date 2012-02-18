# Pickle It

import pickle, shelve

print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]

f = open("pickles.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nUnpickling lists.")
f = open("pickles.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()

print("\nShelving lists.")
s = shelve.open("pickles2.dat")
s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]
s.sync()

print("Retrieving lists from a shelved file:")
print("brand - " + str(s["brand"]))
print("shape - " + str(s["shape"]))
print("variety - " + str(s["variety"]))
s.close()

input("\n\nPress the enter key to exit.")
