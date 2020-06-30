# HL component 2 - Generates random number between low and high


import random

LOW = 1
HIGH = 4

for item in range (1, 20):
    secret = random.randint(LOW, HIGH)
    print(secret, end="\t")
