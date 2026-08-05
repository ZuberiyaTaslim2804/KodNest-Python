# Read the values required
marks=int(input())
attendance=int(input())
project_complete=input()

if marks>=60 and attendance>=75:
    if project_complete=="yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
