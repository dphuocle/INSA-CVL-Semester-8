#!/usr/bin/env python3
import sys

# Initialize dictionaries to hold the matrix values
mat1 = {}
mat2 = {}

# Process each line of input
for line in sys.stdin:
    # Split the line into key and value
    line = line.strip()
    key, value = line.split('\t')
    values = value.split(',')
    # Populate the dictionaries based on the key
    if key == 'M':
        mat1[(int(values[1]), int(values[2]))] = int(values[3])
    elif key == 'N':
        mat2[(int(values[1]), int(values[2]))] = int(values[3])

for i in range(1, 4):  # Rows of the resulting matrix
    for j in range(1, 5):  # Columns of the resulting matrix
        result = 0
        for k in range(1, 3):  # This should be the common dimension size of mat1 columns and mat2 rows
            # Only multiply if both keys exist in the matrices
            if (i, k) in mat1 and (k, j) in mat2:
                result += mat1[(i, k)] * mat2[(k, j)]
        print(f'{i},{j}\t{result}')
