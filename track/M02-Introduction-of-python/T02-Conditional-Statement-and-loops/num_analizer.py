size=int(input())

pos_count=0
neg_count=0
zero_count=0
total=0

for i in range(size):
    num=int(input())
    if num>0:
        pos_count+=1
    elif num<0:
        neg_count+=1
    else:
        zero_count+=1
    total+=num

print("Positive Count:",pos_count)
print("Negative Count:",neg_count)
print("Zero Count:",zero_count)
print("Total:",total)