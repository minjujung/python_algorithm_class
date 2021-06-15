# 소수 구할 때 시간 가장 단축시키는 방법은
# 에라토스테네스의 체!!

# 에라토스네테스의 체로 먼저 소수를 구하는 함수 정의
def prime_list(n):
    sieve = [True] * n      # 범위로 주어진 수만큼(n) Trueㄹ 채워진 list 만들기
    m = int(n**0.5)         # n 의 최대 약수가 sqrt(n)이하 이므로 i = sqrt(n)까지 검사
    for i in range(2, m + 1):
        if sieve[i] == True:  # N이 N의 제곱근 보다 크지 않은 어떤 소수로도 나눠지지 않는다.
            for j in range(i+i, n , i):  # 그러므로 i 가 소수면 i의 배수들은 소수 X
                sieve[j] = False   # 소수가 아닌것들은 False 로 변경
    return [i for i in range(2, n) if sieve[i] == True]


while 1:
    n = int(input())
    if n == 0:
        break
    li = prime_list(2 * n + 1)
    # 문제의 범위가 n 보다 크고 2n 보다 작거나 같은 소수의 개수 출력 이므로!! 
    # 2n까지의 소수를 다 구한뒤 n 보다 큰 것의 갯수를 구한다
    print(len([i for i in li if i > n]))   