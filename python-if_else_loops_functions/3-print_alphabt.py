#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit

output_message = f"Last digit of {number} is {last_digit}"

if last_digit > 5:
    output_message += " and is greater than 5"
elif last_digit == 0:
    output_message += " and is 0"
else:
    output_message += " and is less than 6 and not 0"

print(output_message)
