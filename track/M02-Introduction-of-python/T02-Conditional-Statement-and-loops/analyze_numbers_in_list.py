limit=int(input())
target=int(input())

count=0
total=0
found=False

for i in range(1,limit):
    if i%3==0:
        count+=1
        total+=i
        if i ==target:
            found=True
    
print("count: ",count)
print("Sum: ",total)
print("Target Found:","Yes" if found else "No")