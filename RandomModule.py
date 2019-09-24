import random
import collections

d = []

for x in range(5):
    y = random.randint(0,50)
    if y not in d:
        d.append(y)
        print(y)

print(d)





