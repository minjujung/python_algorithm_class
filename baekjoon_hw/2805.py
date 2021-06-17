# tree_number, length = input().split()

# tree_number = int(tree_number)
# length = int(length)

# trees = input().split()

# for i in range(len(trees)):
#     trees[i] = int(trees[i])

# trees.sort()


# current_min = 1
# current_max = trees[len(trees) - 1]


# while current_min <= current_max:
#     current_guess = (current_max + current_min) // 2
#     sum = 0
#     for number in trees:
#         if current_guess <= number:
#             sum += number - current_guess
#     if sum >= length:
#         current_min = current_guess + 1
#     else:
#         current_max = current_guess - 1



# print(binary_search(trees, length))


N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2
    log = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid
    
    #벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)