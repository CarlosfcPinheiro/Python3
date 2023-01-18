#Math quiz

import random

count = 0
for c in range(0, 5):
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    sum = n1 + n2

    resp = int(input(f"Resolva. {n1} + {n2} = "))

    if (resp == sum):
        count += 1

print(f"O seu resultado foi ({count}/5)")
