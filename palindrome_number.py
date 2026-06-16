# Palindrome Number Check
# This program checks whether a number is a palindrome
# A palindrome reads the same forwards and backwards
# Example: 121, 1331

n = int(input("Enter a number: "))

temp = n
r = ""

# Reverse the number digit by digit
for i in range(len(str(n))):
    d = n % 10
    n = n // 10
    r = r + str(d)

# Compare original number with reversed number
if r == str(temp):
    print("Palindrome")
else:
    print("Not a palindrome")
