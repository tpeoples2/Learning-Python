# a = [1, 11, 21, 1211, 111221, ...
# input = 1
# output = 11
# input = 11
# output = 21

def sequence(num):
    current = num[0]
    num = num[1:] + " "
    count = 1

    term = ""

    for i in num:
        if i != current:
            term += str(count) + current
            count = 1
            current = i
        else:
            count += 1

    return term

num = "1"
for i in range(0, 30):
    #print num
    num = sequence(num)

print len(num)
