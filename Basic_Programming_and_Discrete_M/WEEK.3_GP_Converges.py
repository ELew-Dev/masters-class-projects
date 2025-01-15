def main():
    # Ask for the scale factor a and the common ratio r
    a = float(input("Enter the scale factor a: "))
    r = float(input("Enter the common ratio r: "))

    # See if the GP converges
    if abs(r) < 1:
        # If the common ratio is between -1 and 1, it converges
        sum_infinite = a / (1 - r)
        print(f"This GP converges with infinite elements to {sum_infinite:.7f}")
        
        # Print the first three terms
        terms = [a, a * r, a * r ** 2]
        print(f"The first terms are {terms[0]}, {terms[1]}, and {terms[2]}")
    else:
        # If the common ratio is >= 1 or <= -1, it does not converge
        n = int(input("Enter the number of elements n: "))
        
        # Compute the sum of the first n terms
        sum_n_terms = a * (1 - r**n) / (1 - r) if r != 1 else a * n
        print(f"This GP sum with {n} elements is equal to {sum_n_terms:.0f}")
        
        # Print the first three terms
        terms = [a, a * r, a * r ** 2]
        print(f"The first terms are {terms[0]}, {terms[1]}, and {terms[2]}")

# Run the program
main()