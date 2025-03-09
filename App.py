# Prompt user for input
f_name = input('Enter your first name: ').strip()
l_name = input('Enter your last name: ').strip()
age_input = input('Enter your Age: ').strip()

# Validate input
if not f_name or not l_name or not age_input.isdigit():
    print("Invalid input. Please enter a valid name and numerical age.")
else:
    age = int(age_input)  # Convert age to integer
    
    # Print greeting based on age
    if age < 30:
        greeting = "Hello Young Star!"
    elif 30 <= age <= 50:
        greeting = "Unauthorized! Please"
    else:
        greeting = "Hello Elder!"
    
    print(f"Welcome {f_name} {l_name}, Age: {age}. {greeting}")
