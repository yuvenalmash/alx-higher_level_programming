#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
last_digit_int = int(last_digit)
text = "Last digit of "
if last_digit_int > 5:
    text2 = "greater than 5"
elif last_digit_int == 0:
    text2 = "and is 0"
elif last_digit_int < 6:
    text2 = "and is less than 6 and not 0"

print(f"{text} {number} is {last_digit_int} {text2}")
