import numpy as np

def input_matrix(name):
    print(f"\nEnter details for matrix {name}:")
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    print(f"Enter the elements for {rows}x{cols} matrix (row by row, space-separated):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Error: Number of elements in row does not match columns. Try again.")
            return input_matrix(name)  
        matrix.append(row)
    return np.array(matrix)



def add_matrices(A, B):
    if A.shape != B.shape:
        return "Error: Matrices must have the same dimensions for addition."
    return A + B


def subtract_matrices(A, B):
    if A.shape != B.shape:
        return "Error: Matrices must have the same dimensions for subtraction."
    return A - B


def multiply_matrices(A, B):
    if A.shape[1] != B.shape[0]:
        return "Error: Number of columns in first matrix must equal number of rows in second matrix."
    return np.dot(A, B)


def transpose_matrix(A):
    return A.T


def determinant_matrix(A):
    if A.shape[0] != A.shape[1]:
        return "Error: Matrix must be square (same number of rows and columns) for determinant."
    return np.linalg.det(A)


def display_result(operation, result):
    print(f"\n--- {operation} Result ---")
    if isinstance(result, str):  
        print(result)
    else:
        print("Matrix:")
        print(result)
        print(f"Shape: {result.shape}")
    print("-" * 30)

def main():
    print("Welcome to the Matrix Operations Tool!")
    print("Supported operations: Addition, Subtraction, Multiplication, Transpose, Determinant")
    
    while True:
        print("\nMenu:")
        print("1. Add two matrices")
        print("2. Subtract two matrices")
        print("3. Multiply two matrices (matrix multiplication)")
        print("4. Transpose a matrix")
        print("5. Calculate determinant of a matrix")
        print("0. Exit")
        
        choice = input("Choose an option (0-5): ").strip()
        
        if choice == '0':
            print("Exiting the tool. Goodbye!")
            break
        
        elif choice in ['1', '2', '3']:
            # Operations for two matrices
            A = input_matrix("A")
            B = input_matrix("B")
            if choice == '1':
                result = add_matrices(A, B)
                display_result("Addition (A + B)", result)
            elif choice == '2':
                result = subtract_matrices(A, B)
                display_result("Subtraction (A - B)", result)
            elif choice == '3':
                result = multiply_matrices(A, B)
                display_result("Multiplication (A * B)", result)
        
        elif choice == '4':
            # Transpose one matrix
            A = input_matrix("A")
            result = transpose_matrix(A)
            display_result("Transpose of A", result)
        
        elif choice == '5':
            # square matrix
            A = input_matrix("A")
            result = determinant_matrix(A)
            display_result("Determinant of A", result)
        
        else:
            print("Invalid choice. Please select 0-5.")

if __name__ == "__main__":
    main()