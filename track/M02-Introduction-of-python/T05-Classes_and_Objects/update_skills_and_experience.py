class StudentProfile:

    def __init__(self, name, experience, skills):
        # Store initial data in instance variables
        self.name = name
        self.experience = experience
        self.skills = skills

    def update_experience(self, new_experience):
        # Replace current experience with the new value
        self.experience = new_experience

    def add_skill(self, new_skill):
        # Append the new skill to the existing skills list
        self.skills.append(new_skill)


# Read initial input values
name = input().strip()
experience = int(input())
skills = input().split()

# Read update input values
new_experience = int(input())
new_skill = input().strip()

# Create one StudentProfile object
student = StudentProfile(name, experience, skills)

# Update the student's experience
student.update_experience(new_experience)

# Add the new skill
student.add_skill(new_skill)

# Print the updated profile in the required format
print(f"Name: {student.name}")
print(f"Experience in Years: {student.experience}")
print(f"Skills: {', '.join(student.skills)}")