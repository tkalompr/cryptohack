#a function that calculates if an int is obey the rule is given
def is_quadratic_residue(x, p):
    for i in range(p):
        if (i*i)%p == x:
            return i
    return None

# Given values
p = 29
ints = [14, 6, 11]

# Process each integer to find if it's a quadratic residue and calculate the square root
for x in ints:
    result = is_quadratic_residue(x, p)
    
    if result is None:
        print(f"{x} is a quadratic non-residue modulo {p}")
    else:
        print(f"The square root of {x} modulo {p} is {result} (smallest root).") # its the smallest one because we return 
                                                                                 #and we break the code at the first value that satisfies the equation
