class StudentProfile:
    def __init__(self, name, experience):
        # Store the name and experience
        self.name = name
        self.experience = experience

    # Create the is_valid_experience() static method
    @staticmethod
    def is_valid_experience(experience):
        return 0 <= experience <= 40

# Read inputs
name = input().strip()
experience = int(input())

# Validate the experience using the static method
if StudentProfile.is_valid_experience(experience):
    student = StudentProfile(name, experience)
    print("Profile Created")
    print(f"Name: {student.name}")
    print(f"Experience: {student.experience} years")
else:
    print("Invalid Experience")