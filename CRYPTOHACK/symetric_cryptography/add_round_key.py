state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

#every round we take the key and we xor 
# every element of the matrix state 
# with the same element of the matrix round key
def add_round_key(s, k):
    return bytes(
        state_byte ^ round_key_byte 
        for state_row, round_key_row in zip(state, round_key)
        for state_byte, round_key_byte in zip(state_row, round_key_row)
        )


print(add_round_key(state, round_key))

