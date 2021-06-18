import sys

input = sys.stdin.readline

case = int(input())

numbers = []
sum = 0
for i in range(case):
    num = int(input())
    numbers.append(num)
    sum += num

numbers.sort()

print(round(sum/case))

print(numbers[len(numbers)//2])

count = {}
for i in numbers:
    try: count[i] += 1
    except: count[i] = 1

list = [k for k, v in count.items() if max(count.values()) == v]
list.sort()

if len(list) == 1:
    print(list[0])
else:
    print(list[1])

print(numbers[-1] - numbers[0])