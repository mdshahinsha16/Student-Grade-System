# Student Grade System

try: # use try and except to handle error
    user_input = (float(input("Enter Your Mark (0-100): "))) # first ask user input and call "input" build in function. then convert the input to float to allow decimal marks.
   
# Check boundaries
    if user_input < 0 or user_input > 100: # use or operator to check if mark is less than 0 or greater than 100
        print("Invalid mark. Please enter a number between 0 and 100.")
    else:
        mark = int(user_input) # user input always returns a string, so we need to convert it to an integer

#assign grades
        if mark >= 90: # use >= operator to check if mark is greater than or equal to 90
            print("Mark:", mark, "-> Grade: A")
        elif mark >= 80:
            print("Mark:", mark, "-> Grade: B")
        elif mark >= 70:
            print("Mark:", mark, "-> Grade: C")
        elif mark >= 60:
            print("Mark:", mark, "-> Grade: D")
        else:
            print("Mark:", mark, "-> Grade: E") # if mark is less than 60, it will be grade E

except ValueError: # except ValueError: # if the input cannot be converted to an integer, it raises ValueError
    print("Invalid input. Please enter a valid number.")