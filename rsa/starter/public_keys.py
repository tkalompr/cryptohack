# e as usually
e = 65537

#given text
base = 12

#2 prime numbers p, q of N = p * q
p = 17
q = 23
# Calculate N 
N = p*q

chipher = pow(base, e, N)
print(chipher)