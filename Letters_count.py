sentence = "I want to become a full stack developer"

counter = {}

for i in sentence:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1


print(counter)

#https://github.com/Ozan-007/Python-assignment
