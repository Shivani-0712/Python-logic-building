# Factorial of a Number
# This program calculates the factorial of a given number
# Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

n = int(input("Enter a number: "))

fact = 1

# Multiply numbers from n down to 1
for i in range(n, 0, -1):
    fact = fact * i

print("Factorial =", fact)
