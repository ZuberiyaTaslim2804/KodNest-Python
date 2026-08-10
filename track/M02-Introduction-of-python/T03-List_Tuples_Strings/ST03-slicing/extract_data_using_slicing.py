word=input()

first=int(input())
second=int(input())
third=int(input())

numbers=[first,second,third]
record=(first,second,third)

# Slicing the string ,list and tuple

print("Middle:",word[1:-1])     #removing first and last char
print("First Two:",numbers[:2])  #extract first two elemets from list
print("Reversed Tuple:",record[::-1])  #reverse the tuple