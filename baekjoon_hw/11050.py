from sys import stdin
n, m = list(map(int, stdin.readline().split()))

# def factorial(number):
#     if number <= 1:
#         return 1
#     return number * factorial(number - 1)

# 원래 쓰는 재귀함수 팩토리얼은 런타임 에러가 난다ㅜㅜㅜ
# 다른 방식으로 팩토리얼 표현 해주기
def factorial(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result    

result = factorial(n) / (factorial(n - m) * factorial(m))
print(int(result))