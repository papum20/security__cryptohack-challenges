SIZE = 16
COLS = 4
ROWS = 4

def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return [ matrix[i//ROWS][i%COLS] for i in range(SIZE) ]

def matrix2string(matrix):
    """ Converts a 4x4 matrix into a string of the corresponding chars for those bytes.  """
    return ''.join([ chr(b) for b in matrix2bytes(matrix) ]) 

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

if __name__ == '__main__':
    print(matrix2bytes(matrix))
    print( matrix2string(matrix) )

