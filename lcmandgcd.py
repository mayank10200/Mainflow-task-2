import math

# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# GCD
gcd = math.gcd(a, b)

# LCM formula: (a * b) // GCD
lcm = (a * b) // gcd

print("GCD is:", gcd)
print("LCM is:", lcm)
