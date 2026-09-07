class TrainingBatch:
    # Class variables
    batch_name = "Python Batch 1"
    student_count = 0

    # Instance method (Constructor)
    def __init__(self, student_name, attendance):
        self.student_name = student_name
        self.attendance = attendance
        TrainingBatch.student_count += 1

    # Instance method
    def get_details(self):
        # Return the formatted student details
        return f"{self.student_name}: {self.attendance}%"

    # Create the update_batch_name() class method
    @classmethod
    def update_batch_name(cls, new_batch_name):
        cls.batch_name = new_batch_name

    # Create the is_valid_attendance() static method
    @staticmethod
    def is_valid_attendance(attendance):
        if 0 <= attendance <= 100:
            return True
        else:
            return False


# Read n records
n = int(input())
students = []

for i in range(n):
    student_name = input().strip()
    attendance = int(input())

    # Validate attendance before object creation
    if TrainingBatch.is_valid_attendance(attendance):
        student = TrainingBatch(student_name, attendance)
        students.append(student)

new_batch_name = input().strip()

# Update the batch name using class method
TrainingBatch.update_batch_name(new_batch_name)

# Output results
print(f"Batch: {TrainingBatch.batch_name}")
print(f"Valid Students: {TrainingBatch.student_count}")
for student in students:
    print(student.get_details())