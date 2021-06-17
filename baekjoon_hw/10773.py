number = input()
number = int(number)

stack = []
for i in range(number):
    num = input()
    num = int(num)
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
sum = 0
for final_number in stack:
    sum += final_number

print(sum)