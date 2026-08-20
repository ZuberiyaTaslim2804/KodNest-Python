class StudentProfile:
    def __init__(self, student_id, name, score, skills):
        # Create safe private starting values
        # Initialize the properties and skills
        self.__student_id = student_id
        self.__name = "Unknown"
        self.__score = 0
        self.__skills = []

        self.name = name
        self.score = score
        for skill in skills:
            self.add_skill(skill)

    @property
    def student_id(self):
        # Return the read-only student ID
        return self.__student_id

    @property
    def name(self):
        # Return the private name
        return self.__name

    @name.setter
    def name(self, new_name):
        # Clean and validate the name
        cleaned_name = new_name.strip()
        if cleaned_name:
            self.__name = cleaned_name

    @property
    def score(self):
        # Return the private score
        return self.__score

    @score.setter
    def score(self, new_score):
        # Validate and set the score
        if 0 <= new_score <= 100:
            self.__score = new_score

    @property
    def skills(self):
        # Return an immutable tuple of skills
        return tuple(self.__skills)

    def add_skill(self, new_skill):
        # Clean and add a unique non-empty skill
        cleaned_skill = new_skill.strip()
        if cleaned_skill and cleaned_skill not in self.__skills:
            self.__skills.append(cleaned_skill)

    def __str__(self):
        # Format the complete student profile string
        skills_str = ", ".join(self.__skills)
        return (
            f"STUDENT PROFILE\n"
            f"Student ID: {self.__student_id}\n"
            f"Name: {self.__name}\n"
            f"Score: {self.__score}\n"
            f"Skills: {skills_str}"
        )


student_id = int(input())
name = input().strip()
initial_score = int(input())
skills_input = input().strip()
new_score = int(input())
new_skill = input().strip()

# Split input skills into a list
initial_skills = [s.strip() for s in skills_input.split(",") if s.strip()]

# Create one StudentProfile object
student = StudentProfile(student_id, name, initial_score, initial_skills)

# Update score and add new skill
student.score = new_score
student.add_skill(new_skill)

# Display final profile
print(student)