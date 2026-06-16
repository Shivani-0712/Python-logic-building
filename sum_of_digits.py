# Sum of Digits
# This program calculates the sum of all digits in a number
# Example: 1234 -> 1 + 2 + 3 + 4 = 10

n = int(input("Enter a number: "))

s = 0

# Extract each digit and add it to the sum
for i in range(len(str(n))):
    d = n % 10
    n = n // 10
    s = s + d

print("Sum of digits =", s)
