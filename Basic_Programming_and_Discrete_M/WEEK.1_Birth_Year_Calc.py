# Get user input 
name = input("What is your name?")
age = int(input("How old are you?"))
current_year = int(input("What is the current year?"))

# Calculate possible birth years 
year1 = current_year - age 
year2 = year1 - 1 

# Print result 
print(f"Dear {name}, you were born either in {year1} or {year2}.")

# Pause before closing 
input("Press ENTER to exit...")
