# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Taking input from the user
num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is NOT a Prime Number")
