import numpy as np

# Function to check if two matrices are inverses
def are_matrices_inverses(matrix_a, matrix_b):
    try:
        # Multiply the two matrices
        product = np.dot(matrix_a, matrix_b)
        # Create an identity matrix of the same size
        identity = np.eye(len(matrix_a))
        # Check if the product is equal to the identity matrix
        return np.allclose(product, identity)
    except ValueError:
        # If the matrices cannot be multiplied
        return False

# Input two matrices from the user
def input_matrix(name):
    rows = int(input(f"Enter the number of rows for matrix {name}: "))
    cols = int(input(f"Enter the number of columns for matrix {name}: "))
    
    matrix = []
    print(f"Enter the values for matrix {name}:")
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    
    return np.array(matrix)

# Main program
print("Matrix Inverse Check")

matrix_a = input_matrix("A")
matrix_b = input_matrix("B")

if are_matrices_inverses(matrix_a, matrix_b):
    print("The matrices are inverses of each other.")
else:
    print("The matrices are NOT inverses of each other.")
