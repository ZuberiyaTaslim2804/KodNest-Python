# using Mutable Default Argument
def add_student(name,students=[]):
    students.append(name)
    print(students)

first=input()
second=input()
third=input()

print("Using Mutable Deafult Argument")
add_student(first)
add_student(second)
add_student(third)
# Using None as Default Argument
def add_task(task,tasks=None):
    if tasks is None:
        tasks = []
    
    tasks.append(task)
    return task

print("Using Deafult argument -None")
print(add_task("Learn Python"))
print(add_task("Paractice Functions"))