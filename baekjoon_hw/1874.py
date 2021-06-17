import sys
input = sys.stdin.readline

number = int(input())

numbers = []
temp = []
answer = []
real_answer = []

for i in range(number):
    num = int(input())
    numbers.append(num)

i = 0
j = 1
while answer != numbers:
    if numbers[i] in temp:
        if numbers[i] != temp[len(temp) - 1]:
            break
        else:
            temp.pop()
            answer.append(numbers[i])
            real_answer.append("-")
            i += 1
    else: 
        temp.append(j)
        real_answer.append("+")
        j += 1

if answer == numbers:
    for mark in real_answer:
        print(mark)
else:
    print("NO")