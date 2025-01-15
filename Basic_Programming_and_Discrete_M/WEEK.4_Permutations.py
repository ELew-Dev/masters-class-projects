import math

def main():
    # Ask for the number of subsets
    while True:
        try:
            j = int(input("Enter the number of subsets (3-8): "))
            if 3 <= j <= 8:
                break
            else:
                print("Please enter a number between 3 and 8.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Ask for the size of each subset
    subset_sizes = []
    for i in range(1, j + 1):
        while True:
            try:
                size = int(input(f"Enter the size of subset {i} (1-5): "))
                if 1 <= size <= 5:
                    subset_sizes.append(size)
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    # Calculate the total size of all subsets
    n = sum(subset_sizes)

    # Ask for the total number of elements in the arrangement
    while True:
        try:
            k = int(input(f"Enter the total number of elements in the arrangement (less than {n}): "))
            if 0 < k < n:
                break
            else:
                print(f"Please enter a number less than {n} and greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Compute the number of arrangements using permutations
    arrangements = math.perm(n, k)

    # Print the result
    print(f"The number of arrangements of {k} elements out of {n} is: {arrangements}")

    # Prevent the program from closing immediately
    input("Press Enter to exit the program.")

if __name__ == "__main__":
    main()
