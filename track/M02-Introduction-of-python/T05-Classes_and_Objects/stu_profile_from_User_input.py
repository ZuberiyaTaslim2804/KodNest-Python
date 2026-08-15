class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        score,
        is_placed
    ):
        # Initialize and store instance attributes
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.is_placed = is_placed

    def __str__(self):
        # Return formatted profile string with score rounded to 1 decimal place
        return (
            f"STUDENT PROFILE\n"
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score:.1f}\n"
            f"Placement Status: {placement_status}"
        )


# Read user inputs and convert to appropriate data types
student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
placement_input = input().strip()

# Convert placement string input to a boolean value (case-insensitive)
is_placed=False
if placement_input.lower()=="yes":
    is_placed=True
   
if is_placed:
    placement_status="Placed"
else:
    placement_status="Not Placed"
# Instantiate StudentProfile object using explicit keyword arguments
student = StudentProfile(
    course=course,
    student_id=student_id,
    is_placed=is_placed,
    name=name,
    score=score
)

# Print the student profile via __str__() formatting
print(student)