# Read the value
n=int(input())
# Initialize the count and total
total=0
count=1
# Calculate the total using while loop
while count<=n:
    total+=count
    count+=1
# Display the total
print(f"Total: {total}")