n = int(input("Enter a number:"))
fact = 1

# Fix the loop range to iterate from 1 to n (inclusive)
for i in range(1, n + 1):
    fact *= i

print("Factorial of", n, "is:", fact)
