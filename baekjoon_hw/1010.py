import sys

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

input = sys.stdin.readline

case = int(input())

for i in range(case):
    n,m = list(map(int,input().split()))
    result = factorial(m) / (factorial(n) * (factorial(m - n)))
    print(int(result))
