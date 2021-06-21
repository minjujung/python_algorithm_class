import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

sum_list = [] 
n = [] 

def dfs_backtracking(start):
    sum = 0
    if len(n) == 3:
        for i in range(3):
            sum += n[i]
        sum_list.append(sum)
    else:
        for i in range(start, N):
            if numbers[i] not in n:
                n.append(numbers[i])
                # i 다음에도 재귀로 함수를 돌림으로서 i보다 큰수를
                # M의 길이 까지만 answer(stack)에 넣어서 print할 수 있다
                dfs_backtracking(i + 1)
                n.pop()

# 1부터 N까지 자연수를 탐색 하므로 start는 무조건 1부터
dfs_backtracking(0)
sum_list = list(set(sum_list))

answer = 0
min = 300000
for i in range(len(sum_list)):
    if sum_list[i] <= M:
        if M - sum_list[i] < min:
            min = M - sum_list[i]
            answer = sum_list[i]

print(answer)



