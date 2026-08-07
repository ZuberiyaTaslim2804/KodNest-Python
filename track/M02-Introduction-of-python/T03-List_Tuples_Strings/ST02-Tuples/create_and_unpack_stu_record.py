name=input()
course=input()
score=int(input())

# Create the tuple
student_record=(name,course,score)

# Unpack the tuple
a,b,c=student_record

#Display teh unpack values

print("Name:",a)
print("Course:",b)
print("Score:",c)