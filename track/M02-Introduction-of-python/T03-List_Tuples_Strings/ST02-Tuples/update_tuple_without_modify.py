# Read the course details
course_name=input()
course_week=input()
course_status=input()

#create the original tuple
course_details=(course_name,course_week,course_status)
name,week,status=course_details

# Read the updated week
updated_week=input()

# Create and assign a new tuple
new_tuple=(name,updated_week,status)

# display the updated tuple
print(new_tuple)