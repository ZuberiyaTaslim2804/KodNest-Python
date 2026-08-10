skill=[]

# Read and store five skills
for _ in range(5):
    skill.append(input())

# Convert the list into tuple
skill_record=tuple(skill)

# Create the required slices
first_three=skill_record[:3]
last_two=skill_record[-2:]
alternative=skill_record[::2]
reverse=skill_record[::-1]

#Display all required detials
print("Skill Recorded:",skill_record)
print("First Three:",first_three)
print("Last Two:",last_two)
print("Alternate Skills:",alternative)
print("Reversed Skills:",reverse)