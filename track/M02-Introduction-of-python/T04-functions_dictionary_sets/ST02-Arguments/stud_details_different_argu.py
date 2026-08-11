def display_student(name,course,level):
    print(f"{name} | {course} | {level}")

# calling using positional arguments
display_student("Aarav","Python","Beginner")

# Calling using keyword Arguments
display_student(name="Meera",course="Java",level="Intermediate")

# Calling using both combination
display_student("Kabir",course="SQL",level="Beginner") # positional arguments must come first before keyword arguments