# Function to compute the extended Euclidean algorithm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0  # gcd, x, y
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Function to find the modular inverse
def mod_inverse(g, p):
    gcd, x, _ = extended_gcd(g, p)
    if gcd != 1:
        raise ValueError(f"{g} and {p} are not coprime, no modular inverse exists.")
    return x % p  # Ensure the result is positive

# Given values
p = 991
g = 209

# Find the inverse of g mod p
d = mod_inverse(g, p)

print(f"The multiplicative inverse of {g} mod {p} is: {d}")
