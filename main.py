import random

uppercase_letters = "ABCDEFGIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "1234567890"
symbols = "!@#$^&*<>.,?"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

lenght = 50
amount = 100

for x in range(amount):
    password = "".join(random.sample(all, lenght))
    print(password)
