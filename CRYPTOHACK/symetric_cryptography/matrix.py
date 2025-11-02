#this function takes the givenmatrix and returns an array of bytes
#searching row by row line by line
def matrix2bytes(matrix):
    return bytes(b for row in matrix for b in row)

#The given matrix
matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))
