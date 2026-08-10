def calculator(first_num,second_num,operator):
    if operator=="+":
        return first_num + second_num
    elif operator=="-":
        return first_num - second_num
    elif operator=="*":
        return first_num * second_num
    else:
        return first_num / second_num
    pass

first_num=int(input())
second_num=int(input())
operator=input().strip()

result=calculate(first_num,second_num,operator)
print(result)