# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function to calculate the binomial coefficient (n choose k)
def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Function to create Pascal's Triangle
def generate_pascals_triangle(rows):
    triangle = []
    for n in range(rows):
        row = []
        for k in range(n + 1):
            row.append(binomial_coefficient(n, k))
        triangle.append(row)
    return triangle

# Function to print Pascal's Triangle
def print_pascals_triangle(triangle):
    num_rows = len(triangle)
    for i in range(num_rows):
        # Add spaces at the start of the row for alignment
        print(" " * (num_rows - i - 1), end="")
        for num in triangle[i]:
            print(num, end=" ")
        print()  # Move to the next line

# Main program
def main():
    while True:
        try:
            # Ask user for the number of rows (4 to 8)
            rows = int(input("Enter the number of rows for Pascal's Triangle (4-8): "))
            if 4 <= rows <= 8:
                break  # Valid input, exit the loop
            else:
                print("Please enter a number between 4 and 8.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Generate and print Pascal's Triangle
    triangle = generate_pascals_triangle(rows)
    print("\nPascal's Triangle:")
    print_pascals_triangle(triangle)

# Run the program
main()
