import math


# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


# Input: n+1 distinct natural numbers as a list
numbers = list(map(int, input().split()))

# Find the smallest number q
q = min(numbers)

# Initialize p to q
p = q

while True:
    p += 1  # Increment p to find the next prime

    # Check if p leaves a remainder of q when divided by distinct numbers
    valid = all((p % number) == q for number in numbers if number != q)

    # If p is valid and prime, print it and break the loop
    if valid and is_prime(p):
        print(p)
        break

# If no valid p is found, print "None"
print("None")
