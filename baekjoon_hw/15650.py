# backtracking => dfs로 하나하나 탐색하면서 조건에 맞는것만 반환!
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

answer = []
def dfs_backtracking(start):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
    else:
        for i in range(start, N + 1):
            if i not in answer:
                answer.append(i)
                # i 다음에도 재귀로 함수를 돌림으로서 i보다 큰수를
                # M의 길이 까지만 answer(stack)에 넣어서 print할 수 있다
                dfs_backtracking(i + 1)
                answer.pop()

# 1부터 N까지 자연수를 탐색 하므로 start는 무조건 1부터
dfs_backtracking(1)

# N, M = map(int, input().split())

# num_list = [i + 1 for i in range(N)]
# check_list = [False] * N

# arr = []

# def dfs(cnt):
#     if(cnt == M):
#         print(*arr)
#         return
    
#     for i in range(0, N):
#         if(check_list[i]):
#             continue
        
#         check_list[i] = True
#         arr.append(num_list[i])
#         dfs(cnt + 1)
#         arr.pop()
        
#         # 이 부분이 순열하고의 차이점이다.
#         # 큰 나무에서 전에 봤던 것만
#         # 닫아주면 된다.
#         for j in range(i + 1, N):
#             check_list[j] = False
            
        
# dfs(0)