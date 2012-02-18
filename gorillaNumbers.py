# Gorilla Number Program

import math

def koko(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return 2 * koko(n - 1) + math.floor(koko(n - 2) / 3)

for i in range(1,40):
    print(koko(i))
