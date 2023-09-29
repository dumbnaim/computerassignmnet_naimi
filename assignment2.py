number = float(input("Enter a number: "))
sign = '0' if number >= 0 else '1'
number = abs(number)
integer_part = int(number)
fractional_part = number - integer_part
integer_binary = bin(integer_part)[2:]
binary_representation = sign + '0'
exponent = 0
if integer_part == 0:
    while fractional_part < 1:
        fractional_part *= 2
        exponent -= 1
else:
    while integer_part >= 1:
        integer_part //= 2
        exponent += 1

binary_representation += bin(exponent + 7)[2:].zfill(4)
fractional_binary = ""

for _ in range(10):
    fractional_part *= 2
    fractional_bit = int(fractional_part)
    fractional_binary += str(fractional_bit)
    fractional_part -= fractional_bit

binary_representation += fractional_binary

while len(binary_representation) < 14:
    binary_representation += '0'

print(f"14-bit binary representation: {binary_representation}")

import subprocess

result = subprocess.run(["date"], stdout=subprocess.PIPE, text=True, shell=True)
print("Current time:", result.stdout.strip())