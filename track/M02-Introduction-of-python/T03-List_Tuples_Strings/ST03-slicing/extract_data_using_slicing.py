word=input()

first=int(input())
second=int(input())
third=int(input())

numbers=[first,second,third]
record=(first,second,third)

# Slicing the string ,list and tuple

print("Middle:",word[1:-1])
print("First Two:",numbers[:2])
print("Reversed Tuple:",record[::-1])