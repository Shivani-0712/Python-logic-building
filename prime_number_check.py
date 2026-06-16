# Prime Number Check
# This program checks whether a given number is prime or not
# A prime number has exactly two factors: 1 and itself

n = int(input("Enter a number: "))

c = 0

# Count the number of factors
for i in range(1, n + 1):
    if n % i == 0:
        c += 1

# If the factor count is 2, the number is prime
if c == 2:
    print("Prime")
else:
    print("Non Prime")
