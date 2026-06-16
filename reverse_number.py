# Reverse a Number
# This program reverses the digits of a given number
# Example: 1234 -> 4321

n = int(input("Enter a number: "))

# Extract digits from right to left
for i in range(len(str(n))):
    d = n % 10
    n = n // 10
    print(d, end="")
