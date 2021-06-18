# import sys
# input = sys.stdin.readline

# node_numeber, case, start_point  = list(map(int, input().split()))

# node_array = []
# node_connected_array = []
# for i in range(case):
#     nodes = list(map(int, input().split()))
#     node_array.append(nodes[0])
#     node_connected_array.append(nodes[1])

# n = len(node_array)
# graph = {}
# for i in range(n):
#     node = node_array[i]
#     node_connected = node_connected_array[i]
#     if node not in graph:
#         graph[node] = [node_connected]
#     else:
#         graph[node].append(node_connected)
#     if node_connected not in graph:
#         graph[node_connected] = [node]
#     else:
#         graph[node_connected].append(node)
# print(graph)

# def dfs_stack(node_graph, start_node):
#     stack = [start_node]
#     visited = []

#     while stack:
#         current_node = stack.pop()
#         visited.append(current_node)
#         for adjacent_node in node_graph[current_node]:
#             print(adjacent_node)
#             if adjacent_node not in visited:
#                 stack.append(adjacent_node)
#     return visited

# def bfs_queue(node_graph, start_node):
#     queue = [start_node]
#     visited = []

#     while queue:
#         current_node = queue.pop(0)
#         visited.append(current_node)
#         for adjacent_node in node_graph[current_node]:
#             if adjacent_node not in visited:
#                 queue.append(adjacent_node)
#     return visited

# print(dfs_stack(graph, start_point) , bfs_queue(graph, start_point))

# 내가 했던 코드의 문제점
# 1. 입력만으로 graph를 만들면 시작노드가 어느 간선과도 연결되지 않은 부분 고려가 안됨!!
#   => [1],  [2] -> [3], [4] -> [5] 일때 시작 node가 1인 경우에는...? 
#   =>  graph = {i:[] for i in range(1,n+1)} 이렇게 모든 노드를 키값으로 초기화 해놔야
#       연결된 간선이 없는 노드를 만났을 때 while queue나 while stack문 빠져 나갈 수 있음!!
#
# 2. 내가 작성한 dfs, bfs는 이진 트리 구조 일때만 가능하다!! 이 문제 처럼 한 node에 자식
#   자식 노드가 2개 보다 많고 서로 연결이 되어 있는 map같은 구조에서는 이미 방문 한 node가 
#   stack로 들어오기 전에 걸러지지 않고 중복되는 인접 node들이 계속 들어오면서 stack.pop()
#   에서 나온걸 넣는 visited에 방문했던 게 또 들어 갈 수 있다. 즉 한 노드 서로 서로 같은 인접 
#   노드들이 있으면서 (ex: 1: [2, 3, 4], 4: [1, 2, 3] 여기서 2와 3) 아직 방문은 안했다면 
#   같은 노드 여도 stack에 추가되는 것!!
#   => 그러므로 visited에 node추가하기 전에 그 node가 visited있는지 확인 해줘야함!!
#
# 3. 문제에서 "문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고" 라고
#   했으므로, sort()로 정렬된 그래프에서 stack.pop()을 하면 제일 끝에 있는 제일 큰 수부터 체크하게
#   되므로 stack에 인접 노드를 추가 할 때 역순으로 넣어주어야 함!!


from collections import deque 
def dfs(graph, v): 
    visited = [] 
    stack = [v] 
    while stack: 
        n = stack.pop() 
        if n not in visited: # 2번 문제 해결 => 방문 했던 node 걸러주는 타이밍 중요!!
            visited.append(n) 
            stack += reversed(graph[n]) # 3번 문제 해결 => 인접 노드 역순으로 나열해서 stack에 넣어주기
            # print(stack) 
    return visited 

def bfs(graph, v): 
    visited = [] 
    queue = deque([v]) 
    while queue: 
        n = queue.popleft() # queue는 앞에서 pop하므로 
        if n not in visited: 
            visited.append(n) 
            queue += graph[n] # 인접 노드를 역순으로 나열 안해줘도 됨!
            # print(queue) 
    return visited 
    
n, m, v = map(int, input().split()) 
graph = {i:[] for i in range(1,n+1)} 

for i in range(1, m+1): 
    x, y = map(int, input().split()) 
    graph[x].append(y) 
    graph[y].append(x) 
    
for key in graph: graph[key].sort()

# visited는 list 이므로 string으로 바꿔서 결과값 출력
print(" ".join(list(map(str, dfs(graph, v)))))
print(" ".join(list(map(str, bfs(graph, v)))))
