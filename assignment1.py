valid_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

number = input("Enter the number: ")
from_base = int(input("Enter the base of the input number: "))
to_base = int(input("Enter the base you want to convert to: "))
for digit in number:
    if digit not in valid_digits[:from_base]:
        print("Error: Invalid input number.")
        break
else:
    decimal_value = 0
    for digit in number:
        decimal_value = decimal_value * from_base + int(digit, from_base)
    result = ''
    while decimal_value > 0:
        remainder = decimal_value % to_base
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result
        decimal_value //= to_base

    print(f"Converted number in base {to_base}: {result}")
import subprocess

result = subprocess.run(["date"], stdout=subprocess.PIPE, text=True, shell=True)
print("Current time:", result.stdout.strip())