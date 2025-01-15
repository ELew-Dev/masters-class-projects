print("Enter 'Q' anytime to quit.\n")

while True: # Loop to allow user to retry 
    # Ask user for a number as a string, allowing 'Q' to quit 
    number_str = input("Enter a number (no more than 5 digits)").upper()

    if number_str == 'Q':
        print("Goodbye!")
        break 
 
    # Digit length limit(5 digits max)
    if len(number_str) > 5:
        print("Error: Number exceeds maximum of 5 digits.")
        continue 
   
    # Ask user for the base (an integer between 2 and 16) or allow "Q" to quit
    base_input = input("Enter a base (between 2 and 16)").upper()
    
    if base_input == 'Q':
        print("Goodbye!")
        break
        
    try:        
        # convert base input into an integer 
        base = int(base_input)
            
        if base < 2 or base > 16: 
            print("Error: Base must be between 2 and 16.")
            continue 
        else: 
            # Check if number_str contains valid digits for base given
            valid_digits = '0123456789ABCDEF'[:base]
            if all(digit in valid_digits for digit in number_str.upper()):
        
                # Convert the number from the specified base to decimal/to binary
                decimal_value = int(number_str, base)
                binary_value = bin(decimal_value)[2:] 
                # Print results 
                print(f"{number_str} in base {base} is: {decimal_value} in base 10 and {binary_value} in base 2")
            else:
                # Error message if number_str has invalid digts for base 
                print(f"Error: '{number_str}' is not a valid number in base {base}. Please try again.")
    except ValueError: 
        # Error message if  the base was not a valid integer 
        print("Invalid base entry. Please enter an integer between 2 and 16.")

    if number_str == 'Q':
        print("Goodbye!")
        break 

