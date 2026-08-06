#Read the no.of students
stu_count=int(input())

#Initialize the total and counters
total_marks=0
passed_count=0
failed_count=0

# read and process each mark
for i in range(stu_count):
    mark=int(input())
    total_marks+=mark
    if mark>=40:
        passed_count+=1
    else:
        failed_count+=1
    
# Display the summary
print("Total Marks:",total_marks)
print("Passed Students:",passed_count)
print("Failed Students:",failed_count)

# Display the batch result
if failed_count==0:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Needs Improvement")