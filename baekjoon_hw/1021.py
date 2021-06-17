import sys
from collections import deque


input = sys.stdin.readline

n, m = map(int, input().split())
find_numbers = list(map(int, input().split()))

numbers_list = []

for i in range(1, n + 1):
    numbers_list.append(i)

numbers_left = deque(numbers_list)
numbers_right = deque(numbers_list)

def find_left(n, array):
    count = 0
    while array[0] != n:
        temp = array[0]
        array.popleft()
        array.append(temp)
        count += 1
    return count, array

def find_right(n, array):
    count = 0
    while array[0] != n:
        temp = array[- 1]
        array.pop()
        array.appendleft(temp)
        count += 1
    return count, array


sum = 0
for i in range(len(find_numbers)):
    left = find_left(find_numbers[i], numbers_left)
    right = find_right(find_numbers[i], numbers_right)
    sum += min(left[0], right[0])
    if min(left[0], right[0]) == left[0]:
        numbers_left.popleft()
        numbers_right = deque(list(numbers_left))
    else:
        numbers_right.popleft()
        numbers_left = deque(list(numbers_right))

print(sum)